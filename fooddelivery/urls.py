from django.urls import path, include
from .views import home
urlpatterns = [
    path('', include('fooddelivery.views.userLogin.urls')),
    path('customer/', include('fooddelivery.views.customer.urls')),
    path('order/', include('fooddelivery.views.order.urls')),
    path('menu/', include('fooddelivery.views.menu.urls')),
    path('menuitem/', include('fooddelivery.views.menuitem.urls')),
    path('restaurant/', include('fooddelivery.views.restaurant.urls')),
    path('staff/', include('fooddelivery.views.staff.urls')),
    path('', home.home_page, name="home"),
    path('', home.about, name="about"),
]
