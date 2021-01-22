from django.shortcuts import render
import requests

from .models import City
from .forms import CityForm


def initial_page(request):
    """ Представление первоначальной страницы """
    app_id = '162b96b3defebbf60cd419a77ba9f339'
    forms = CityForm()
    error_add = False
    error_delete = False

    # url = 'https://api.openweathermap.org/data/2.5/weather?q={city name}&units=metric&appid={API key}'
    # units=metric : Измерение температуры в градумах.
    # q: Название города.
    # appid: Ключ API https://home.openweathermap.org/

    cities = City.objects.all()
    weather_cities = []
    for city in cities:
        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city.title}&units=metric&appid={app_id}'
        ).json()
        if response['cod'] == 200:
            # cod 200 - OK; cod 404 - NOT
            weather_city = {
                'city': city.title,
                'temp': response['main']['temp'],
                'icon': response['weather'][0]['icon'],
            }
            weather_cities.append(weather_city)

    if request.method == 'POST':
        if request.POST.get('add'):
            forms = CityForm(request.POST)
            if forms.is_valid():
                form_post = forms.save(commit=False)
                city = forms.cleaned_data['title']
                response = requests.get(
                    f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={app_id}'
                ).json()
                if response['cod'] == 200:
                    form_post.title = city
                    form_post.save()
                    forms = CityForm()
                else:
                    error_add = 'City not found'

        if request.POST.get('delete'):
            if request.POST.get('delete_city_title'):
                delete_city_title = request.POST['delete_city_title']
                city_delete = City.objects.filter(title=delete_city_title)
                if city_delete:
                    city_delete.delete()

    context = {'forms': forms, 'cities': weather_cities, 'error_add': error_add, 'error_delete': error_delete}

    return render(request, 'application/initial_page.html', context)
