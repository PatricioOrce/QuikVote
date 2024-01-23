from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_polls),
    path('create_poll/', views.create_poll),
    path('option/', views.get_options),
    path('option/<int:pollId>', views.get_options_by_pollId)
]