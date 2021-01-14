from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    #with all of the arguments parameter
    #decorate something
    def wrapper_func(request, *args, **kwargs):
        
        if request.user.is_authenticated:
            return redirect("home")
        else:
            #wiew function is implemented here
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_user(allowed_grp=[]):
    def decorator_func(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                #get the first name's group
                group = request.user.groups.all()[0].name
            if group in allowed_grp:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorize to view this page')
        return wrapper_func
    return decorator_func


def only_admin(view_func):
    #thís is a frame for decorating
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer':
            return redirect('userpage')
        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_func
