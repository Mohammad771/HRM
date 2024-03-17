from django import template
register = template.Library()

@register.simple_tag
def calculate_loan_percentage(complete_payments, all_payments):
    return int((complete_payments/all_payments)*100)