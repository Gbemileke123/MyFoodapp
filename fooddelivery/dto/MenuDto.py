from datetime import date

from fooddelivery.models import Restaurant


class CreateMenuDto:
    menu_version: str
    other_details: str
    date_of_creation: date
    image_url: str
    restaurant_id: int


class EditMenuDto:
    id: int
    menu_version: str
    other_details: str
    image_url: str


class ListMenuDto:
    id: int
    menu_version: str
    other_details: str
    date_of_creation: date
    image_url: str
    restaurant: Restaurant


class MenuDetailsDto:
    id: int
    menu_version: str
    other_details: str
    date_of_creation: date
    image_url: str
    restaurant: Restaurant
