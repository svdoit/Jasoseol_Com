from django.shortcuts import render, redirect
from .forms import JssForm
from .models import Jasoseol
# Create your views here.

def index(request):
    all_jss = Jasoseol.objects.all()
    return render(request, 'index.html', {'all_jss':all_jss})

def create(request):
    if request.method == "POST":
        filled_form = JssForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index')
    jss_form = JssForm()
    return render(request, 'create.html', {'jss_form':jss_form})

def detail(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    return render(request, 'detail.html', {'my_jss':my_jss})
    
def delete(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    my_jss.delete()
    return redirect('index')