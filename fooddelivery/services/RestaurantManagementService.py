from abc import ABCMeta, abstractmethod
from typing import List

from fooddelivery.dto.CommonDto import SelectOptionDto
from fooddelivery.dto.RestaurantDto import CreateRestaurantDto, EditRestaurantDto, ListRestaurantDto, RestaurantDetailsDto
from fooddelivery.repositories.RestaurantRepository import RestaurantRepository


class RestaurantManagementService(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Creates a customer object"""
        raise NotImplementedError

    @abstractmethod
    def create(self, model: CreateRestaurantDto):
        """Creates a restaurant object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: int, model: EditRestaurantDto):
        """Updates a restaurant object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListRestaurantDto]:
        """Gets list of restaurants"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, restaurant_id: int):
        """Deletes a restaurant"""
        raise NotImplementedError

    @abstractmethod
    def get(self, restaurant_id: int):
        """Gets a single restaurant"""
        raise NotImplementedError


class DefaultRestaurantManagementService(RestaurantManagementService):
    repository: RestaurantRepository = None

    def __init__(self, repository: RestaurantRepository):
        self.repository = repository

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def create(self, model: CreateRestaurantDto):
        return self.repository.create(model)

    def edit(self, id: int, model: EditRestaurantDto):
        return self.repository.edit(id, model)

    def list(self) -> List[ListRestaurantDto]:
        return self.repository.list()

    def delete(self, restaurant_id: int):
        return self.repository.delete(restaurant_id)

    def get(self, restaurant_id: int) -> RestaurantDetailsDto:
        return self.repository.get(restaurant_id)
