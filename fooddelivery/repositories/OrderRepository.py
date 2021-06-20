from abc import ABCMeta, abstractmethod
from typing import List

from fooddelivery.dto.CommonDto import SelectOptionDto
from fooddelivery.dto.MealDto import CreateMealDto, EditMealDto, ListMealDto, MealDetailsDto
from fooddelivery.models import Order


class MealRepository(metaclass=ABCMeta):
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


class DjangoORMnMealRepository(MealRepository):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        meals = Order.objects.values("id", "status")
        return [SelectOptionDto(meal["id"], meal["status"]) for meal in meals]

    def create(self, model: CreateMealDto):
        meal = Order()
        meal.menuitem_id = model.menuitem_id
        meal.customer_id = model.customers_id
        meal.status = model.status
        meal.address = model.address
        meal.quantity = model.quantity
        meal.rate = model.rate
        meal.order_date = model.order_date
        meal.order_time = model.order_time
        meal.save()

    def edit(self, meal_id: int, model: EditMealDto):
        try:
            meal = Order.objects.get(id=id)
            meal.menuitem_id = model.menuitem_id
            meal.customer_id = model.customers_id
            meal.status = model.status
            meal.address = model.address
            meal.quantity = model.quantity
            meal.rate = model.rate
            meal.save()
        except Order.DoesNotExist as meal:
            message = "Tried order does not exist"
            print(message)
            raise meal

    def list(self) -> List[ListMealDto]:
        meals = list(Order.objects.values("id",
                                         "menuitem_id",
                                         "customer_id",
                                         "status",
                                         "address",
                                         "quantity",
                                         "rate",
                                         "order_date",
                                         "order_time",
                                          ))
        result: List[ListMealDto] = []
        for meal in meals:
            item = ListMealDto()
            item.id = meal["id"]
            item.menuitem_id = meal["menuitem_id"]
            item.customers_id = meal["customers_id"]
            item.status = meal["status"]
            item.address = meal["address"]
            item.quantity = meal["quantity"]
            item.rate = meal["rate"]
            item.order_date = meal["order_date"]
            item.order_time = meal["order_time"]
            result.append(item)
        return result

    def delete(self, meal_id: int):
        try:
            meals = Order.objects.get(id=meal_id)
            meals.delete(meal_id)
        except Order.DoesNotExist as meal:
            message = "Tried order but does not exist"
            print(message)
            raise meal

    def get(self, meal_id: int):
        try:
            meal = Order.objects.select_related("menuitem", "customer").get(id=meal_id)
            result = MealDetailsDto()
            result.menuitem_id = meal.menuitem_id
            result.customer_id = meal.customer_id
            result.status = meal.status
            result.address = meal.address
            result.quantity = meal.quantity
            result.rate = meal.rate
            result.order_date = meal.order_date
            result.order_time = meal.order_time
            return result
        except Order.DoesNotExist as meal:
            message = "Tried order but does not exist"
            print(message)
            raise meal
