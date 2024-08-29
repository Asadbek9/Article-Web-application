from django.shortcuts import render


def categories(requests):
    return render(requests, 'categories.html')
