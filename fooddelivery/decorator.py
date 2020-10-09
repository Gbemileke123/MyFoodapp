from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_users(allowed_user=None):
    if allowed_user is None:
        allowed_user = []

    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_user:
                return view_function(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized. Thank you!")
        return wrapper_function
    return decorator