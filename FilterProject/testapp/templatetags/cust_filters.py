from django import template
register = template.Library()

def truncate5(value):
    result=value[0:5]
    return result

register.filter('truncate5',truncate5)

@register.filter(name='t_n')          ###To register the filter you can use decorator 
def truncate_n(value,n):
    result=value[0:n]
    return result




