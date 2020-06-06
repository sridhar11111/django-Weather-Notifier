import requests
from django.shortcuts import render
from .models import City
from .forms import Cityform
from win10toast import ToastNotifier
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=e13c79776fccd7a279c86d4f10ff7084'
    cities_in_data = City.objects.all()
    weather_data = []

    if request.method == 'POST':
        form = Cityform(request.POST)
        form.save()
    form = Cityform

    # toast = ToastNotifier()
    # a = cities_in_data[len(cities_in_data)-1]
    # aa = requests.get(url.format(a)).json()
    # Noti = " It's " + aa['weather'][0]['description'] + "Today "
    # body = ""
    # if aa['weather'][0]['description'] == "Haze":
    #     body = body + "It may Rain Today !!"
    # elif aa['weather'][0]['description'] == "clear sky":
    #     body = body + "You Can Go out its clear"
    # elif aa['weather'][0]['description'] == "light rain":
    #     body = body + "Light Rain Today . . "
    # toast.show_toast(Noti, body, duration=20)

    for city in cities_in_data:
        tt = requests.get(url.format(city)).json()
        city_weather = {
            'mint': tt['main']['temp_min'],
            'maxt': tt['main']['temp_max'],
            'wind': tt['wind']['speed'],
            'city': tt['name'],
            'temperature': tt['main']['temp'],
            'description': tt['weather'][0]['description'],
            'icon': tt['weather'][0]['icon'],

        }
        weather_data.append(city_weather)
    # print(city_weather)
    weather_data.reverse()
    context = {'weather_data': weather_data ,'form' : form}
    return render(request, 'weather/weather.html', context)
