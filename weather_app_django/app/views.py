from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def weather_app(request):
    if request.method == "POST":
        lati=request.POST['lat']
        longi=request.POST['long']
        context = {
            'lati':lati,
            'longi':longi
        }
    else:
        context = {}
return render(request,'weather.html',context)
