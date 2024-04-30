from django.shortcuts import render

from .models import Teacher

# Create your views here.


def teachers_list(request):
    teachers = Teacher.objects.filter(is_active=True)
    context = {
        'teachers': teachers
    }
    return render(request, 'teachers/list.html', context)


def teacher_detail(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id, is_active=True)
    context = {
        'teacher': teacher
    }
    return render(request, 'teachers/detail.html', context)
