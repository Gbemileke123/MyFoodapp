from abc import ABCMeta, abstractmethod
from typing import List

from fooddelivery.dto.CommonDto import SelectOptionDto
from fooddelivery.dto.CustomersDto import CreateCustomersDto, EditCustomersDto, ListCustomersDto, CustomersDetailsDto
from fooddelivery.repositories.CustomersRepository import CustomersRepository


class CustomerManagementService(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[ListCustomersDto]:
        """Creates a customer object"""
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
    def get(self, customers_id: int):
        """Gets a single customer"""
        raise NotImplementedError


class DefaultCustomerManagementService(CustomerManagementService):
    repository: CustomersRepository = None

    def __init__(self, repository: CustomersRepository):
        self.repository = repository

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def create(self, model: CreateCustomersDto):
        return self.repository.create(model)

    def edit(self, id: int, model: EditCustomersDto):
        return self.repository.edit(id, model)

    def list(self) -> List[ListCustomersDto]:
        return self.repository.list()

    def get(self, customer_id: int) -> CustomersDetailsDto:
        return self.repository.get(customer_id)