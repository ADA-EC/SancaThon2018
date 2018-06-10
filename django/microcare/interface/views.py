from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	

	return render(request, "view/index.html")#, {'now': now, 'iuv_data_hora': data_hora, 'state': state, 'state_color': stateColor, 'rain':rain, 'night':night, 'iuv': iuv, 'sunrise': sunrise, 'sunset': sunset, 'manual': manual})

def view(request):
    return render(request, "view/view.html")

def search(request):
    return render(request, "view/search.html")

def manage(request):
    return render(request, "view/manage.html")

def exit(request):
    return render(request, "view/exit.html")
