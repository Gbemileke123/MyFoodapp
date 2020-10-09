from abc import ABCMeta, abstractmethod
from typing import List

from fooddelivery.dto.CommonDto import SelectOptionDto
from fooddelivery.dto.MealDto import CreateMealDto, EditMealDto, ListMealDto, MealDetailsDto
from fooddelivery.repositories.MealRepository import MealRepository


class MealManagementService(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Create an order object"""
        raise NotImplementedError

    @abstractmethod
    def create(self, model: CreateMealDto):
        """Create a order object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: int, model: EditMealDto):
        """Updates a order object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListMealDto]:
        """Gets list of order"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, meal_id: int):
        """Deletes a order"""

    @abstractmethod
    def get(self, meal_id: int):
        """Gets a single order"""
        raise NotImplementedError


class DefaultMealManagementService(MealManagementService):
    repository: MealRepository = None

    def __init__(self, repository: MealRepository):
        self.repository = repository

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def create(self, model: CreateMealDto):
        return self.repository.create(model)

    def edit(self, id: int, model: EditMealDto):
        return self.repository.edit(id, model)

    def list(self) -> List[ListMealDto]:
        return self.repository.list()

    def delete(self, meal_id: int):
        return self.repository.delete(meal_id)

    def get(self, meal_id: int) -> MealDetailsDto:
        return  self.repository.get(meal_id)
