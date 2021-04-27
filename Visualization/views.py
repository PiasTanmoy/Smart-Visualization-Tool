from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def csv_data_read(request):
    return render(request, 'JS-learn.html')

def bar(request):
    return render(request, 'bar.html')

def multiple_chart(request):
    return render(request, 'multiple_chart.html')

def smartScale(request):
    return render(request, 'smartScaleData.html')

def smartScale2(request):
    return render(request, 'smartScaleData2.html')

def dataSelection(request):
    return render(request, 'data_selection.html')