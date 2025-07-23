from django.http import HttpResponse

def saludo (request):
    return HttpResponse("bienveido a mi sitio web victoriano")    
