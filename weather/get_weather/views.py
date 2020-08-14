from django.shortcuts import render
import requests

def input_form(request):
    return render(request, 'input_form.html')
