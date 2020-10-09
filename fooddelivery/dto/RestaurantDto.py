class CreateRestaurantDto:
    username: str
    password: str
    name: str
    email: str
    restaurant_address: str
    restaurant_contact: str
    food_description: str


class EditRestaurantDto:
    id: int
    name: str
    email: str
    owner_id: str
    restaurant_address: str
    restaurant_contact: str
    food_description: str


class ListRestaurantDto:
    id: int
    name: str
    email: str
    owner_id: str
    restaurant_address: str
    restaurant_contact: str


class RestaurantDetailsDto:
    id: int
    name: str
    email: str
    owner_id: str
    restaurant_address: str
    restaurant_contact: str
    food_description: str
