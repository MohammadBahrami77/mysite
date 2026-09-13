from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# def http_test(request):
#     # return HttpResponse('http_test')
#     return HttpResponse('<h1>this is a test</h1>')

# def json_test(request):
#     return JsonResponse({'name':'mohammad'})


def index_view(request):
    return HttpResponse('<h1>Home Page</h1>')

def about_view(request):
    return HttpResponse('<h1>About Page</h1>')

def contact_view(request):
    return HttpResponse('<h1>Contact Page</h1>')