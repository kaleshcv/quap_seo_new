from django.shortcuts import render
import json,urllib,requests
from .models import *
# Create your views here.

def downloadCities(request):

    url = 'https://parseapi.back4app.com/classes/Uscounties_Area?count=1&limit=1000000'
    headers = {
        'X-Parse-Application-Id': 'TCZwiRougYSZWViRAoXSeWLxRCRSqaPxK52eeH9k', # This is your app's application id
        'X-Parse-REST-API-Key': 'nmFAnDMfAvbfWjaRERO7ZChuV0jLf23aN20focQz' # This is your app's REST API key
    }
    data = json.loads(requests.get(url,headers=headers).content.decode('utf-8')) # Here you have the data that you need
    #print(json.dumps(data, indent=2))

    states = (data['results'])
    for i in states:
        FIPSCode = i['FIPSCode']
        state = i['state']
        stateAbbreviation = i['stateAbbreviation']
        countyCode = i['countyCode']
        countyName = i['countyName']
        states_obj = StateCityList(FIPSCode=FIPSCode,state=state,stateAbbreviation=stateAbbreviation,countyCode=countyCode,countyName=countyName)
        states_obj.save()


def indexPage(request):
    return render(request,'index.html')
def productsHomePage(request):
    return render(request,'shop-left-sidebar.html')
def storeLocator(request):

    locations = StateCityList.objects.values_list('state', flat=True).distinct()
    print(locations)
    data={'locations':locations}
    return render(request,'store-locator-home-page.html',data)

def storeLocatorCounties(request,statename):

    statename = statename
    location = StateCityList.objects.filter(state=statename)
    data = {'location':location,'state':statename}
    return render(request,'store-locator-county-page.html',data)

def blogDetailsRightSidebar(request):
    return render(request,'blog-details-right-sidebar.html')