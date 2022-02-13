from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

import csv
from pagination.settings import BUS_STATION_CSV

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    stations_list = []

    # достаем данные из csv
    with open(BUS_STATION_CSV, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for station in reader:
            stations_list.append({
                "Name": station["Name"],
                "Street": station["Street"],
                "District": station["District"]
            })

    # получаем get-параметр с номером страницы и передаем их в пагинатор
    page_number = int(request.GET.get("page", 1))
    pagin_page = Paginator(stations_list, 10)
    page = pagin_page.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }

    return render(request, 'stations/index.html', context)
