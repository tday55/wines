from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import Wine, Stock

def index(request):
    latest_wine_list = Wine.objects.order_by('maker__country', 'wine_type', 'blend')
    template = loader.get_template('winecat/index.html')
    context = {
        'latest_wine_list': latest_wine_list,
    }
    return HttpResponse(template.render(context, request))

def winelist(request):
    my_stock = Stock.objects.filter(opened__isnull=True).order_by('wine__maker__country', 'wine__wine_type', 'wine__blend')
    template = loader.get_template('winecat/winelist.html')
    context = {
        'my_stock': my_stock,
    }
    return HttpResponse(template.render(context, request))

def wine(request, wine_id):
    this_wine = Wine.objects.filter(id=wine_id)
    template = loader.get_template('winecat/onewine.html')
    context = {
        'this_wine': this_wine,
    }
    return HttpResponse(template.render(context, request))

def makers(request, maker_id):
    this_maker = Wine.objects.filter(maker = maker_id).order_by('maker__name')
    template = loader.get_template('winecat/onemaker.html')
    context = {
        'this_maker': this_maker,
    }
    return HttpResponse(template.render(context, request))

def appellations(request, appellation_in):
    this_appellation = Wine.objects.filter(appellation = appellation_in).order_by('maker__name')
    template = loader.get_template('winecat/oneappellation.html')
    context = {
        'this_appellation': this_appellation,
    }
    return HttpResponse(template.render(context, request))


def slots(request, location_id):
    return HttpResponse("You're looking at location %s." % location_id)

def types(request, wine_id):
    response = "You're looking at wines from %s."
    return HttpResponse(response % wine_id)

