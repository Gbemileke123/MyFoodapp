from abc import ABCMeta, abstractmethod
from typing import List

from django.contrib.auth.models import User, Group
from fooddelivery.dto.StaffDto import CreateStaffDto, EditStaffDto, ListStaffDto, StaffDetailsDto
from fooddelivery.models import Staff


class StaffRepository(metaclass=ABCMeta):
    @abstractmethod
    def create(self, model: CreateStaffDto):
        """Create a customer object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: int, model: EditStaffDto):
        """Update customer object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListStaffDto]:
        """Gets list of customers"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, staff_id: int):
        """Deletes a staff object"""
        raise NotImplementedError

    @abstractmethod
    def get(self, staff_id: int):
        """Gets a single customer"""
        raise NotImplementedError


class DjangoORMStaffRepository(StaffRepository):
    def create(self, model: CreateStaffDto):
        staff = Staff()
        staff.staff_address = model.staff_address
        staff.staff_contact = model.staff_contact

        # create the user
        user = User.objects.create_user(model.username, model.email, model.password)
        user.first_name = model.first_name
        user.last_name = model.last_name
        user.save()

        staff.user = user
        staffs = Group.objects.get(name='Staff')
        user.groups.add(staffs)

        staff.save()

    def edit(self, staff_id: int, model: EditStaffDto):
        try:
            staff = Staff.objects.get(id=staff_id)
            staff.user.first_name = model.first_name
            staff.user.last_name = model.last_name
            staff.user.email = model.email
            staff.staff_address = model.staff_address
            staff.staff_contact = model.staff_contact
            staff.save()
        except Staff.DoesNotExist as s:
            message = "Staff does not exist"
            print(message)
            raise s

    def list(self) -> List[ListStaffDto]:
        staff = list(Staff.objects.values("id",
                                          "user__first_name",
                                          "user__last_name",
                                          "user__email",
                                          "staff_address",
                                          "staff_contact"
                                          ))
        result: List[ListStaffDto] = []
        for s in staff:
            item = ListStaffDto()
            item.id = s["id"]
            item.first_name = s["user__first_name"]
            item.last_name = s["user__last_name"]
            item.email = s["user__email"]
            item.staff_address = s["staff_address"]
            item.staff_contact = s["staff_contact"]
            result.append(item)
        return result

    def delete(self, staff_id: int):
        try:
            staff = Staff.objects.get(id=staff_id)
            staff.delete()
        except Staff.DoesNotExist as s:
            message = "Staff info does not exist"
            print(message)
            raise s

    def get(self, staff_id: int):
        try:
            staff = Staff.objects.get(id=staff_id)
            result = StaffDetailsDto()
            result.id = staff.id
            result.first_name = staff.user.first_name
            result.last_name = staff.user.last_name
            result.email = staff.user.email
            result.staff_address = staff.staff_address
            result.staff_contact = staff.staff_contact
            return result
        except Staff.DoesNotExist as s:
            message = "Staff does not exist"
            print(message)
            raise s
