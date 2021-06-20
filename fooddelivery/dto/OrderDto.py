from fooddelivery.models import MenuItem, Customer


class CreateOrderDto:
    menuitem_id: int
    customers_id: int
    status: str
    address: str
    quantity: int
    rate: float
    order_date: str
    order_time: str


class EditOrderDto:
    id: int
    menuitem_id: int
    customers_id: int
    status: str
    address: str
    quantity: int
    rate: float


class ListOrderDto:
    id: int
    menuitem: MenuItem
    customer: Customer
    status: str
    address: str
    quantity: int
    rate: float
    order_date: str
    order_time: str


class OrderDetailsDto:
    id: int
    menuitem: MenuItem
    customer: Customer
    status: str
    status: str
    address: str
    quantity: int
    rate: float
    order_date: str
    order_time: str

