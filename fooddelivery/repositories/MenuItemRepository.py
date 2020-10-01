from abc import ABCMeta, abstractmethod
from typing import List, Dict

from fooddelivery.dto.CommonDto import SelectOptionDto
from fooddelivery.dto.MenuItemDto import CreateMenuItemDto, EditMenuItemDto, ListMenuItemDto, SearchMenuItemDto, \
    MenuItemDetailsDto
from fooddelivery.models import MenuItem


class MenuItemRepository(metaclass=ABCMeta):
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

    @abstractmethod
    def search(self, item_name: str, item_description: str, item_price: float, other_details: str):
        """Search a menuitem"""
        raise NotImplementedError


class DjangoORMMenuItemRepository(MenuItemRepository):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        menuitem = MenuItem.objects.values("id", "menuitem_id")
        return [SelectOptionDto(e["id"], e["menuItem_id"]) for e in menuitem]

    def create(self, model: CreateMenuItemDto):
        menuitem = MenuItem()
        menuitem.menu_id = model.menu_id
        menuitem.item_name = model.item_name
        menuitem.item_description = model.item_description
        menuitem.item_price = model.item_price
        menuitem.other_details = model.other_details
        menuitem.save()

    def edit(self, id: int, model: EditMenuItemDto):
        try:
            menuitem = MenuItem.objects.get(id=_id)
            menuitem.menu_id = model.menu_id
            menuitem.item_name = model.item_name
            menuitem.item_description = model.item_description
            menuitem.item_price = model.item_price
            menuitem.other_details = model.other_details
            menuitem.save()
        except MenuItem.DoesNotExist as e:
            message = " the required menuitem does not exist"
            print(message)
            raise e

    def list(self) -> List[ListMenuItemDto]:
        menuitem = list(MenuItem.objects.values("id",
                                                "menu__menu_version",
                                                "item_name",
                                                "item_description",
                                                "item_price",
                                                "other_details"
                                                ))
        result: List[ListMenuItemDto] = []
        for e in menuitem:
            item = ListMenuItemDto()
            item.id = e["id"]
            item.item_name = e["item_name"]
            item.item_description = e["item_description"]
            item.item_price = e["item_price"]
            item.other_details = e["other_details"]
            item.menu_version = e['menu__menu_version']

            result.append(item)
        return result

    def delete(self, menuitem_id: int):
        try:
            menuitem = MenuItem.objects.get(id=menuitem_id)
            menuitem.delete()
        except MenuItem.DoesNotExist as e:
            message = "MenuItem does not exist"
            print(message)
            raise e

    def get(self, menuitem_id: int):
        try:
            menuitem = MenuItem.objects.select_related("menu").get(id=menuitem_id)
            result = MenuItemDetailsDto()
            result.id = menuitem.id
            result.menu_id = menuitem.menu_id
            result.item_name = menuitem.item_name
            result.item_description = menuitem.item_description
            result.item_price = menuitem.item_price
            result.other_details = menuitem.other_details
            return result
        except MenuItem.DoesNotExist as e:
            message = " the required menuitem does not exist"
            print(message)
            raise e

    def search(self, item_name: str, item_description: str, item_price: float, other_details: str) -> List[SearchMenuItemDto]:
        menuitem = MenuItem.objects
        if menuitem is not None:
            menuitem = menuitem.filter(item_name=item_name)
        if menuitem is not None:
            menuitem = menuitem.filter(item_description=item_description)
        if menuitem is not None:
            menuitem = menuitem.filter(item_price=item_price)
        if menuitem is not None:
            menuitem = menuitem.filter(other_details=other_details)

        menuitem = list(menuitem)
        result = []
        for e in menuitem:
            result = SearchMenuItemDto()
            result.item_name = e.item_name
            result.item_description = e.item_description
            result.item_price = e.item_price
            result.other_details = e.other_details
        return result

