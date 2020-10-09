from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from fooddelivery.dto.MenuDto import CreateMenuDto, EditMenuDto, ListMenuDto, MenuDetailsDto
from fooddelivery.models import Menu
from fooddelivery.service_factory import fooddelivery_service_container

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home_menu(request):
    menu = fooddelivery_service_container.menu_management_service().list()
    context = {
        "title": "Menu",
        "menus": menu

    }
    return render(request, "fooddelivery/menu/home_menu.html", context)


@login_required(login_url='login')
def view_menu(request, menu_id):
    menu = __get_menu_details_dto_or_raise_404(menu_id)
    context = {
        "title": f"Menu {menu.menu_version}",
        "menus": menu

    }
    return render(request, "fooddelivery/menu/view_menu.html", context)


def create_menu(request):

    context = {

    }
    __create_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect("create_menuitem")
    return render(request, "fooddelivery/menu/create_menu.html", context)


def edit_menu(request, menu_id):
    menu_details_dto = __get_menu_details_dto_or_raise_404(menu_id)
    context = {
        "title": f"Edit Menu {menu_details_dto.menu_version}",
        "menu_id": menu_id,
        "menu": menu_details_dto,

    }
    new_menu_details_dto = __edit_if_post_method(context, menu_id, request)
    if new_menu_details_dto is not None:
        context["menu"] = new_menu_details_dto
    return render(request, "fooddelivery/menu/edit_menu.html", context)


def get_menu_for_select(request):
    menu = fooddelivery_service_container.menu_management_service().get_all_for_select_list()
    context = {
        "menu": menu
    }
    return JsonResponse(context)


def delete_menu(request, menu_id: int):
    try:
        fooddelivery_service_container.menu_management_service().delete(menu_id)
        return redirect("home_menu")
    except Exception:
        raise Http404("Menu does not exist")


def __create_if_post_method(context, request):
    if request.method == "POST":
        try:
            menu = __get_create_menu_dto_from_request(request)
            fooddelivery_service_container.menu_management_service().create(menu)
            context["saved"] = True
        except Exception as m:
            print(m)
            context["saved"] = False


def __edit_if_post_method(context, menu_id: int, request: HttpRequest):
    if request.method == "POST":
        try:
            menu = __get_edit_menu_dto_from_request(menu_id, request)
            fooddelivery_service_container.menu_management_service().edit(menu_id, menu)
            context["saved"] = True
            return __get_menu_details_dto_or_raise_404(menu_id)
        except Exception as m:
            print(m)
            context["saved"] = False


def __get_create_menu_dto_from_request(request: HttpRequest) -> CreateMenuDto:
    create_menu_dto = CreateMenuDto()
    create_menu_dto.menu_version = request.POST["menu_version"]
    __set_menu_attributes_from_request_create(create_menu_dto, request)
    return create_menu_dto


def __get_edit_menu_dto_from_request(menu_id: int, request: HttpRequest) -> EditMenuDto:
    edit_menu_dto = EditMenuDto()
    edit_menu_dto.id = menu_id
    __set_menu_attributes_from_request(edit_menu_dto, request)
    return edit_menu_dto


def __set_menu_attributes_from_request(edit_menu_dto, request):
    edit_menu_dto.menu_version = request.POST["menu_version"]
    edit_menu_dto.other_details = request.POST["other_details"]
    edit_menu_dto.image_url = request.POST["image_url"]


def __set_menu_attributes_from_request_create(create_menu_dto, request):
    create_menu_dto.menu_version = request.POST["menu_version"]
    create_menu_dto.other_details = request.POST["other_details"]
    create_menu_dto.date_of_creation = request.POST["date_of_creation"]
    create_menu_dto.image_url = request.POST["image_url"]


def __get_menu_details_dto_or_raise_404(menu_id) -> MenuDetailsDto:
    try:
        menu = fooddelivery_service_container.menu_management_service().get(menu_id)
    except Menu.DoesNotExist:
        raise Http404("The requested menu does not exist")
    return menu