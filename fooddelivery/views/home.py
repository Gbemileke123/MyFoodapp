from django.shortcuts import render

from fooddelivery.service_factory import fooddelivery_service_container


def home_page(request):
    menu = fooddelivery_service_container.menu_management_service().list()
    context = {
        "title": "Home",
        'menu': menu,
        'logged_in': request.user.is_authenticated
    }
    return render(request, "fooddelivery/Home/home.html", context)


def about(request):
    context = {
        "title": "About"
    }
    return render(request, "fooddelivery/Home/about.html", context)


def contact(request):
    context = {
        "title": "contact"
    }
    return render(request, "fooddelivery/Home/contact.html", context)
