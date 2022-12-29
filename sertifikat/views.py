from django.shortcuts import render
from django.http import HttpResponse
from .forms import Zipform
from .pillow import process
from .models import HslSertifikat
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method=='POST':
        form=Zipform(request.POST,request.FILES)
        if form.is_valid():
            filezip=process(request.FILES['image'],request.FILES['datacsv'],request.POST.get("position",""),request.POST.get("size",""),request.POST.get("colour",""),request.POST.get("font",""))
            zipsave=HslSertifikat(file=filezip)
            zipsave.save()
            print(zipsave.file.url)
    return render(request,'sertifikat/index.html',context={"down":zipsave})

def test(request):
    return render(request,'sertifikat/test.html')

