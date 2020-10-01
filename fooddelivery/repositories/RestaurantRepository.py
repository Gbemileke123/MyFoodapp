from abc import ABCMeta, abstractmethod
from typing import List

from django.contrib.auth.models import User, Group
from fooddelivery.dto.CommonDto import SelectOptionDto
from fooddelivery.dto.RestaurantDto import CreateRestaurantDto, EditRestaurantDto, ListRestaurantDto, \
    RestaurantDetailsDto
from fooddelivery.models import Restaurant


class RestaurantRepository(metaclass=ABCMeta):
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


class DjangoORMRestaurantRepository(RestaurantRepository):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        restaurant = Restaurant.objects.values("id", "name")
        return [SelectOptionDto(r["id"], r["name"]) for r in restaurant]

    def create(self, model: CreateRestaurantDto):
        restaurant = Restaurant()
        restaurant.name = model.name
        restaurant.email = model.email
        restaurant.restaurant_address = model.restaurant_address
        restaurant.restaurant_contact = model.restaurant_contact
        restaurant.food_description = model.food_description

        owner = User.objects.create_user(model.username, model.email, model.password)

        restaurant.owner = owner
        rest = Group.objects.get(name='Restaurant')
        owner.groups.add(rest)

        restaurant.save()

    def edit(self, id: int, model: EditRestaurantDto):
        try:
            restaurant = Restaurant.objects.get(id=id)
            restaurant.restaurant_address = model.restaurant_address
            restaurant.restaurant_contact = model.restaurant_contact
            restaurant.food_description = model.food_description
            restaurant.save()
        except Restaurant.DoesNotExist as r:
            message = "Restaurant does not exist"
            print(message)
            raise r

    def list(self) -> List[ListRestaurantDto]:
        restaurant = list(Restaurant.objects.values("id",
                                                    "name",
                                                    "email",
                                                    "owner_id",
                                                    "restaurant_address",
                                                    "restaurant_contact",
                                                    "food_description",
                                                    ))
        result: List[ListRestaurantDto] = []
        for r in restaurant:
            item = ListRestaurantDto()
            item.id = r["id"]
            item.name = r["name"]
            item.email = r["email"]
            item.restaurant_address = r["restaurant_address"]
            item.restaurant_contact = r["restaurant_contact"]
            item.food_description = r["food_description"]
            result.append(item)
        return result

    def delete(self, restaurant_id: int):
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
            restaurant.delete()
        except Restaurant.DoesNotExist as r:
            message = "Restaurant does not exist"
            print(message)
            raise r

    def get(self, restaurant_id: int):
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
            result = RestaurantDetailsDto()
            result.id = restaurant.id
            result.name = restaurant.name
            result.email = restaurant.email
            result.owner_id = restaurant.owner_id
            result.restaurant_address = restaurant.restaurant_address
            result.restaurant_contact = restaurant.restaurant_contact
            result.food_description = restaurant.food_description
            return result
        except Restaurant.DoesNotExist as r:
            message = "Restaurant does not exist"
            print(message)
            raise r

