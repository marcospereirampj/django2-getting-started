from django.http import HttpResponse


def home_page(request):
    return HttpResponse("Hello, world. You're at the polls index.")