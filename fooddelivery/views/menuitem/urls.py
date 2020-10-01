from fooddelivery.views.menuitem import views
from django.urls import path


urlpatterns = [
    path('', views.home_menuitem, name='home_menuitem'),
    path('create', views.create_menuitem, name="create_menuitem"),
    path('<int:menuitem_id>/view', views.view_menuitem, name="view_menuitem"),
    path('<int:menuitem_id>/edit', views.edit_menuitem, name="edit_menuitem"),
    path('<int:menuitem_id>/delete', views.delete_menuitem, name="delete_menuitem"),
    path('<int:menuitem_id>/search', views.search_menuitem, name="search_menuitem"),

]