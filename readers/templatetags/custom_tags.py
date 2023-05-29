from django import template

register = template.Library()

@register.filter
def mul(int, val):
    return int*val

@register.filter
def list(num):
    return range(num)

@register.filter
def elem1(array, index):
    return array[2*index + 1]

@register.filter
def elem2(array, index):
    return array[2*index + 2]