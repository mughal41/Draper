from django.shortcuts import render, redirect
from django.views import generic
from pages.models import Donorinfo, Postform
from django.views.generic.edit import CreateView
# Create your views here.

def home(request):
    return render(request, 'index.html',{'title': 'Home Page'})

def Donor(request):
    form = Postform()
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Donor')
    return render(request, 'donor.html', {'title': 'Donors Registration', 'form': form})

def donor_info(request):
    form = Postform()
    data = Donorinfo.objects.all()
    return render(request, 'donors_info.html',{'title':'Confirmation','rows':data})


class DonorCreate(CreateView):
    model = Donorinfo
    fields = ['firstname', 'lastname','address','city','state','postalcode','country','bloodgroup','phonenumber','email']
    template_name = 'donor_form.html'