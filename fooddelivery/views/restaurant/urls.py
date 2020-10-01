from fooddelivery.views.restaurant import views
from django.urls import path


urlpatterns = [
    path('homes/', views.restaurant_homepage, name='restaurant_homepage'),
    path('', views.home_restaurant, name='home_restaurant'),
    path('create', views.create_restaurant, name="create_restaurant"),
    path('<int:restaurant_id>/view', views.view_restaurant, name="view_restaurant"),
    path('<int:restaurant_id>/edit', views.edit_restaurant, name="edit_restaurant"),
    path('<int:restaurant_id>/delete', views.delete_restaurant, name="delete_restaurant"),
]