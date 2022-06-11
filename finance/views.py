from django.shortcuts import render
import string
import random
from django.utils import timezone
from .models import rewards as rewards_model
from .models import punishments as punishments_model
from .models import payrolls
from users.models import users
from track_performance.models import attendance
from employees_requests.models import overtime
from HRM.CRUD import *

# Create your views here.

def punishments(request):
    context = {}
    if request.user.is_admin:
        if request.method == "POST":
            if request.POST["request_type"] == "delete":
                result = Delete("punishments", request.POST["punishment_id"])
                if result['status']:
                    context["success_notification"] = "Operation Successful 👍"
                else:
                    print(result['error'])
            else:
                result = Create(request.POST, 'punishments')
                if result["status"] == True:
                    context["success_notification"] = "Operation Successful 👍"
                else:
                    context["form_errors"] = result['form_errors']

        context['viewPunishment'] = Read("punishments")
        context["users"] = Read("users")
    else:
        context['viewPunishment'] = Read("punishments", request.user)
    return render(request, 'finance/punishments.html', context)
        
def rewards(request):
    context = {}
    if request.user.is_admin:
        if request.method == "POST":
            if request.POST["request_type"] == "delete":
                result = Delete("rewards", request.POST["reward_id"])
                if result['status']:
                    context["success_notification"] = "Operation Successful 👍"
                else:
                    print(result['error'])
            else:
                
                result = Create(request.POST, 'rewards')
                if result["status"] == True:
                    context["success_notification"] = "Operation Successful 👍"
                else:
                    context["form_errors"] = result['form_errors']

        context['viewReward'] = Read("rewards")
        context["users"] = Read("users")
    else:
        context['viewReward'] = Read("rewards", request.user)
    return render(request, 'finance/rewards.html', context)

def create_payroll(request):
    context = {}

    if request.method == "POST" and "sign_off" in request.POST:
        
        payroll_confirmation = request.POST["payroll_confirmation"]
        payroll_query = payrolls.objects.filter(payroll_confirmation=payroll_confirmation)

        if len(payroll_query) < 1:
            context["error"] = "The system received an incorrect security token, this incident has been reported. If this wasn't a mistake, you are in a big trouble."
        else:
    
            payroll_row = payroll_query[0]

            payroll_row.payroll_signed_off = True
            payroll_row.payroll_sign_off_date = timezone.now()
            payroll_row.payroll_updated_at = timezone.now()
            payroll_row.save()

            context["users"] = Read("users")
            context["success_notification"] = "Operation Successful 👍"
            return render(request, 'finance/create_payroll.html', context)


    elif request.method == "POST":
        user_id = request.POST['user_id']
        selected_user = users.objects.get(pk=user_id)
        

    else:
        selected_user = request.user

    current_date = datetime.datetime.today()
    current_month = current_date.month
    current_day = current_date.day
    next_month = current_month + 1
    beginning_of_month = str(current_date.year) + "-" + str(current_month) + "-01"
    end_of_month = str(current_date.year) + "-" + str(next_month) + "-01"
    user_attendance_rows = attendance.objects.filter(attendance_user_id=selected_user).filter(
        attendance_created_at__range=(beginning_of_month, end_of_month))

    total_attendance_hours = 0

    for attendance_row in user_attendance_rows:
        total_attendance_hours = total_attendance_hours + (
            attendance_row.attendance_duration.hour + attendance_row.attendance_duration.minute/60.0)

    total_attendance_hours = round(total_attendance_hours, 2)
    context['total_attendance_hours'] = total_attendance_hours
    context['total_absence_hours'] = (current_day * 8) - total_attendance_hours
    attendance_ratio = round((total_attendance_hours / 240), 2)
    context['attendance_ratio'] = attendance_ratio

    user_overtimes = overtime.objects.filter(overtime_user_id=selected_user).filter(
        overtime_date__range=(beginning_of_month, end_of_month))
    total_overtime_hours = 0
    for user_overtime in user_overtimes:
        total_overtime_hours = total_overtime_hours + user_overtime.overtime_hours
    context['user_overtimes'] = user_overtimes
    context['total_overtime_hours'] = total_overtime_hours

    user_rewards = rewards_model.objects.filter(reward_user_id=selected_user).filter(
        reward_created_at__range=(beginning_of_month, end_of_month))

    user_punishments = punishments_model.objects.filter(punishment_user_id=selected_user).filter(
        punishment_created_at__range=(beginning_of_month, end_of_month))

    if len(user_rewards) or len(user_punishments):

        total_user_rewards = 0
        total_user_punishmets = 0

        for reward in user_rewards:
            total_user_rewards = reward.reward_amount
        for punishment in user_punishments:
            total_user_punishmets = punishment.punishment_amount

        total_rewards_and_punishments = total_user_rewards - total_user_punishmets
        context['total_rewards_and_punishments'] = total_rewards_and_punishments
        context['user_rewards'] = user_rewards
        context['user_punishments'] = user_punishments
    else:
        total_rewards_and_punishments = 0

    if selected_user.user_salary == None:
        total_month_salary = total_overtime_hours*30 + total_rewards_and_punishments
    else:
        total_month_salary = (selected_user.user_salary * attendance_ratio) + total_overtime_hours*30 + total_rewards_and_punishments

    context['total_month_salary'] = round(total_month_salary, 2)
    context['selected_user'] = selected_user


    check_existing_payroll = payrolls.objects.filter(payroll_user_id=selected_user).filter(
        payroll_created_at__range=(beginning_of_month, end_of_month))

    if len(check_existing_payroll) < 1:

        payroll_confirmation = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
        payroll = payrolls(payroll_user_id=selected_user, payroll_net_salary=total_month_salary, payroll_confirmation=payroll_confirmation)
        payroll.save()

        context['payroll_confirmation'] = payroll_confirmation
    else:

        if check_existing_payroll[0].payroll_signed_off:
            context['already_signed_off'] = "The payroll for this employee in this month has already been signed off"
        else:
            context['payroll_confirmation'] = check_existing_payroll[0].payroll_confirmation

    context["users"] = Read("users")
    return render(request, 'finance/create_payroll.html', context)

def view_payroll(request):
    context = {}
    context["payrolls"] = Read("payrolls")
    return render(request, 'finance/view_payroll.html',context)

def add_dates(start, end):
    today = datetime.date.today()
    d_start = datetime.datetime.combine(today, start)
    d_end = datetime.datetime.combine(today, end)
    result = d_end - d_start
    return result