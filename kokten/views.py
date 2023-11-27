import subprocess
from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from venv import activate_venv

# Create your views here.


def index(request):
    return render(request, "index.html")


def venv(request, venv_name):
    activate_venv(venv_name)
    context = {'venv_name': venv_name}
    return render(request, 'index.html', context)

def create_venv(request):
    try:
        # Yeni venv oluştur
        subprocess.run(['python', '-m', 'venv', 'venv_name'], check=True)
        return HttpResponse(status=200)  # Başarılı yanıt
    except Exception as e:
        print("Hata:", e)
        return HttpResponse(status=500)  # Hata durumunda 500 hatası döndür