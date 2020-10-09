from fooddelivery.views.menu import views
from django.urls import path


urlpatterns = [
    path('', views.home_menu, name='home_menu'),
    path('create', views.create_menu, name="create_menu"),
    path('<int:menu_id>/view', views.view_menu, name="view_menu"),
    path('<int:menu_id>/edit', views.edit_menu, name="edit_menu"),
    path('<int:menu_id>/delete', views.delete_menu, name="delete_menu")

]