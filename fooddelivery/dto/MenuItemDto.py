class CreateMenuItemDto:
    menu_id: int
    item_name: str
    item_description: str
    item_price: float
    other_details: str
    image_url: str


class EditMenuItemDto:
    id: int
    menu_id: int
    item_name: str
    item_description: str
    item_price: float
    other_details: str
    image_url: str


class ListMenuItemDto:
    id: int
    menu_version: str
    item_name: str
    item_description: str
    item_price: float
    other_details: str
    image_url: str


class MenuItemDetailsDto:
    id: int
    menu_id: int
    item_name: str
    item_description: str
    item_price: float
    other_details: str
    image_url: str


class SearchMenuItemDto:
    id: int
    menu_id: int
    item_name: str
    item_description: str
    item_price: float
    other_details: str

