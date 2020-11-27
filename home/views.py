from django.shortcuts import render, HttpResponse, redirect
from .models import cities
import requests
import json


# Create your views here.


def index(request):
    citiesall = cities.objects.all()
    lst = list()
    if request.method == "POST":
        cityn = request.POST.get('city')
        if cityn is None:
            return redirect("/")
        else:
            x = cities(cityname=cityn)
            x.save()
            return redirect("/")
    for city in citiesall:
        url = "http://api.weatherbit.io/v2.0/current?city=" + \
            city.cityname
        url = url + "&key=c62cdf198e1740cba1adf7c25e762517"
        response = requests.get(url)
        js = json.loads(response.text)
        # print(json.dumps(js))

        d = dict()
        d["cityname"] = city.cityname
        d["temp"] = js["data"][0]["temp"]
        d["desc"] = js["data"][0]["weather"]["description"]
        d["icon"] = js["data"][0]["weather"]["icon"]
        lst.append(d)
    context = {"var": lst}

    return render(request, 'w.html', context)
