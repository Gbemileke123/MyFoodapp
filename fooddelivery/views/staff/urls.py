from fooddelivery.views.staff import views
from django.urls import path


urlpatterns = [
    path('homes/', views.staff_homepage, name='staff_homepage'),
    path('', views.home_staff, name='home_staff'),
    path('create', views.create_staff, name="create_staff"),
    path('<int:staff_id>/view', views.view_staff, name="view_staff"),
    path('<int:staff_id>/edit', views.edit_staff, name="edit_staff"),
    path('<int:staff_id>/delete', views.delete_staff, name="delete_staff"),

]