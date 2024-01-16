from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_polls),
    path('option/', views.get_options),
    path('option/<int:pollId>', views.get_options_by_pollId)
]