from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect

from fooddelivery.dto.MenuItemDto import CreateMenuItemDto, EditMenuItemDto, MenuItemDetailsDto, ListMenuItemDto, SearchMenuItemDto
from fooddelivery.models import MenuItem
from fooddelivery.service_factory import fooddelivery_service_container
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home_menuitem(request):
    menuitem = fooddelivery_service_container.menuitem_management_service().list()
    context = {
        "title": "MenuItem",
        "menuitem": menuitem
    }
    return render(request, "fooddelivery/restaurant/home_restaurant.html", context)


def view_menuitem(request, menuitem_id):
    menuitem = __get_menuitem_details_dto_or_raise_404(menuitem_id)
    context = {
        "title": f"MenuItem {menuitem.item_name}",
        "menuitem": menuitem
    }
    return render(request, "fooddelivery/menuitem/view_menuitem.html", context)


def edit_menuitem(request, menuitem_id):
    menuitem_details_dto = __get_menuitem_details_dto_or_raise_404(menuitem_id)
    menu = fooddelivery_service_container.menu_management_service().get_all_for_select_list()
    context = {
        "title": f"Edit MenuItem {menuitem_details_dto.item_name}",
        "menuitem_id": menuitem_id,
        "menuitem": menuitem_details_dto,
        "menu": menu
    }
    new_menuitem_details_dto = __edit_if_post_method(context, menuitem_id, request)
    if new_menuitem_details_dto is not None:
        context["menuitem"] = new_menuitem_details_dto
    return render(request, "fooddelivery/menuitem/edit_menuitem.html", context)


@login_required(login_url='login')
def create_menuitem(request):
    menu = fooddelivery_service_container.menu_management_service().get_all_for_select_list()
    context = {
        "menu": menu
    }
    __create_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect("restaurant_homepage")
    return render(request, "fooddelivery/menuitem/create_menuitem.html", context)


def delete_menuitem(request, menuitem_id: int):
    try:
        fooddelivery_service_container.menuitem_management_service().delete(menuitem_id)
        return redirect("restaurant_homepage")
    except Exception:
        raise Http404("No such menu item exists")


def __create_if_post_method(context, request):
    if request.method == "POST":
        try:
            menuitem = __get_create_menuitem_dto_from_request(request)
            fooddelivery_service_container.menuitem_management_service().create(menuitem)
            context["saved"] = True
        except Exception as e:
            print(e)
            context["saved"] = False


def __edit_if_post_method(context, menuitem_id: int, request: HttpRequest) -> MenuItemDetailsDto:
    if request.method == "POST":
        try:
            menuitem = __get_edit_menuitem_dto_from_request(menuitem_id, request)
            fooddelivery_service_container.menuitem_management_service().edit(menuitem_id, menuitem)
            context["saved"] = True
            return __get_menuitem_details_dto_or_raise_404(menuitem_id)
        except Exception as e:
            print(e)
            context["saved"] = False


def __get_create_menuitem_dto_from_request(request: HttpRequest) -> CreateMenuItemDto:
    create_menuitem_dto = CreateMenuItemDto()
    create_menuitem_dto.item_name = request.POST["item_name"]
    __set_menuitem_attributes_from_request(create_menuitem_dto, request)
    return create_menuitem_dto


def __get_edit_menuitem_dto_from_request(menuitem_id: int, request: HttpRequest) -> EditMenuItemDto:
    edit_menuitem_dto = EditMenuItemDto()
    edit_menuitem_dto.id = menuitem_id
    __set_menuitem_attributes_from_request(edit_menuitem_dto, request)
    return edit_menuitem_dto


def __set_menuitem_attributes_from_request(edit_menuitem_dto, request):
    edit_menuitem_dto.menu_id = request.POST["menu_id"]
    edit_menuitem_dto.item_name = request.POST["item_name"]
    edit_menuitem_dto.item_description = request.POST["item_description"]
    edit_menuitem_dto.item_price = request.POST["item_price"]
    edit_menuitem_dto.other_details = request.POST["other_details"]
    edit_menuitem_dto.image_url = request.POST["image_url"]


def __get_menuitem_details_dto_or_raise_404(menuitem_id) -> MenuItemDetailsDto:
    try:
        menuitem = fooddelivery_service_container.menuitem_management_service().get(menuitem_id=menuitem_id)
    except MenuItem.DoesNotExist:
        raise Http404("The requested menu item does not exist")
    return menuitem


def search_menuitem(request) -> SearchMenuItemDto:
    menuitem = fooddelivery_service_container.menuitem_management_service().search_menuitem(request.GET.get("item_name", None), request.GET.get("item_description"))
    context = {
        "menuitem": menuitem,
        "item_name": request.GET.get("item_name"),
        "item_description": request.GET.get("item_description"),
    }
    return render(request, "fooddelivery/menuitem/search_menuitem.html", context)


def __search_if_post_method(context, request):
    if request.method == "POST":
        try:
            menuitem = __get_search_menuitem_dto_from_request(request)
            fooddelivery_service_container.menuitem_management_service().search(menuitem)
            context["saved"] = True
        except Exception as e:
            print(e)
            context["saved"] = False


def __get_search_menuitem_dto_from_request(request: HttpRequest) -> SearchMenuItemDto:
    search_menuitem_dto = SearchMenuItemDto()
    search_menuitem_dto.item_name = request.POST["item_name"]
    __set_menuitem_attributes_from_request(search_menuitem_dto, request)
    return search_menuitem_dto