class CreateCustomersDto:
    username: str
    user_first_name: str
    user_last_name: str
    password: str
    email: str
    address: str
    contact: str


class EditCustomersDto:
    id: int
    user_first_name: str
    user_last_name: str
    email: str
    address: str
    contact: str


class ListCustomersDto:
    id: int
    user_first_name: str
    user_last_name: str
    email: str
    address: str
    contact: str


class CustomersDetailsDto:
    id: int
    user_first_name: str
    user_last_name: str
    email: str
    address: str
    contact: str


