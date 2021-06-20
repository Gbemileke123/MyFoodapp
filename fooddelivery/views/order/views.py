from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from fooddelivery.dto.MealDto import CreateMealDto, EditMealDto, ListMealDto, MealDetailsDto
from fooddelivery.models import Order
from fooddelivery.service_factory import fooddelivery_service_container


def home_meal(request):
    meals = fooddelivery_service_container.meal_management_service().list()
    context = {
        "title": "Order",
        "meals": meals
    }
    return render(request, "fooddelivery/meal/home_meal.html", context)


def view_meal(request, meal_id):
    meal = __get_meal_details_dto_or_raise_404(meal_id)
    context = {
        "title": f"Order {meal.status}",
        "order": meal
    }
    return render(request, "fooddelivery/meal/view_meal.html", context)


def edit_meal(request, meal_id):
    meal_details_dto = __get_meal_details_dto_or_raise_404(meal_id)
    customer = fooddelivery_service_container.customer_management_service().get_all_for_select_list()
    menuitem = fooddelivery_service_container.menuitem_management_service().get_all_for_select_list()
    context = {
        "title": f"Edit Order {meal_details_dto.status}",
        "meal_id": meal_id,
        "order": meal_details_dto,
        "customer": customer,
        "menuitem": menuitem
    }
    new_meal_details_dto = __edit_if_post_method(context, meal_id, request)
    if new_meal_details_dto is not None:
        context["order"] = new_meal_details_dto
    return render(request, "fooddelivery/meal/edit_meal.html", context)


def create_meal(request):
    customer = fooddelivery_service_container.customer_management_service().get_all_for_select_list()
    menuitem = fooddelivery_service_container.menuitem_management_service().get_all_for_select_list()
    context = {
        "customer": customer,
        "menuitem": menuitem
    }
    __create_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect("home")
    return render(request, "fooddelivery/meal/create_meal.html", context)


def delete(request, meal_id):
    try:
        fooddelivery_service_container.meal_management_service().delete(meal_id)
        return redirect("home")
    except Exception:
        raise Http404("No such order exist")


def __create_if_post_method(context, request):
    if request.method == "POST":
        try:
            meal = __get_edit_meal_dto_from_request(request)
            fooddelivery_service_container.meal_management_service().create(meal)
            context["saved"] = True
            return __get_meal_details_dto_or_raise_404(meal)
        except Exception as meals:
            print(meals)
            context["saved"] = False


def __edit_if_post_method(context, meal_id: int, request: HttpRequest) -> MealDetailsDto:
    if request.method == "POST":
        try:
            meal = __get_edit_meal_dto_from_request(meal_id, request)
            fooddelivery_service_container.meal_management_service().edit(meal_id, meal)
            context["saved"] =True
            return __get_meal_details_dto_or_raise_404(meal_id)
        except Exception as meals:
            print(meals)
            context["saved"] = False


def __get_create_meal_dto_from_request(request: HttpRequest) -> CreateMealDto:
    create_meal_dto = CreateMealDto()
    create_meal_dto.status = request.POST["status"]
    __set_meal_attributes_from_request(create_meal_dto, request)
    return create_meal_dto


def __get_edit_meal_dto_from_request(meal_id: int, request: HttpRequest) -> EditMealDto:
    edit_meal_dto = EditMealDto()
    edit_meal_dto.id = meal_id
    __set_meal_attributes_from_request(edit_meal_dto, request)
    return edit_meal_dto


def __set_meal_attributes_from_request(edit_meal_dto, request):
    edit_meal_dto.menuitem_id = int(request.POST["menuitem_id"])
    edit_meal_dto.customers_id = int(request.POST["customer_id"])
    edit_meal_dto.status = request.POST["status"]
    edit_meal_dto.address = request.POST["address"]
    edit_meal_dto.quantity = request.POST["quantity"]
    edit_meal_dto.rate = request.POST["rate"]
    edit_meal_dto.order_date = request.POST["order_date"]
    edit_meal_dto.order_time = request.POST["order_time"]


def __get_meal_details_dto_or_raise_404(meal_id) -> MealDetailsDto:
    try:
        meal = fooddelivery_service_container.meal_management_service().get(meal_id=meal_id)
    except Order.DoesNotExist:
        raise Http404("The request order does not exist")
    return meal
