from django.shortcuts import render
from django.http import HttpResponse
from .forms import Zipform
from .pillow import process
from .models import HslSertifikat
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404

@csrf_exempt
def index(request):
    if request.method=='POST':
        form=Zipform(request.POST,request.FILES)
        print(request.POST)
        print("request file")
        print(request.FILES)
        filezip=process(request.FILES['image'],request.FILES['datacsv'],request.POST.get("position",""),request.POST.get("size",""),request.POST.get("color",""),request.POST.get("font",""))
        zipsave=HslSertifikat(file=filezip)
        # zipsave.save()
        response = HttpResponse(filezip.read(), content_type="application/zip")
        response['Content-Disposition'] = 'inline; filename=' + str(filezip)
        return response
    raise Http404
    # return render(request,'sertifikat/index.html',context={"down":zipsave})

def test(request):
    return render(request,'sertifikat/test.html')

