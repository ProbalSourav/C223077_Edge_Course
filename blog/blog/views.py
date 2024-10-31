from django.http import HttpResponse
from django.views import View

def Man(request):
    return HttpResponse("Welcome to Django")

class man1(View):
    def get(self,request):
        return HttpResponse("Welcome to Man1")