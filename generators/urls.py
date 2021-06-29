from django.urls import path
from .views import GeneratorListView, GeneratorStepsView

app_name = 'generator'
urlpatterns = [
    path('', GeneratorListView.as_view(), name='generator_list'),
    path('<slug>/', GeneratorStepsView.as_view(), name='generator_steps')
]
