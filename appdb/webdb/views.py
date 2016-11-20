from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.contrib.postgres.search import SearchQuery
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Count
from .models import Rating
from .models import Professor
from .models import University
from itertools import chain
#from jsonmerge import merge
import json
from django.db.models import Q

#Create your views here.

def index(request):

    records = Professor.objects.all()   
    data = serializers.serialize("json", records)

    return HttpResponse(data, content_type='application/json')
    
def rating(request):

    records = Rating.objects.all()
    #records = records.pk
    #data = records.aggregate(rating0 = Avg('rating0'))
    #dataf = json.dumps({'avg0': int(data['rating0'])})
    data = serializers.serialize("json", records)
    #return HttpResponse(data['rating0'])
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def insertRating(request):

    if request.method == "POST":
        name = request.POST['name']
        fname = name.split() 
        records = Professor.objects.get(firstName = fname[0], lastName = fname[1])
        r0 = request.POST['rating0']
        r1 = request.POST['rating1']
        b = Rating(professor = records , rating0 = int(r0), rating1 = int(r1))
        b.save()
        return HttpResponse("true")
    
    else:
        return HttpResponse("erro")


@csrf_exempt
def searchProfessor(request):
    
    if request.method == "POST":
        try:
            nameFull = request.POST['searchQuery']        
            Name = nameFull.split() 
            if(len(Name) == 2):
                records = Professor.objects.filter(firstName__icontains=Name[0], lastName__icontains=Name[1])             
                if (not records):
                    records = Professor.objects.filter(course__iexact=nameFull)
            else:    
                records = Professor.objects.filter(Q(firstName__icontains=nameFull) | Q(lastName__icontains=nameFull) | Q(course__iexact=nameFull))
            if (not records):
                uRecords = University.objects.filter(sigla__iexact=nameFull)
                if (not uRecords):
                    return HttpResponse("no rows")
                records = Professor.objects.filter(university=uRecords)
                if (not records):
                    return HttpResponse("no rows")
            if (len(records) < 2):
                uni = University.objects.filter(pk=(records.values_list('university')[0][0]))
                agr = Rating.objects.filter(professor=records).aggregate(avr0 = Avg('rating0'), avr1 = Avg('rating1'), num = Count('rating0'))         
                if(not agr):
                    return HttpResponse("no rows")
                fName = records.values_list('firstName', 'lastName', 'course')
                univ = uni.values_list('name', 'sigla')
                recf = json.dumps([{'avg0' :int(agr['avr0']), 'avg1' : int(agr['avr1'] ), 'num':int(agr['num']), 'firstName':fName[0][0], 'lastName':fName[0][1], 'course':fName[0][2],'uniName':univ[0][0], 'uniSgl':univ[0][1] }])
            else:
                recf = serializers.serialize("json", records)

            return HttpResponse(recf, content_type='application/json')
        except:
            nameFull = request.POST.get('name')
            uni = request.POST.get('uni')
            return twoFilter(nameFull, uni)

    else:
        return HttpResponse("erro")

def twoFilter(nameFull, uni):
    universidade = University.objects.filter(sigla__icontains=uni)
    Name = nameFull.split()
    if(len(Name) == 2):
        records = Professor.objects.filter(firstName__icontains=Name[0], lastName__icontains=Name[1], university=universidade)
    else:
        records = Professor.objects.filter(Q(firstName__icontains=nameFull) | Q(lastName__icontains=nameFull), university=universidade)

    if (not records):
        return HttpResponse("no rows")
    recf = serializers.serialize("json", records)
    return HttpResponse(recf, content_type='application/json')





    
