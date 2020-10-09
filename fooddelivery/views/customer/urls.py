from fooddelivery.views.customer import views
from django.urls import path


urlpatterns = [
    path('', views.home_customer, name='home_customer'),
    path('create', views.create_customer, name="create_customer"),
    path('<int:customer_id>/', views.view_customer, name="view_customer"),
    path('<int:customer_id>/edit', views.edit_customer, name="edit_customer"),
    path('<int:customer_id>/delete', views.delete_customer, name="delete_customer"),

]