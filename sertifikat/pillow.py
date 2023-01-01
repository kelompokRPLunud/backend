from PIL import Image as im
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
import pandas as pd
from io import BytesIO
import zipfile
from django.core.files.uploadedfile import InMemoryUploadedFile

def processImage(images,xper,yper,text,height,width,box,thefont,colour):
    besarfont=box[2]
    tinggifont=box[3]
    xper=(width/100)*xper
    xper=xper-(besarfont//2)
    yper=(height/100)*yper
    yper=yper-tinggifont
    draw=ImageDraw.Draw(images)
    draw.text((xper,yper),text,font=thefont,fill=colour)
    return images
def processSertif(image,add,xy,hsl,fontsize,colour,fonts):
    width,height=image.size
    listofimage=[]
    for i in range(hsl.shape[0]):
        tempimg=image.copy()
        for z in range(len(add)):
            thefont=ImageFont.truetype('arial.ttf',int(fontsize[z]))
            tempimg=processImage(tempimg,int(xy[z][0]),int(xy[z][1]),str(hsl[add[z]][i]),height,width,thefont.getbbox(str(hsl[add[z]][i])),thefont,colour[z])
        listofimage.append(tempimg)
    return listofimage

def process(cv2_img,csv,xy,fontsiz,colour,font):
    csvfile=csv.read().decode("utf-8")
    lines=csvfile.split("\r\n")
    lines=[i.split(",") for i in lines]
    names=cv2_img.name.split(".")
    #color255,255,255|255,255,255 = [(255,255,255),(255,255,255)]
    colour=colour.split("|")
    for i in range(len(colour)):
        colour[i]=tuple([int(z) for z in colour[i].split(",")])    
    code=BytesIO(cv2_img.read())
    cv2_img=im.open(code)
    hsl=pd.DataFrame(lines[1:],columns=lines[0])
    indexadd=[]
    xy=str(xy).split("|")
    for i in range(len(xy)):
        xy[i]=str(xy[i]).split(",")
    fontsiz=fontsiz.split("|")
    for i in hsl:
        if i[0]=="#":
            indexadd.append(i)
    image=processSertif(cv2_img,indexadd,xy,hsl,fontsiz,colour,font)
    zip_buffer=BytesIO()
    zip_file=zipfile.ZipFile(zip_buffer,'w')
    for i in range(len(image)) :
        imagestream=BytesIO()
        image[i].save(imagestream,'JPEG')
        imagestream.seek(0)
        zip_file.writestr("{}.jpg".format(i),imagestream.read())
    zip_file.close()
    zip_buffer.seek(0)
    isi_zip= InMemoryUploadedFile(
        zip_buffer,
        None,
        names[0]+".zip",
        'application/zip',
        zip_buffer.getbuffer().nbytes,
        None
    )

    return isi_zip

    
