from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from fooddelivery.dto.RestaurantDto import CreateRestaurantDto, EditRestaurantDto, RestaurantDetailsDto, ListRestaurantDto
from fooddelivery.models import Restaurant
from fooddelivery.service_factory import fooddelivery_service_container
from django.contrib.auth.decorators import login_required
from fooddelivery.decorator import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_user=['Restaurant'])
def restaurant_homepage(request):
    menuitem = fooddelivery_service_container.menuitem_management_service().list()
    context = {
        "menuitem": menuitem
    }
    return render(request, "fooddelivery/restaurant/restaurant_homepage.html", context)


def home_restaurant(request):
    restaurant = fooddelivery_service_container.restaurant_management_service().list()
    context = {
        "title": "Restaurant",
        "restaurant": restaurant
    }
    return render(request, "fooddelivery/restaurant/home_restaurant.html", context)


def view_restaurant(request, restaurant_id):
    restaurant = __get_restaurant_details_dto_or_raise_404(restaurant_id)
    context = {
        "title": f"Restaurant {restaurant.name}",
        "restaurant": restaurant

    }
    return render(request, "fooddelivery/restaurant/view_restaurant.html", context)


def edit_restaurant(request, restaurant_id):
    restaurant_details_dto = __get_restaurant_details_dto_or_raise_404(restaurant_id)
    context = {
        "title": f"Restaurant {restaurant_details_dto.name}",
        "restaurant": restaurant_details_dto
    }
    new_restaurant_details_dto = __edit_if_post_method(context, restaurant_id, request)
    if new_restaurant_details_dto is not None:
        context["restaurant"] = new_restaurant_details_dto
    return render(request, "fooddelivery/restaurant/edit_restaurant.html", context)


def create_restaurant(request):
    context = {

    }
    __create_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect("login")
    return render(request, "fooddelivery/restaurant/create_restaurant.html", context)


def get_restaurant_for_select(request):
    restaurant = fooddelivery_service_container.restaurant_management_service().get_all_for_select_list()
    context = {
        "restaurant": restaurant
    }
    return JsonResponse(context)


def delete_restaurant(request, restaurant_id: int):
    try:
        fooddelivery_service_container.restaurant_management_service().delete(restaurant_id)
        return redirect("home_restaurant")
    except Exception:
        raise Http404("No such restaurant exists")


def __create_if_post_method(context, request):
    if request.method == "POST":
        try:
            restaurant = __get_create_restaurant_dto_from_request(request)
            fooddelivery_service_container.restaurant_management_service().create(restaurant)
            context["saved"] = True
        except Exception as r:
            print(r)
            context["saved"] = False


def __edit_if_post_method(context, restaurant_id: int, request: HttpRequest) -> RestaurantDetailsDto:
    if request.method == "POST":
        try:
            restaurant = __get_edit_restaurant_dto_from_request(restaurant_id, request)
            fooddelivery_service_container.restaurant_management_service().edit(restaurant_id, restaurant)
            context["saved"] = True
            return __get_restaurant_details_dto_or_raise_404(restaurant_id)
        except Exception as r:
            print(r)
            context["saved"] = False


def __get_create_restaurant_dto_from_request(request: HttpRequest) -> CreateRestaurantDto:
    create_restaurant_dto = CreateRestaurantDto()
    create_restaurant_dto.username = request.POST["username"]
    __set_restaurant_attributes_from_request(create_restaurant_dto, request)
    return create_restaurant_dto


def __get_edit_restaurant_dto_from_request(restaurant_id: int, request: HttpRequest) -> EditRestaurantDto:
    edit_restaurant_dto = EditRestaurantDto()
    edit_restaurant_dto.id = restaurant_id
    __set_restaurant_attributes_from_request_edit(edit_restaurant_dto, request)
    return edit_restaurant_dto


def __set_restaurant_attributes_from_request_edit(edit_restaurant_dto, request):
    edit_restaurant_dto.restaurant_address = request.POST["restaurant_address"]
    edit_restaurant_dto.restaurant_contact = request.POST["restaurant_contact"]
    edit_restaurant_dto.food_description = request.POST['food_description']


def __set_restaurant_attributes_from_request(create_restaurant_dto, request):
    create_restaurant_dto.username = request.POST["username"]
    create_restaurant_dto.password = request.POST["password"]
    create_restaurant_dto.email = request.POST["email"]
    create_restaurant_dto.name = request.POST["name"]
    create_restaurant_dto.restaurant_address = request.POST["restaurant_address"]
    create_restaurant_dto.restaurant_contact = request.POST["restaurant_contact"]
    create_restaurant_dto.food_description = request.POST['food_description']


def __get_restaurant_details_dto_or_raise_404(restaurant_id) -> RestaurantDetailsDto:
    try:
        restaurant = fooddelivery_service_container.restaurant_management_service().get(restaurant_id=restaurant_id)
    except Restaurant.DoesNotExist:
        raise Http404("The requested restaurant does not exist")
    return restaurant
