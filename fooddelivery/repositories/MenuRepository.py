from abc import ABCMeta, abstractmethod
from typing import List

from fooddelivery.dto.CommonDto import SelectOptionDto
from fooddelivery.dto.MenuDto import CreateMenuDto, EditMenuDto, ListMenuDto, MenuDetailsDto
from fooddelivery.models import Menu


class MenuRepository(metaclass=ABCMeta):
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


class DjangoORMMenuRepository(MenuRepository):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        menu = Menu.objects.values("id", "menu_version")
        return [SelectOptionDto(m["id"], m["menu_version"]) for m in menu]

    def create(self, model: CreateMenuDto):
        menu = Menu()
        menu.menu_version = model.menu_version
        menu.other_details = model.other_details
        menu.date_of_creation = model.date_of_creation
        menu.image_url = model.image_url
        menu.save()

    def edit(self, menu_id: int, model: EditMenuDto):
        try:
            menu = Menu.objects.get(id=menu_id)
            menu.menu_version = model.menu_version
            menu.other_details = model.other_details
            menu.image_url = model.image_url
            menu.save()

        except Menu.DoesNotExist as m:
            message = " Menu information does not exist"
            print(message)
            raise m

    def list(self) -> List[ListMenuDto]:
        menu = list(Menu.objects.values("id",
                                        "menu_version",
                                        "other_details",
                                        "date_of_creation",
                                        "image_url",
        ))
        result: List[ListMenuDto] = []
        for m in menu:
            item = ListMenuDto()
            item.id = m["id"]
            item.menu_version = m["menu_version"]
            item.other_details = m["other_details"]
            item.date_of_creation = m["date_of_creation"]
            item.image_url = m['image_url']
            result.append(item)
        return result

    def delete(self, menu_id: int):
        try:
            menu = Menu.objects.get(id=menu_id)
            menu.delete()
        except Menu.DoesNotExist as m:
            message = " Menu information does not exist"
            print(message)
            raise m

    def get(self, menu_id: int):
        try:
            menu = Menu.objects.get(id=menu_id)
            result = MenuDetailsDto()
            result.id = menu.id
            result.menu_version = menu.menu_version
            result.other_details = menu.other_details
            result.date_of_creation = menu.date_of_creation
            return result
        except Menu.DoesNotExist as m:
            message = " Menu information does not exist"
            print(message)
            raise m
