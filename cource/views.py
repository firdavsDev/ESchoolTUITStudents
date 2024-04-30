from django.shortcuts import render

from .models import Course


def courses_list(request):
    courses = Course.objects.filter(is_active=True)
    context = {
        'courses': courses
    }
    return render(request, 'courses/list.html', context)


def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id, is_active=True)
    context = {
        'course': course
    }
    return render(request, 'courses/detail.html', context)
