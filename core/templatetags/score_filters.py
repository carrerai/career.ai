from django import template

register = template.Library()

@register.filter
def percentage(score, max_score):
    try:
        if max_score == 0:
            return 0
        return int((abs(score) / abs(max_score)) * 100)
    except (ValueError, TypeError):
        return 0

@register.filter
def lookup(dictionary, key):
    return dictionary.get(key, 0)
