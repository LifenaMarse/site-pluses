from django.urls import path
from .views import *
urlpatterns = [
    path('', returner, name='home'),
    path('demand/', demand, name='demand'),
    path('geography/', geography, name='geography'),
    path('skills/', skills, name='skills'),
    path('latest/', latest, name='latest')
]



