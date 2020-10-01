from datetime import date


class CreateMenuDto:
    menu_version: str
    other_details: str
    date_of_creation: date
    image_url: str


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


class MenuDetailsDto:
    id: int
    menu_version: str
    other_details: str
    date_of_creation: date
    image_url: str
