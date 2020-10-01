class CreateMealDto:
    menuitem_id: int
    customers_id: int
    status: str
    address: str
    quantity: int
    rate: float
    order_date: str
    order_time: str


class EditMealDto:
    id: int
    menuitem_id: int
    customers_id: int
    status: str
    address: str
    quantity: int
    rate: float


class ListMealDto:
    id: int
    menuitem_id: int
    customers_id: int
    status: str
    address: str
    quantity: int
    rate: float
    order_date: str
    order_time: str


class MealDetailsDto:
    id: int
    menuitem_id: int
    customers_id: int
    status: str
    address: str
    quantity: int
    rate: float
    order_date: str
    order_time: str

