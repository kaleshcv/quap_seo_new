from django.shortcuts import render, redirect
import json,urllib,requests
from .models import *
from django.contrib import messages

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
    url_ob = request.get_host()
    blogs = Blogs.objects.all()
    parts = Products.objects.all()
    all_years = Years.objects.all()
    brands = Brands.objects.all()
    products = Products.objects.exclude(product_image="products/default.jpg")
    data = {'blogs': blogs,'parts':parts,'all_years':all_years,'brands':brands,'url':url_ob,'products':products}
    return render(request,'index.html',data)


def productHomePage(request):
    side_products = Products.objects.all()[:20]
    products = Products.objects.exclude(product_image="products/default.jpg")
    brands = Brands.objects.all()[:15]
    data = {'products': products, 'brands': brands, 'side_products': side_products}
    return render(request, 'shop-left-sidebar.html', data)


def productsSearchPage(request):
    if request.method == 'POST':
        part = request.POST['part']
        parts = Products.objects.filter(product_name__contains=part)

        if parts.count() > 0:
            parts = parts
            parts_count = parts.count()
            messages.info(request, str(parts_count) + ' Related products found')
        else:
            messages.info(request, 'The product you submitted is not available')
            parts = Products.objects.all()
            parts_count = 0

        all_years = Years.objects.all()
        brands = Brands.objects.all()
        data = {'parts': parts, 'all_years': all_years, 'brands': brands, 'part': part,'part_count':parts_count}
        return render(request, 'contact-us-with-part-catefory.html', data)
    else:

        parts = Products.objects.all()
        all_years = Years.objects.all()
        brands = Brands.objects.all()
        data = {'parts': parts, 'all_years': all_years, 'brands': brands}
        return render(request, 'contact-us-with-part-catefory.html', data)


def productsSearchPageCategory(request,part):
    part = part
    parts = Products.objects.filter(product_name__contains=part)

    if parts.count() > 0:
        parts = parts
        parts_count = parts.count()
        messages.info(request, str(parts_count) + ' Related products found')
    else:
        messages.info(request, 'The product you submitted is not available')
        parts = Products.objects.all()
        parts_count = 0

    all_years = Years.objects.all()
    brands = Brands.objects.all()
    data = {'parts': parts, 'all_years': all_years, 'brands': brands, 'part': part, 'part_count': parts_count}
    return render(request, 'contact-us-with-part-catefory.html', data)


def singleProductPage(request,pname):
    if request.method == 'POST':
        pid = request.POST['pid']
        product = Products.objects.get(id=pid)
        all_years = Years.objects.all()
        brands = Brands.objects.all()
        data = {'product': product, 'years': all_years, 'brands': brands}
        return render(request, 'single-product.html', data)

    else:
        part = pname.replace('-',' ')
        part = part.title()
        try:
            product = Products.objects.get(product_name__iexact=part)
        except Products.DoesNotExist:
            product = None
            messages.info(request,'The requested product does not exist')
            return redirect('/used-auto-parts-us')
        all_years = Years.objects.all()
        brands = Brands.objects.all()
        data = {'product': product,'years':all_years,'brands':brands}
        return render(request, 'single-product.html', data)



def productShopLocalArea(request):
    return render(request, 'shop-left-sidebar-from-counties.html')

def storeLocator(request):

    locations = StateCityList.objects.values_list('state', flat=True).distinct()
    locations = State.objects.all()
    data={'locations':locations}
    return render(request,'store-locator-home-page.html',data)

def displayCities(request,statename):

    state = statename.replace('-' , ' ')
    state = state.title()
    cities = StateCityListNew.objects.filter(state__iexact = state)
    products = Products.objects.exclude(product_image="products/default.jpg")
    side_products = Products.objects.all()[:10]
    desc = State.objects.get(name__iexact = state)
    brands = Brands.objects.all()[:10]
    data = {'cities':cities,'state':state,'products':products,'side_products':side_products,'desc':desc,'brands':brands}
    return render(request, 'store-locator-city-page.html', data)

def cityDetailswithProducts(request,statename,cityname):

    state = statename.replace('-', ' ')
    state = state.title()
    city = cityname.replace('-', ' ')
    city = city.title()
    city_details = StateCityListNew.objects.get(county_or_city__iexact = city)
    products = Products.objects.exclude(product_image="products/default.jpg")
    side_products = Products.objects.all()[:10]
    brands = Brands.objects.all()[:10]
    data = {'city_details':city_details,'state':state,'city':city,'products':products,'side_products':side_products,'brands':brands}
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

def blogDetailsRightSidebar(request,title):

    title = title.replace('-',' ')
    blog = Blogs.objects.get(title__iexact=title)
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
        data = {'year':year,'part':part,'brand':brand}
        return render(request,'thanks-for-order.html',data)

def orderCompleted(request):
    return render(request,'thanks-for-order.html')

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

