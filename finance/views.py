from django.shortcuts import render
# from datetime import datetime
from .models import rewards as rewards_model
from .models import punishments as punishments_model
from users.models import users
from track_performance.models import attendance
from employees_requests.models import overtime
from HRM.CRUD import *

# Create your views here.

def punishments(request):

    context = {}
    if request.method == "POST":
        print(request.POST)
        result = Create(request.POST, 'punishments')
        if result["status"] == True:
            context["success_message"] = "Alhamdulillah"
        else:
            context["form_errors"] = result['form_errors']

    context['viewPunishment'] = Read("punishments")
    context["users"] = Read("users")
    return render(request, 'finance/punishments.html', context)

def rewards(request):
    context = {}
    if request.method == "POST":
        result = Create(request.POST, 'rewards')
        if result["status"] == True:
            context["success_message"] = "Reward has been added 👍"
        else:
            context["form_errors"] = result['form_errors']

    context['viewReward'] = Read("rewards")
    context["users"] = Read("users")
    return render(request, 'finance/rewards.html', context)

def create_payroll(request):
    context = {}
    if request.method == "POST":
        user_id = request.POST['user_id']
        current_date = datetime.datetime.today()
        current_month = current_date.month
        next_month = current_month + 1
        beginning_of_month = str(current_date.year) + "-" + str(current_month) + "-01"
        end_of_month = str(current_date.year) + "-" + str(next_month) + "-01"
        print(beginning_of_month)
        print(end_of_month)
        selected_user = users.objects.get(pk=user_id)
        user_attendance_rows = attendance.objects.filter(attendance_user_id=selected_user).filter(
            attendance_created_at__range=(beginning_of_month, end_of_month))

        # total_attendance_hours = datetime.datetime.strptime("00:00", '%H:%M').time()
        # total_attendance_hours = total_attendance_hours.hour + total_attendance_hours.minute/60.0
        total_attendance_hours = 0

        for attendance_row in user_attendance_rows:
            total_attendance_hours = total_attendance_hours + (
                attendance_row.attendance_duration.hour + attendance_row.attendance_duration.minute/60.0)
            # total_attendance_hours = add_dates(total_attendance_hours, attendance_row.attendance_duration)
            # days = datetime.combine(date.min, total_attendance_hours) + datetime.combine(date.min, start)
            # total_attendance_hours = total_attendance_hours + attendance_row.attendance_duration
        total_attendance_hours = round(total_attendance_hours, 2)
        context['total_attendance_hours'] = total_attendance_hours
        context['total_absence_hours'] = 240 - total_attendance_hours
        context['attendance_ratio'] = round((total_attendance_hours / 240), 2)

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

        if selected_user.user_salary == None:
            total_month_salary = total_overtime_hours*30 + total_rewards_and_punishments
        else:
            total_month_salary = selected_user.user_salary + total_overtime_hours*30 + total_rewards_and_punishments

        context['total_month_salary'] = total_month_salary
        context['selected_user'] = selected_user

    context["users"] = Read("users")
    return render(request, 'finance/create_payroll.html', context)

def view_payroll(request):
    return render(request, 'finance/view_payroll.html')

def add_dates(start, end):
    today = datetime.date.today()
    d_start = datetime.datetime.combine(today, start)
    d_end = datetime.datetime.combine(today, end)
    result = d_end - d_start
    return result