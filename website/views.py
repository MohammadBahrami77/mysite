from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm, ContactForm, NewsletterForm

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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()            
    return render(request, 'website/contact.html',{'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')



# def test_view(request):
#     return render(request, 'website/test.html')

def test_view(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():

            form.save()

            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # subject = form.cleaned_data['subject']
            # message = form.cleaned_data['message']
            # print(name, email,subject,message)

            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    form = ContactForm()

    #     form = NameForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         subject = form.cleaned_data['subject']
    #         message = form.cleaned_data['message']
    #         print(name, email,subject,message)
    #         return HttpResponse('done')
    #     else:
    #         return HttpResponse('not valid')
    # form = NameForm()

        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # subject = request.POST.get('subject')
        # message = request.POST.get('message')
        # c = Contact()
        # c.name = name
        # c.email = email
        # c.subject = subject
        # c.message = message
        # c.save()

    return render(request, 'test.html',{'form':form})