from django.shortcuts import render
from django.http import HttpResponse
from .models import Device, Equipament

# Create your views here.

def index(request):
	

	return render(request, "view/index.html")
    
def view(request):
    return render(request, "view/view.html")

def search(request):
    query_results = None
    equipament_query_results = []
    if request.method == 'GET':
        if request.GET.get('name'):
            name = request.GET['name']
            equipament_query_results = Equipament.objects.filter(name__contains=name).select_related('device')
            print(equipament_query_results)
            # = Equipament.objects.filter(name__contains=name).values()
            #device_query_results = []
            #for equip in equipament_query_results:
                #help(equip)
            #    mac = equip.device_id
            #    device_query_results.append(Device.objects.filter(mac_address=mac))
            #equipament_query_results.append(device_query_results)				
    return render(request, "view/search.html", { 'equipament_query_results': equipament_query_results } )

def manage(request):
    return render(request, "view/manage.html")

def exit(request):
    return render(request, "view/exit.html")
