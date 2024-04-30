from django.urls import path

from .views import teachers_list, teacher_detail

urlpatterns = [
    path('list/', teachers_list, name='teachers_list'),
    path('detail/<int:teacher_id>/', teacher_detail, name='teacher_detail')
]
