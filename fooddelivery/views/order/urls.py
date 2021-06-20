from fooddelivery.views.order import views
from django.urls import path


urlpatterns = [
    path('', views.home_meal, name='home_meal'),
    path('create', views.create_meal, name="create_meal"),
    path('<int:meal_id>/', views.view_meal, name="view_meal"),
    path('<int:meal_id>/edit', views.edit_meal, name="edit_meal"),

]