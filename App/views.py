from django.shortcuts import render, redirect
from .models import *
from .forms import *
import requests

def index(request):
    url ='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperia1&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    err_msg=''
    message=''
    message_class=''

    if request.method == 'POST':
        form=CityForm(request.POST)
        if form.is_valid():
            new_city=form.cleaned_data['name']
            existing_city_count=CityModel.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                r=requests.get(url.format(new_city)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg=' City does not in the world!'
                
            else:
                err_msg=' City already exists in the database'

        if err_msg:
            message=err_msg
            message_class='is-danger'

        else:
            message='City added succesfully!'
            message_class='is-succes'
    form=CityForm()
    weather_data=[]
    
    cities=CityModel.objects.all()
    for city in cities:
        r=requests.get(url.format(city)).json()
        city_weather={
            'city':city.name,
            'tamperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],        
                    }
        weather_data.append(city_weather)
    context={ 
        'weather_data': weather_data,
        'form':form,
        'message':message,
        'message_class':message_class
        }        

    return render(request, 'weather/weather.html', context)

def delete(request, city_name):
    CityModel.objects.get(name=city_name).delete()
    return redirect('index')



