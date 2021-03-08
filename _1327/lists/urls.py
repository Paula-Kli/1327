from django.urls import path

from . import views

urlpatterns = [
	path("index", views.lists_index, name='listindex')
]
