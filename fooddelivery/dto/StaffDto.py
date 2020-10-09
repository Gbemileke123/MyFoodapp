class CreateStaffDto:
    username: str
    first_name: str
    last_name: str
    password: str
    email: str
    staff_address: str
    staff_contact: str


class EditStaffDto:
    id: int
    first_name: str
    last_name: str
    email: str
    staff_address: str
    staff_contact: str


class ListStaffDto:
    id: int
    first_name: str
    last_name: str
    email: str
    staff_address: str
    staff_contact: str


class StaffDetailsDto:
    id: int
    first_name: str
    last_name: str
    email: str
    staff_address: str
    staff_contact: str