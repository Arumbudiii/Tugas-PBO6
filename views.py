from django.shortcuts import render

def about (request):
    isi = "Selamat Datang pengguna baru The Ocean !!! Segera pantau kondisi cuaca di perairan sebelum berlayar serta pergerakan angin di lautan tujuan kalian berlayar."
    menu = ["cuaca", 'ombak', 'angin']
    akhr = "dst"

    konteks = {
        's' : isi,
        'menu' : menu,
        'akh' :akhr
    }
    return render(request,'about.html',konteks)

def member (request):
    return render(request,'member.html')

# Create your views here.
