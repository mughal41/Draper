from django.urls import path
from pages.views import Donor, home, donor_info, DonorCreate

app_name = 'pages'

urlpatterns = [
    path('confirm', donor_info, name = 'Donor_info'),
    path('donor', Donor, name = 'Donor'),
    path('', home, name= 'index' ),
    path('donor/add', DonorCreate.as_view(), name='DonorAdd'),

]