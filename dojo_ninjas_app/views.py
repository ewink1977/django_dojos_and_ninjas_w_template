from django.shortcuts import render, redirect, HttpResponse
from .models import *

def home(request):
    context = {"dojos": Dojos.objects.all(), "ninjas": Ninjas.objects.all()}
    return render(request, 'dojos\index.html', context)

def newdojo(request):
    if request.method == 'POST':
        newname = request.POST['name']
        newcity = request.POST['city']
        newstate = request.POST['state']
        Dojos.objects.create(name = newname, city = newcity, state = newstate, desc = 'Added via webform.')
        return redirect('/')

def newninja(request):
    if request.method == 'POST':
        newfirst = request.POST['first_name']
        newlast = request.POST['last_name']
        assigneddojo = Dojos.objects.get(id=request.POST['dojo'])
        Ninjas.objects.create(first_name = newfirst, last_name = newlast, dojo = assigneddojo)
        return redirect('/')

def deletedojo(request, dojotodel):
    if request.method == 'GET':
        doomeddojo = Dojos.objects.get(id=dojotodel)
        doomeddojo.delete()
        return redirect('/')