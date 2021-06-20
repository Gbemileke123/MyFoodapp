from abc import ABCMeta, abstractmethod
from typing import List

from fooddelivery.dto.CommonDto import SelectOptionDto
from fooddelivery.dto.OrderDto import CreateOrderDto, EditOrderDto, ListOrderDto, OrderDetailsDto
from fooddelivery.repositories.OrderRepository import OrderRepository


class OrderManagementService(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Create an order object"""
        raise NotImplementedError

    @abstractmethod
    def create(self, model: CreateOrderDto):
        """Create a order object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: int, model: EditOrderDto):
        """Updates a order object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListOrderDto]:
        """Gets list of order"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, order_id: int):
        """Deletes a order"""

    @abstractmethod
    def get(self, order_id: int):
        """Gets a single order"""
        raise NotImplementedError


class DefaultMealManagementService(OrderManagementService):
    repository: OrderRepository = None

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def create(self, model: CreateOrderDto):
        return self.repository.create(model)

    def edit(self, id: int, model: EditOrderDto):
        return self.repository.edit(id, model)

    def list(self) -> List[ListOrderDto]:
        return self.repository.list()

    def delete(self, meal_id: int):
        return self.repository.delete(meal_id)

    def get(self, meal_id: int) -> OrderDetailsDto:
        return  self.repository.get(meal_id)
