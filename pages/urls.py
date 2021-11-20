from django.urls import path
from pages.views import *

app_name = 'pages'

urlpatterns = [
    path("request_blood/", request, name="request_blood"),
    path("all_request/", all_request, name="all_request"),
    path("donor/", be_a_donor, name="become_donor"),
    path('', home, name= 'index' ),
    path("login/", Login, name="login"),
    path("donors_list/<int:myid>/", donors_list, name="donors_list"),
    path('profile/', profile, name='profile'),
    path('edit_profile/',edit_profile, name='edit_profile'),

    

]