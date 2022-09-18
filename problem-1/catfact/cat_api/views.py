from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Catfact

# Create your views here.
def index(request):
    catList = Catfact.objects.all()
    context = {'catList':catList}
    return render(request, 'cat_api/list.html', context)

def catfact_list(request):
    MAX_OBJECTS = 20
    catfact = Catfact.objects.all()[:MAX_OBJECTS]
    data = {"results":list(catfact.values("fact", "length"))}
    return JsonResponse(data)

def catfact_detail(request, pk):
    catfact = get_object_or_404(Catfact, pk=pk)
    data = {"results":{
        "fact":catfact.fact, 
        "length":catfact.length
    }}
    return JsonResponse(data)

def detail(request, catId):
    cat = Catfact.objects.get(id=catId)
    context = {'cat':cat}
    return render(request, 'cat_api/detail.html', context)