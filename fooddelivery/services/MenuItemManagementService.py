from abc import ABCMeta, abstractmethod
from typing import List, Dict

from fooddelivery.dto.CommonDto import SelectOptionDto
from fooddelivery.dto.MenuItemDto import CreateMenuItemDto, EditMenuItemDto, ListMenuItemDto, SearchMenuItemDto, MenuItemDetailsDto
from fooddelivery.repositories.MenuItemRepository import MenuItemRepository


class MenuItemManagementService(metaclass=ABCMeta):
    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Create a aircraft object"""
        raise NotImplementedError

    @abstractmethod
    def create(self, model: CreateMenuItemDto):
        """Creates a menuitem object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: int, model: EditMenuItemDto):
        """Updates a menuitem object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListMenuItemDto]:
        """Gets list of a menuitem"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, menuitem_id: int):
        """Deletes a menuitem"""
        raise NotImplementedError

    @abstractmethod
    def get(self, menuitem_id: int):
        """Gets a single menuitem"""
        raise NotImplementedError


class DefaultMenuItemManagementService(MenuItemManagementService):
    repository: MenuItemRepository = None

    def __init__(self, repository: MenuItemRepository):
        self.repository = repository

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def create(self, model: CreateMenuItemDto):
        return self.repository.create(model)

    def edit(self, id: int, model: EditMenuItemDto):
        return self.repository.edit(id, model)

    def list(self) -> List[ListMenuItemDto]:
        return self.repository.list()

    def delete(self, menuitem_id: int):
        return self.repository.delete(menuitem_id)

    def get(self, menuitem_id: int) -> MenuItemDetailsDto:
        return self.repository.get(menuitem_id)


