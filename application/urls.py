from django.urls import path

from .views import initial_page

urlpatterns = [
    path('', initial_page, name='initial_page')
]

