
from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
from django.conf import settings
import os

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']
            # print(res_name,url)

            # Generate QR Code
            qr = qrcode.make(url)
            #   print(qr)
            file_name = res_name.replace(" ","_").lower()+"_menu.png"
            file_path = os.path.join(settings.MEDIA_ROOT,file_name)
            qr.save(file_path)

            # create image url
            qr_url =os.path.join(settings.MEDIA_URL,file_name)
          
            return render(request,'qr-result.html',{'res_name':res_name,'qr_url':qr_url,'file_name':file_name})
          
    else:
        form = QRCodeForm()
    return render(request,'generate-qr-code.html',{'form':form})