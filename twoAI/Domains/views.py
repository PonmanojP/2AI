from django.shortcuts import render
from .models import ML,DL,Vision,Bigdata,NLP,Edge,Cloud,Web,Design

def ML_view(request):
    ml = ML.objects.all()
    return render(request, 'Domains/ml.html',{'domainobject':ml})

def DL_view(request):
    dl = DL.objects.all()
    return render(request, 'Domains/dl.html',{'domainobject':dl})

def Vision_view(request):
    vision = Vision.objects.all()
    return render(request, 'Domains/vision.html',{'domainobject':vision})

def Bigdata_view(request):
    bigdata = Bigdata.objects.all()
    return render(request, 'Domains/bigdata.html',{'domainobject':bigdata})

def Edge_view(request):
    edge = Edge.objects.all()
    return render(request, 'Domains/edge.html',{'domainobject':edge})

def Cloud_view(request):
    cloud = Cloud.objects.all()
    return render(request, 'Domains/cloud.html',{'domainobject':cloud})

def NLP_view(request):
    nlp = NLP.objects.all()
    return render(request, 'Domains/nlp.html',{'domainobject':nlp})

def Web_view(request):
    web = Web.objects.all()
    return render(request, 'Domains/web.html',{'domainobject':web})

def Design_view(request):
    design = Design.objects.all()
    return render(request, 'Domains/design.html',{'domainobject':design})


