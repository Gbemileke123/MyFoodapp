from abc import ABCMeta, abstractmethod
from typing import List

from fooddelivery.dto.CommonDto import SelectOptionDto
from fooddelivery.dto.MenuDto import CreateMenuDto, EditMenuDto, ListMenuDto, MenuDetailsDto
from fooddelivery.repositories.MenuRepository import MenuRepository


class MenuManagementService(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Creates a menu object"""
        raise NotImplementedError

    @abstractmethod
    def create(self, model: CreateMenuDto):
        """Creates a menu object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: int, model: EditMenuDto):
        """Updates menu object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListMenuDto]:
        """Gets list of a menu"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, menu_id: int):
        """Deletes a menu object"""
        raise NotImplementedError

    @abstractmethod
    def get(self, menu_id: int):
        """Gets a single menu"""
        raise NotImplementedError


class DefaultMenuManagementService(MenuManagementService):
    repository: MenuRepository = None

    def __init__(self, repository: MenuRepository):
        self.repository = repository

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def create(self, model: CreateMenuDto):
        return self.repository.create(model)

    def edit(self, id: int, model: EditMenuDto):
        return self.repository.edit(id, model)

    def list(self) -> List[ListMenuDto]:
        return self.repository.list()

    def delete(self, menu_id: int):
        return self.repository.delete(menu_id)

    def get(self, menu_id: int) -> MenuDetailsDto:
        return self.repository.get(menu_id)
