from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Return encoded URL parameters that are the same as the current
    request's parameters, only with the specified GET parameters added or changed.

    It also removes any empty parameters to keep things neat,
    so you can remove a parm by setting it to ``""``.

    For example, if you're on the page ``/things/?with_frosting=true&page=5``,
    then

    <a href="/things/?{% param_replace page=3 %}">Page 3</a>

    would expand to

    <a href="/things/?with_frosting=true&page=3">Page 3</a>

    Based on
    https://stackoverflow.com/questions/22734695/next-and-before-links-for-a-django-paginated-query/22735278#22735278

    Article
    https://www.caktusgroup.com/blog/2018/10/18/filtering-and-pagination-django/
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()


@register.inclusion_tag('core/components/breadcrumb.html')
def breadcrumb(label, view_name, active):
    return {
        'label': label,
        'view_name': view_name,
        'active': active,
    }

@register.inclusion_tag('core/components/search_field.html')
def search_field(view_name, search):
    return {
        'view_name': view_name,
        'search': search,
    }