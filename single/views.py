from django.shortcuts import render

def single(requests):
    return render(requests, 'single.html')
