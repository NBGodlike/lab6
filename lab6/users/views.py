from django.shortcuts import render
from users.Models import Course,Comment
from django.views.generic import TemplateView
from django.views import View


def index(request):
    return render(request, 'index.html')


class Courses(TemplateView):
    template_name = 'index1.html'

    def get_context_data(self, **kwargs):
        Courses = Course.objects.all()
        context = dict(Courses=Courses)
        return context


class Comments(TemplateView):
    template_name = 'index2.html'

    def get_context_data(self, **kwargs):
        Comments = Comment.objects.all()
        context = dict(Comments=Comments)
        return context
