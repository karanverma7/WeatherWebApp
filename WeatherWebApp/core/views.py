from django.shortcuts import render
import requests


def index(request):

    if request.POST:
        city = request.POST['city']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7f58fb81d202f06c8b815b95b72d4473'
        r = requests.get(url.format(city)).json()
        temp_in_celcius = "{:.2f}".format((r['main']['temp'] - 32) * 5/9)

        city_weather = {
            'name': r['name'],
            'country': r['sys']['country'],
            'temp': temp_in_celcius,
            'humidity': r['main']['humidity'],
            'pressure': r['main']['pressure'],
            'wind': r['wind']['speed'],
            'description': r['weather'][0]['main'],
            'icon': r['weather'][0]['icon']
        }

        img_url = 'https://api.unsplash.com/search/photos?per_page=1&query={}&client_id=jKdZP3hygPsn8nZa0u26Kqkq59BhjQGDconnica895c'
        r2 = requests.get(img_url.format(city)).json()
        img_src = r2['results'][0]['urls']['thumb']

        return render(request, 'index.html', {'city_weather': city_weather, 'img_src': img_src})
    else:
        return render(request, 'index.html')