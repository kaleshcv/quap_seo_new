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
    side_products = Products.objects.all()[:20]
    products = Products.objects.exclude(product_image="products/default.jpg")
    brands = Brands.objects.all()[:15]
    data = {'products':products,'brands':brands,'side_products':side_products}
    return render(request,'shop-left-sidebar.html',data)

def productShopLocalArea(request):
    return render(request, 'shop-left-sidebar-from-counties.html')

def storeLocator(request):

    locations = StateCityList.objects.values_list('state', flat=True).distinct()
    locations = State.objects.all()
    data={'locations':locations}
    return render(request,'store-locator-home-page.html',data)

def displayCities(request,statename):
    state = statename
    cities = StateCityListNew.objects.filter(state = statename)
    products = Products.objects.exclude(product_image="products/default.jpg")
    side_products = Products.objects.all()[:20]
    desc = State.objects.get(name = statename)
    data = {'cities':cities,'state':state,'products':products,'side_products':side_products,'desc':desc}
    return render(request, 'store-locator-city-page.html', data)

def cityDetailswithProducts(request,statename,cityname):
    state = statename
    city = cityname
    city_details = StateCityListNew.objects.get(county_or_city = city)
    products = Products.objects.exclude(product_image="products/default.jpg")
    side_products = Products.objects.all()[:20]
    data = {'city_details':city_details,'state':state,'city':city,'products':products,'side_products':side_products}
    return render(request,'city-product-page.html',data)


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

        customer = Customer.objects.create(year = year,part = part, brand = brand,
                   customer_name=customer_name,customer_phone=customer_phone,customer_email=customer_email)
        customer.save()
        return redirect('/')


def contactUS(request):

    parts = Products.objects.all()
    all_years = Years.objects.all()
    brands = Brands.objects.all()
    data = {'parts': parts, 'all_years': all_years, 'brands': brands}
    return render(request,'contact-us.html',data)

def contactUsWithPartName(request,part):
    part = part
    parts = Products.objects.all()
    all_years = Years.objects.all()
    brands = Brands.objects.all()
    data = {'parts': parts, 'all_years': all_years, 'brands': brands,'part':part}
    return render(request, 'contact-us-with-part.html', data)

def orderPartNow(request,part):
    part = part
    parts = Products.objects.filter(product_name__contains = part)
    all_years = Years.objects.all()
    brands = Brands.objects.all()
    data = {'parts': parts, 'all_years': all_years, 'brands': brands, 'part': part}
    return render(request, 'contact-us-with-part-catefory.html', data)

def aboutUS(request):
    return render(request,'about-us.html')

def changeProductName(request):
    p = Products.objects.all()[:10]
    for i in p:

        print(i.product_name)
        new = i.product_name.lower()
        new = new.replace(' ','-')
        new = new.replace('/', '')
        print(new)

