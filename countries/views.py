from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from . models import Country, Club
from . forms import CountryDataForm, ClubDataForm

def chartjs(request):
    data = Club.objects.all()
    new_data = ClubDataForm()
    if request.method == "POST":
        new_data = ClubDataForm(request.POST)
        if new_data.is_valid():
            new_data.save()
            return redirect('charjs_view')

    else:
        new_data = ClubDataForm()
    context = {
        'datas': data,
        'new_data': new_data
    }
    return render(request, 'club.html', context)




def home(request):
    data = Country.objects.all()
    new_data = CountryDataForm()
    if request.method == "POST":
        new_data = CountryDataForm(request.POST)
        if new_data.is_valid():
            new_data.save()
            return redirect('home_view')

    else:
        new_data = CountryDataForm()
    context = {
        'datas': data,
        'new_data': new_data
    }
    return render(request, 'home.html', context)
