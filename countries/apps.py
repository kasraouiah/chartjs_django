from django.apps import AppConfig


class CountriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'countries'

class ClubConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name= 'Clubs'
