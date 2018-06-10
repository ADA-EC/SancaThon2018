from django.shortcuts import render
from django.http import HttpResponse
from .models import Device, Equipament

# Create your views here.

def index(request):
	return render(request, "view/index.html")
    
def locate(request):
    equipament = None
    # distance uses symbolic values just for mockup purposes
    distance = ""
    if request.method == 'GET':
        if request.GET.get('localization'):
            category = request.GET['category']
            localization = request.GET['localization']
            equipaments = Equipament.objects.filter(category__startswith=category).select_related('device')
            for equip in equipaments:
                if equip.device.last_position == localization:
                    distance = "0"
                    return render(request, "view/locate.html", { 'item': equip, 'distance': distance } )
            distance = "230"
            return render(request, "view/locate.html", { 'item': equipaments.first, 'distance': distance } )
    return render(request, "view/locate.html", { 'item': equipament, 'distance': distance } )

def look(request):
    equipament_query_results = []
    if request.method == 'GET':
        if request.GET.get('name'):
            name = request.GET['name']
            equipament_query_results = Equipament.objects.filter(name__contains=name).select_related('device')
    return render(request, "view/look.html", { 'equipament_query_results': equipament_query_results } )

def manage(request):
    if request.method == 'GET':
        if request.GET.get('name'):
            name = request.GET['name']
            category = request.GET['category']
            mac = request.GET['mac']
            device = Device(mac_address=mac)
            equipament = Equipament(name=name, category=category, device=device)
            device.save()
            equipament.save()
    return render(request, "view/manage.html")

def exit(request):
    return render(request, "view/exit.html")
