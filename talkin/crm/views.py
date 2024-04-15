from django.shortcuts import render


from django.http import HttpResponse

def register (request):
    return render(request, 'crm/register.html')

def home(request):

    context = {'first_name': "Robby", 'message': "This needs real data"}



    return render(request, 'crm/index.html', context)

def errorMessage(request):
    return HttpResponse("ERROR YOU SILLY GOOSE. 404. 404. 404. 500.")