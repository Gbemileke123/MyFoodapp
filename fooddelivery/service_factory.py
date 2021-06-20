from dependency_injector import containers, providers

from fooddelivery.repositories.CustomersRepository import CustomersRepository, DjangoORMCustomersRepository
from fooddelivery.repositories.OrderRepository import OrderRepository, DjangoORMnOrderRepository
from fooddelivery.repositories.MenuRepository import MenuRepository, DjangoORMMenuRepository
from fooddelivery.repositories.MenuItemRepository import MenuItemRepository, DjangoORMMenuItemRepository
from fooddelivery.repositories.RestaurantRepository import RestaurantRepository, DjangoORMRestaurantRepository
from fooddelivery.repositories.StaffRepository import StaffRepository, DjangoORMStaffRepository
from fooddelivery.services.CustomerManagementService import DefaultCustomerManagementService, CustomerManagementService
from fooddelivery.services.OrderManagementService import DefaultMealManagementService, OrderManagementService
from fooddelivery.services.MenuManagementService import DefaultMenuManagementService, MenuManagementService
from fooddelivery.services.MenuItemManagementService import DefaultMenuItemManagementService, MenuItemManagementService
from fooddelivery.services.RestaurantManagementService import DefaultRestaurantManagementService, \
    RestaurantManagementService
from fooddelivery.services.StaffManagementService import DefaultStaffManagementService, StaffManagementService
from typing import Callable


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    customer_repository: Callable[[], CustomersRepository] = providers.Factory(
        DjangoORMCustomersRepository
    )

    meal_repository: Callable[[], OrderRepository] = providers.Factory(
        DjangoORMnOrderRepository
    )

    menuitem_repository: Callable[[], MenuItemRepository] = providers.Factory(
        DjangoORMMenuItemRepository
    )

    menu_repository: Callable[[], MenuRepository] = providers.Factory(
        DjangoORMMenuRepository
    )

    restaurant_repository: Callable[[], RestaurantRepository] = providers.Factory(
        DjangoORMRestaurantRepository
    )

    staff_repository: Callable[[], StaffRepository] = providers.Factory(
        DjangoORMStaffRepository
    )

    customer_management_service: Callable[[], CustomerManagementService] = providers.Factory(
        DefaultCustomerManagementService,
        repository=customer_repository
    )

    meal_management_service: Callable[[], OrderManagementService] = providers.Factory(
        DefaultMealManagementService,
        repository=meal_repository
    )

    menuitem_management_service: Callable[[], MenuItemManagementService] = providers.Factory(
        DefaultMenuItemManagementService,
        repository=menuitem_repository
    )

    menu_management_service: Callable[[], MenuManagementService] = providers.Factory(
        DefaultMenuManagementService,
        repository=menu_repository
    )

    restaurant_management_service: Callable[[], RestaurantManagementService] = providers.Factory(
        DefaultRestaurantManagementService,
        repository=restaurant_repository
    )

    staff_management_service: Callable[[], StaffManagementService] = providers.Factory(
        DefaultStaffManagementService,
        repository=staff_repository
    )


fooddelivery_service_container = Container()