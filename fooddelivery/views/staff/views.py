from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from fooddelivery.dto.StaffDto import CreateStaffDto, EditStaffDto, ListStaffDto, StaffDetailsDto
from fooddelivery.models import Staff
from fooddelivery.service_factory import fooddelivery_service_container
from django.contrib.auth.decorators import login_required
from fooddelivery.decorator import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_user=['Staff'])
def staff_homepage(request):
    context = {

    }
    return render(request, "fooddelivery/staff/staff_homepage.html", context)


def home_staff(request):
    staff = fooddelivery_service_container.staff_management_service().list()
    context = {
        "title": "Staff",
        "staff": staff
    }
    return render(request, "fooddelivery/staff/home_staff.html", context)


def view_staff(request, staff_id):
    staff = __get_staff_details_dto_or_raise_404(staff_id)
    context = {
        "title": f"Staff {staff.last_name}",
        "staff": staff
    }
    return render(request, "fooddelivery/staff/view_staff.html", context)


def edit_staff(request, staff_id):
    staff_details_dto = __get_staff_details_dto_or_raise_404(staff_id)
    context = {
        "title": f"Edit Staff {staff_details_dto.last_name}",
        "staff": staff_details_dto,
    }
    new_staff_details_dto = __edit_if_post_method(context, staff_id, request)
    if new_staff_details_dto is not None:
        context["staff"] = new_staff_details_dto
    return render(request, "fooddelivery/staff/edit_staff.html", context)


def create_staff(request):
    context = {

    }
    __create_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect("staff_homepage")
    return render(request, "fooddelivery/staff/create_staff.html", context)


def delete_staff(request, staff_id: int):
    try:
        fooddelivery_service_container.staff_management_service().delete(staff_id)
        return redirect("home_staff")
    except Exception as e:
        raise Http404("Staff does not exist")


def get_staff_for_select(request):
    staff = fooddelivery_service_container.staff_management_service.get_all_for_select_list()
    context = {
        "staff": staff
    }
    return JsonResponse(context)


def __create_if_post_method(context, request):
    if request.method == "POST":
        try:
            staff = __get_create_staff_dto_from_request(request)
            fooddelivery_service_container.staff_management_service().create(staff)
            context["saved"] = True
        except Exception as c:
            print(c)
            context["saved"] = False


def __edit_if_post_method(context, staff_id: int, request: HttpRequest) -> StaffDetailsDto:
    if request.method == "POST":
        try:
            staff = __get_edit_staff_dto_from_request(staff_id, request)
            fooddelivery_service_container.staff_management_service().edit(staff_id, staff)
            context["saved"] = True
            return __get_staff_details_dto_or_raise_404(staff_id)
        except Exception as s:
            print(s)
            context["saved"] = False


def __get_create_staff_dto_from_request(request: HttpRequest) -> CreateStaffDto:
    create_staff_dto = CreateStaffDto()
    create_staff_dto.username = request.POST["username"]
    create_staff_dto.password = request.POST["password"]
    __set_staff_attributes_from_request(create_staff_dto, request)
    return create_staff_dto


def __get_edit_staff_dto_from_request(staff_id: int, request: HttpRequest) -> EditStaffDto:
    edit_staff_dto = EditStaffDto()
    edit_staff_dto.id = staff_id
    __set_staff_attributes_from_request(edit_staff_dto, request)
    return edit_staff_dto


def __set_staff_attributes_from_request(dto, request):
    dto.first_name = request.POST["first_name"]
    dto.last_name = request.POST["last_name"]
    dto.email = request.POST["email"]
    dto.staff_address = request.POST["staff_address"]
    dto.staff_contact = request.POST["staff_contact"]


def __get_staff_details_dto_or_raise_404(staff_id) -> StaffDetailsDto:
    try:
        staff = fooddelivery_service_container.staff_management_service().get(staff_id=staff_id)
    except Staff.DoesNotExist:
        raise Http404("The requested staff does not exist")
    return staff
