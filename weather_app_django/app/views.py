from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def weather_app(request):
    if request.method == "POST":
        lati=request.POST['lat']
        longi=request.POST['long']
        print(lati, longi)
        return render(request,'weather.html',{'lati':lati,'longi':longi})
    return render(request,'weather.html')