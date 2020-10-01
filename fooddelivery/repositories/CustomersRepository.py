from abc import ABCMeta, abstractmethod
from typing import List

from django.contrib.auth.models import User, Group
from fooddelivery.dto.CommonDto import SelectOptionDto
from fooddelivery.dto.CustomersDto import CreateCustomersDto, EditCustomersDto, ListCustomersDto, CustomersDetailsDto
from fooddelivery.models import Customer


class CustomersRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Create an order object"""
        raise NotImplementedError

    @abstractmethod
    def create(self, model: CreateCustomersDto):
        """Create a customer object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: int, model: EditCustomersDto):
        """Update customer object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListCustomersDto]:
        """Gets list of customers"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, customer_id: int):
        """Deletes a customer"""
        raise NotImplementedError

    @abstractmethod
    def get(self, customer_id: int):
        """Gets a single customer"""
        raise NotImplementedError


class DjangoORMCustomersRepository(CustomersRepository):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        customer = Customer.objects.values("id", "user__last_name")
        return [SelectOptionDto(c["id"], c["last_name"]) for c in customer]

    def create(self, model: CreateCustomersDto):
        customer = Customer()
        customer.address = model.address
        customer.contact = model.contact

        # create the user
        user = User.objects.create_user(model.username, model.email, model.password)
        user.user_first_name = model.user_first_name
        user.user_last_name = model.user_last_name
        user.save()

        customer.user = user
        customers = Group.objects.get(name='Customer')
        user.groups.add(customers)

        customer.save()

    def edit(self, customer_id: int, model: EditCustomersDto):
        try:
            customer = Customer.objects.get(id=customer_id)
            customer.user_first_name = model.user_first_name
            customer.user_last_name = model.user_last_name
            customer.email = model.email
            customer.address = model.address
            customer.contact = model.contact
            customer.save()
        except Customer.DoesNotExist as c:
            message = "Customer does not exist"
            print(message)
            raise c

    def list(self) -> List[ListCustomersDto]:
        customer = list(Customer.objects.values("id",
                                                "user__first_name",
                                                "user__last_name",
                                                "user__email",
                                                "address",
                                                "contact"))
        result: List[ListCustomersDto] = []
        for c in customer:
            item = ListCustomersDto()
            item.id = c["id"]
            item.user_first_name = c["user__first_name"]
            item.user_last_name = c["user__last_name"]
            item.user_email = c["user__email"]
            item.address = c["address"]
            item.contact = c["contact"]
            result.append(item)
        return result

    def delete(self, customer_id: int):
        try:
            customer = Customer.objects.get(id=customer_id)
            customer.delete()
        except Customer.DoesNotExist as c:
            message = "Customer information does not exist"
            print(message)
            raise c

    def get(self, customer_id: int):
        try:
            customer = Customer.objects.get(id=customer_id)
            result = CustomersDetailsDto()
            result.id = customer.id
            result.user_first_name = customer.user.first_name
            result.user_last_name = customer.user.last_name
            result.user_email = customer.user.email
            result.address = customer.address
            result.contact = customer.contact
            return result
        except Customer.DoesNotExist as c:
            message = "Customers does not exist"
            print(message)
            raise c
