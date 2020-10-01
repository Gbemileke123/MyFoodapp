from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from fooddelivery.dto.CustomersDto import CreateCustomersDto, EditCustomersDto, ListCustomersDto, CustomersDetailsDto
from fooddelivery.models import Customer
from fooddelivery.service_factory import fooddelivery_service_container
from django.contrib.auth.decorators import login_required
from fooddelivery.decorator import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_user=['Customer'])
def home_customer(request):
    customer = fooddelivery_service_container.customer_management_service().list()
    context = {
        "title": "Customer",
        "customer": customer
    }
    return render(request, "fooddelivery/customer/home_customer.html", context)


def view_customer(request, customer_id):
    customer = __get_customer_details_dto_or_raise_404(customer_id)
    context = {
        "title": f"Customer{customer.user_last_name}",
        "customer": customer
    }
    return render(request, "fooddelivery/customer/view_customer.html", context)


def edit_customer(request, customer_id):
    customer_details_dto = __get_customer_details_dto_or_raise_404(customer_id)
    context = {
        "title": f"Edit Customer {customer_details_dto.user_last_name}",
        "customer": customer_details_dto,
    }
    new_customer_details_dto = __edit_if_post_method(context, customer_id, request)
    if new_customer_details_dto is not None:
        context["customer"] = new_customer_details_dto
    return render(request, "fooddelivery/customer/edit_customer.html", context)


def create_customer(request):
    context = {

    }
    __create_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect("home_customer")
    return render(request, "fooddelivery/customer/create_customer.html", context)


def delete_customer(request, customer_id: int):
    try:
        fooddelivery_service_container.menu_management_service().delete(customer_id)
        return redirect("home_customer")
    except Exception:
        raise Http404("Customer does not exist")


def get_customer_for_select(request):
    customer = fooddelivery_service_container.customer_management_service.get_all_for_select_list()
    context = {
        "customer": customer
    }
    return JsonResponse(context)


def __create_if_post_method(context, request):
    if request.method == "POST":
        try:
            customer = __get_create_customer_dto_from_request(request)
            fooddelivery_service_container.customer_management_service().create(customer)
            context["saved"] = True
        except Exception as c:
            print(c)
            context["saved"] = False


def __edit_if_post_method(context, customer_id: int, request: HttpRequest) -> CustomersDetailsDto:
    if request.method == "POST":
        try:
            customer = __get_edit_customer_dto_from_request(customer_id, request)
            fooddelivery_service_container.customer_management_service().edit(customer_id, customer)
            context["saved"] = True
            return __get_customer_details_dto_or_raise_404(customer_id)
        except Exception as c:
            print(c)
            context["saved"] = False


def __get_create_customer_dto_from_request(request: HttpRequest) -> CreateCustomersDto:
    create_customer_dto = CreateCustomersDto()
    create_customer_dto.user_last_name = request.POST["user_last_name"]
    __set_customer_attributes_from_request_create(create_customer_dto, request)
    return create_customer_dto


def __get_edit_customer_dto_from_request(customer_id: int, request: HttpRequest) -> EditCustomersDto:
    edit_customer_dto = EditCustomersDto()
    edit_customer_dto.id = customer_id
    __set_customer_attributes_from_request(edit_customer_dto, request)
    return edit_customer_dto


def __set_customer_attributes_from_request(edit_customer_dto, request):
    edit_customer_dto.user_first_name = request.POST["user_first_name"]
    edit_customer_dto.user_last_name = request.POST["user_last_name"]
    edit_customer_dto.email = request.POST["email"]
    edit_customer_dto.address = request.POST["address"]
    edit_customer_dto.contact = request.POST["contact"]


def __set_customer_attributes_from_request_create(create_customer_dto, request):
    create_customer_dto.username = request.POST["username"]
    create_customer_dto.password = request.POST["password"]
    create_customer_dto.user_first_name = request.POST["user_first_name"]
    create_customer_dto.user_last_name = request.POST["user_last_name"]
    create_customer_dto.email = request.POST["email"]
    create_customer_dto.address = request.POST["address"]
    create_customer_dto.contact = request.POST["contact"]


def __get_customer_details_dto_or_raise_404(customer_id) -> CustomersDetailsDto:
    try:
        customer = fooddelivery_service_container.customer_management_service().get(customer_id=customer_id)
    except Customer.DoesNotExist:
        raise Http404("The requested customer does not exist")
    return customer
