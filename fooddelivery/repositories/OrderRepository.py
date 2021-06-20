from abc import ABCMeta, abstractmethod
from typing import List

from fooddelivery.dto.CommonDto import SelectOptionDto
from fooddelivery.dto.OrderDto import CreateOrderDto, EditOrderDto, ListOrderDto, OrderDetailsDto
from fooddelivery.models import Order


class OrderRepository(metaclass=ABCMeta):
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

    # @abstractmethod
    # def delete(self, order_id: int):
    #     """Deletes a order""" #TODO May need to optimize later

    @abstractmethod
    def get(self, meal_id: int):
        """Gets a single order"""
        raise NotImplementedError


class DjangoORMnOrderRepository(OrderRepository):
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        orders = Order.objects.values("id", "status")
        return [SelectOptionDto(order["id"], order["status"]) for order in orders]

    def create(self, model: CreateOrderDto):
        order = Order()
        order.menuitem_id = model.menuitem_id
        order.customer_id = model.customers_id
        order.status = model.status
        order.address = model.address
        order.quantity = model.quantity
        order.rate = model.rate
        order.order_date = model.order_date
        order.order_time = model.order_time
        order.save()

    def edit(self, meal_id: int, model: EditOrderDto):
        try:
            order = Order.objects.get(id=id)
            order.menuitem_id = model.menuitem_id
            order.customer_id = model.customers_id
            order.status = model.status
            order.address = model.address
            order.quantity = model.quantity
            order.rate = model.rate
            order.save()
        except Order.DoesNotExist as order:
            message = "Tried order does not exist"
            print(message)
            raise order

    def list(self) -> List[ListOrderDto]:
        orders = list(Order.objects.values("id",
                                           "menuitem",
                                           "customer",
                                           "status",
                                           "address",
                                           "quantity",
                                           "rate",
                                           "order_date",
                                           "order_time",
                                           ))
        result: List[ListOrderDto] = []
        for order in orders:
            item = ListOrderDto()
            item.id = order["id"]
            item.menuitem = order["menuitem"]
            item.customers = order["customers"]
            item.status = order["status"]
            item.address = order["address"]
            item.quantity = order["quantity"]
            item.rate = order["rate"]
            item.order_date = order["order_date"]
            item.order_time = order["order_time"]
            result.append(item)
        return result

    # def delete(self, order_id: int):
    #     try:
    #         meals = Order.objects.get(id=order_id)
    #         meals.delete(order_id)
    #     except Order.DoesNotExist as meal:
    #         message = "Tried order but does not exist"
    #         print(message)
    #         raise meal #TODO May need to optimize later

    def get(self, order_id: int):
        try:
            order = Order.objects.select_related("menuitem", "customer").get(id=order_id)
            result = OrderDetailsDto()
            result.menuitem_ = order.menuitem
            result.customer = order.customer
            result.status = order.status
            result.address = order.address
            result.quantity = order.quantity
            result.rate = order.rate
            result.order_date = order.order_date
            result.order_time = order.order_time
            return result
        except Order.DoesNotExist as order:
            message = "Tried order but does not exist"
            print(message)
            raise order
