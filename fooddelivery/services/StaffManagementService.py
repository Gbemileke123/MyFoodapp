from abc import ABCMeta, abstractmethod
from typing import List

from fooddelivery.dto.StaffDto import CreateStaffDto, EditStaffDto, ListStaffDto, StaffDetailsDto
from fooddelivery.repositories.StaffRepository import StaffRepository


class StaffManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create(self, model: CreateStaffDto):
        """Create a customer object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: int, model: EditStaffDto):
        """Update customer object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListStaffDto]:
        """Gets list of customers"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, staff_id: int):
        """Deletes a staff object"""

    @abstractmethod
    def get(self, staff_id: int):
        """Gets a single customer"""
        raise NotImplementedError


class DefaultStaffManagementService(StaffManagementService):
    repository: StaffRepository = None

    def __init__(self, repository: StaffRepository):
        self.repository = repository

    def create(self, model: CreateStaffDto):
        return self.repository.create(model)

    def edit(self, id: int, model: EditStaffDto):
        return self.repository.edit(id, model)

    def list(self) -> List[ListStaffDto]:
        return self.repository.list()

    def delete(self, staff_id: int):
        return self.repository.delete(staff_id)

    def get(self, staff_id: int) -> StaffDetailsDto:
        return self.repository.get(staff_id)