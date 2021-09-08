from django.shortcuts import render, redirect
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

    blogs = Blogs.objects.all()
    parts = Products.objects.all()
    all_years = Years.objects.all()
    brands = Brands.objects.all()
    data = {'blogs': blogs,'parts':parts,'all_years':all_years,'brands':brands}
    return render(request,'index.html',data)

def productsHomePage(request):
    return render(request,'shop-left-sidebar.html')

def productShopLocalArea(request):
    return render(request, 'shop-left-sidebar-from-counties.html')

def storeLocator(request):

    locations = StateCityList.objects.values_list('state', flat=True).distinct()
    data={'locations':locations}
    return render(request,'store-locator-home-page.html',data)

def storeLocatorCounties(request,statename):
    statename = statename
    location = StateCityList.objects.filter(state=statename)
    data = {'location':location,'state':statename}
    return render(request,'store-locator-county-page.html',data)

def blogHomePage(request):
    blogs = Blogs.objects.all()
    data = {'blogs':blogs}
    return render(request,'blog-list-fullwidth.html',data)

def blogDetailsRightSidebar(request,pk):
    pk=pk
    blog = Blogs.objects.get(id=pk)
    recent_blogs = Blogs.objects.all().order_by('-date_created')[:10]
    data = {'blog':blog,'recent_blogs':recent_blogs}
    return render(request,'blog-details-right-sidebar.html',data)

def subscribeNow(request):
    if request.method == 'POST':
        email_id = request.POST['email']
        email = EmailSubscriptions.objects.create(email_id = email_id)
        email.save()
        return redirect('/')
    else:
        return redirect('/')

def contactWithPart(request):
    if request.method == 'POST':
        year = request.POST['year']
        part = request.POST['part']
        brand = request.POST['brand']
        customer_name = request.POST['customer_name']
        customer_phone = request.POST['customer_phone']
        customer_email = request.POST['customer_email']




