from django.urls import path
from . import views

app_name = "search"
urlpatterns = [
    path("", views.index, name="index"),
    path("main/", views.search_main, name="search_main"),
    path("download/", views.selected_download, name="selected_download"),
    path("detail/<uuid:id>", views.search_detail, name="search_detail"),
]
