
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def register(request):
    return HttpResponse("Up and running")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', register)
]
