from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home_view"),
    path('chartjs/', views.chartjs, name="charjs_view")

]
