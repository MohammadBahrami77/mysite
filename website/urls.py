from django.urls import path
from website.views import *

urlpatterns = [
    # path('http-test', http_test),
    # path('json-test', json_test)

    path('',index_view),
    path('about',about_view),
    path('contact',contact_view)
]