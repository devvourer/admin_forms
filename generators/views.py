from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from .models import Generator, Step, Field, FieldData
from .forms import FieldDataForm, FieldForm, forms
import json


class GeneratorListView(ListView):
    model = Generator
    template_name = 'generators/index.html'


class GeneratorStepsView(ListView):
    template_name = 'generators/steps_list.html'
    queryset = Field.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        generator = get_object_or_404(Generator, slug=self.kwargs['slug'])
        context = super(GeneratorStepsView, self).get_context_data(**kwargs)
        context['steps'] = Step.objects.filter(generator=generator)
        return context

    def post(self, request, slug):
        jsin = json.dumps(request.POST)
        FieldData.objects.create(data=jsin)
        return redirect('generator:generator_list')



