from django.shortcuts import render,redirect
from django.http import JsonResponse
import requests
from datetime import datetime


agora = datetime.now()
hora_atual = agora.hour

# Create your views here.
def tempo_hoje_lisboa(request):
    url_lisboa = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    response = requests.get(url_lisboa)
    data = response.json()

    weather_today = data['data'][0]
    city = 'Lisboa'
    min_temp = weather_today['tMin']
    max_temp = weather_today['tMax']
    weather_type_id = weather_today['idWeatherType']
    date = weather_today['forecastDate']

    weather_desc_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'
    response = requests.get(weather_desc_url)
    weather_desc_data = response.json()['data']
    weather_desc = next(item for item in weather_desc_data if item["idWeatherType"] == weather_type_id)['descWeatherTypePT']

    if(weather_type_id < 10):
        if 7 <= hora_atual <= 18:
            icon_url = f"/static/meteo/w_ic_d_0{weather_type_id}.svg"
        else:
            icon_url = f"/static/meteo/w_ic_n_0{weather_type_id}.svg"
    else:
        if 7 <= hora_atual <= 18:
            icon_url = f"/static/meteo/w_ic_d_{weather_type_id}.svg"
        else:
            icon_url = f"/static/meteo/w_ic_n_{weather_type_id}.svg"

    context = {
        'city': city,
        'min_temp': min_temp,
        'max_temp': max_temp,
        'date': date,
        'weather_desc': weather_desc,
        'icon_url': icon_url,
    }

    return render(request, 'meteo/tempo_hoje_lisboa.html', context)

def tempo_hoje_cidade(request, city_id):
    url_cidade = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    response = requests.get(url_cidade)
    data = response.json()


    weather_today = data['data'][0]
    city = f'City ID: {city_id}'
    min_temp = weather_today["tMin"]
    max_temp = weather_today["tMax"]
    weather_type_id = weather_today["idWeatherType"]
    date = weather_today["forecastDate"]

    weather_desc_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'
    response = requests.get(weather_desc_url)


    weather_desc_data = response.json()['data']
    weather_desc = next((item for item in weather_desc_data if item["idWeatherType"] == weather_type_id), None)


    weather_desc = weather_desc['descWeatherTypePT']

    if(weather_type_id < 10):
        if 7 <= hora_atual <= 18:
            icon_url = f"/static/meteo/w_ic_d_0{weather_type_id}.svg"
        else:
            icon_url = f"/static/meteo/w_ic_n_0{weather_type_id}.svg"
    else:
        if 7 <= hora_atual <= 18:
            icon_url = f"/static/meteo/w_ic_d_{weather_type_id}.svg"
        else:
            icon_url = f"/static/meteo/w_ic_n_{weather_type_id}.svg"


    context = {
        'city': city,
        'min_temp': min_temp,
        'max_temp': max_temp,
        'date': date,
        'weather_desc': weather_desc,
        'icon_url': icon_url,
    }

    return render(request, 'meteo/tempo_hoje_cidade.html', context)





def cidades(request):
    url_cidades = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(url_cidades)
    data = response.json()

    cities = data['data']

    if 'city_id' in request.GET:
        city_id = request.GET['city_id']
        return redirect('meteo:tempo_hoje_cidade', city_id=city_id)

    context = {
        'cities': cities,
    }

    return render(request, 'meteo/cidades.html', context)


def previsao_cinco_dias(request, city_id):
    url_cidade = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    response = requests.get(url_cidade)
    data = response.json()

    weather_data = data['data'][:5]

    for i, day in enumerate(weather_data):
        weather_type_id = day["idWeatherType"]
        if i == 0:
            if weather_type_id < 10:
                if 7 <= hora_atual <= 18:
                    day['icon_url'] = f"/static/meteo/w_ic_d_0{weather_type_id}.svg"
                else:
                    day['icon_url'] = f"/static/meteo/w_ic_n_0{weather_type_id}.svg"
            else:
                if 7 <= hora_atual <= 18:
                    day['icon_url'] = f"/static/meteo/w_ic_d_{weather_type_id}.svg"
                else:
                    day['icon_url'] = f"/static/meteo/w_ic_n_{weather_type_id}.svg"
        else:
            if weather_type_id < 10:
                day['icon_url'] = f"/static/meteo/w_ic_d_0{weather_type_id}.svg"
            else:
                day['icon_url'] = f"/static/meteo/w_ic_d_{weather_type_id}.svg"

    context = {
        'weather_data': weather_data
    }

    return render(request, 'meteo/previsao_cinco_dias.html', context)




def api_lista_cidades(request):
    url_cidades = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(url_cidades)
    data = response.json()
    return JsonResponse(data)

def api_previsao_hoje(request, city_id):
    url_cidade = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    response = requests.get(url_cidade)
    data = response.json()
    return JsonResponse(data['data'][0])

def api_previsao_cinco_dias(request, city_id):
    url_cidade = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    response = requests.get(url_cidade)
    data = response.json()
    return JsonResponse(data['data'][:5], safe=False)