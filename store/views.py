from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'store/home.html')

def store(request):
    return render(request, 'store/store.html')