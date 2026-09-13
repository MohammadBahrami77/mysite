from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# def http_test(request):
#     # return HttpResponse('http_test')
#     return HttpResponse('<h1>this is a test</h1>')

# def json_test(request):
#     return JsonResponse({'name':'mohammad'})


def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')