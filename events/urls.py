from django.urls import path

from .views import event_detail, event_list


urlpatterns = [
    path('list/', event_list, name='event_list'),
    path('detail/<int:pk>/', event_detail, name='event_detail'),
]
