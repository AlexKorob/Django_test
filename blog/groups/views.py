from django.shortcuts import render
from .models import Group, Person
import json
from django.http.response import JsonResponse

def index(request):
    group_name = request.GET["group_name"]
    group = list(Person.objects.filter(membership__group__name=group_name).values())
    return JsonResponse(group, safe=False)
