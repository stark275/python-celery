from django import template

register = template.Library()

@register.filter
def get_branch_code(sale):
    return sale.sale[2:].split(':')[0]
    
    