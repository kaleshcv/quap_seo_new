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
    engine_set = Products.objects.filter(product_name__icontains='engine').order_by('-id')[:4]
    first_set = Products.objects.all().order_by('-id')[:4]
    second_set = Products.objects.all().order_by('-id')[4:8]

    newproducts = Products.objects.exclude(product_image="products/default.jpg").order_by('-id')[:12]

    data = {'blogs': blogs,'parts':parts,'all_years':all_years,'brands':brands,'url':url_ob,'products':products,
            'first_set':first_set,'second_set':second_set,'engine_set':engine_set,
            'newproducts':newproducts,
            }
    return render(request,'index.html',data)


def productHomePage(request):
    if request.method== 'POST':
        part = request.POST['part']
        products = Products.objects.filter(product_name__icontains=part)
        if products.count()==0:
            products = Products.objects.exclude(product_image="products/default.jpg")
        pop_products = Products.objects.filter(popular_product=True).order_by('-id')[:12]
        brands = Brands.objects.all()
        all_years = Years.objects.all()
        side_products = Products.objects.all().order_by('-id')[100:115]
        data = {'products':products,'pop_products':pop_products,'side_products':side_products,'brands':brands,'years':all_years}
        return render(request, 'shop-left-sidebar.html', data)

    else:
        side_products = Products.objects.all().order_by('-id')[200:215]
        products = Products.objects.exclude(product_image="products/default.jpg")
        brands = Brands.objects.all()
        all_years = Years.objects.all()
        pop_products = Products.objects.filter(popular_product=True).order_by('-id')[:12]
        data = {'products': products, 'brands': brands, 'side_products': side_products,'pop_products':pop_products,'years':all_years}
        return render(request, 'shop-left-sidebar.html', data)



def singleProductPage(request,pname):
    if request.method == 'POST':
        pid = request.POST['pid']
        product = Products.objects.get(id=pid)
        all_years = Years.objects.all()
        brands = Brands.objects.all()
        products = Products.objects.exclude(product_image="products/default.jpg")
        data = {'product': product, 'years': all_years, 'brands': brands,'products':products}
        return render(request, 'single-product.html', data)
    else:
        part = pname.replace('-',' ')

        try:
            product = Products.objects.get(product_name__iexact=part)
        except Products.DoesNotExist:
            product = None
            messages.info(request,'The requested product does not exist')
            return redirect('/used-auto-parts-us')

        all_years = Years.objects.all()
        brands = Brands.objects.all()
        products = Products.objects.exclude(product_image="products/default.jpg")
        data = {'product': product,'years':all_years,'brands':brands,'products':products}
        return render(request, 'single-product.html', data)

def singleProductPageNew(request,pname,pid):
    product = Products.objects.get(id=pid)
    all_years = Years.objects.all()
    brands = Brands.objects.all()
    products = Products.objects.exclude(product_image="products/default.jpg")
    data = {'product': product, 'years': all_years, 'brands': brands, 'products': products}
    return render(request, 'single-product.html', data)



def productShopLocalArea(request):
    return render(request, 'shop-left-sidebar-from-counties.html')

def storeLocator(request):

    locations = StateCityList.objects.values_list('state', flat=True).distinct()
    locations = State.objects.all()
    data={'locations':locations}
    return render(request,'store-locator-home-page.html',data)

def displayCities(request,statename):
    if statename == 'Maryland':
        return redirect('/used-auto-parts/maryland')
    elif statename == 'Texas':
        return redirect('/used-auto-parts/texas')
    elif statename == 'Mississippi':
        return redirect('/used-auto-parts/mississippi')

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
    if statename == 'Maryland' and cityname == 'Baltimore':
        return redirect('/used-auto-parts/maryland/baltimore')
    elif statename == 'Texas' and cityname == 'Dallas':
        return redirect('/used-auto-parts/texas/dallas')
    elif statename == 'Texas' and cityname == 'Houston':
        return redirect('/used-auto-parts/texas/houston')
    elif statename == 'Texas' and cityname == 'San Antonio':
        return redirect('/used-auto-parts/texas/san-antonio')
    elif statename == 'Maryland' and cityname == 'Frederick':
        return redirect('/used-auto-parts/maryland/frederick')
    elif statename == 'Maryland' and cityname == 'Germantown':
        return redirect('/used-auto-parts/maryland/germantown')
    elif statename == 'Maryland' and cityname == 'Silver Spring':
        return redirect('/used-auto-parts/maryland/silver-spring')
    elif statename == 'Maryland' and cityname == 'Columbia':
        return redirect('/used-auto-parts/maryland/columbia')
    elif statename == 'Colorado' and cityname == 'Denver':
        return redirect('/used-auto-parts/colorado/denver')
    elif statename == 'Mississippi' and cityname == 'Gulfport':
        return redirect('/used-auto-parts/mississippi/gulfport')
    elif statename == 'Mississippi' and cityname == 'Southaven':
        return redirect('/used-auto-parts/mississippi/southaven')
    elif statename == 'Mississippi' and cityname == 'Hattiesburg':
        return redirect('/used-auto-parts/mississippi/hattiesburg')

    state = statename.replace('-', ' ')
    state = state.title()
    city = cityname.replace('-', ' ')
    city = city.title()
    city_details = StateCityListNew.objects.get(county_or_city__iexact = city,state__iexact=state)
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
    if title == '10' or title == '8' or title == '9':
        return redirect('/blogs')
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
        part_id = request.POST['part_id']
        brand_id = request.POST['brand_id']
        part = Products.objects.get(id=part_id)
        brand = Brands.objects.get(id=brand_id)

        data = {'year':year,'product':part,'brand':brand}
        return render(request,'single-product-search.html',data)
    else:
        pass



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

def offersAndDiscounts(request):
    side_products = Products.objects.all().order_by('-id')[200:215]
    products = Products.objects.exclude(product_image="products/default.jpg")
    brands = Brands.objects.all()[:15]
    pop_products = Products.objects.all()
    data = {'products': products, 'brands': brands, 'side_products': side_products, 'pop_products': pop_products}
    return render(request,'offers-discounts.html',data)

def changeProductName(request):
    p = Products.objects.all()[:10]
    for i in p:

        print(i.product_name)
        new = i.product_name.lower()
        new = new.replace(' ','-')
        new = new.replace('/', '')
        print(new)


#Redirects
def redirectToProductPage(request,pname):
    return redirect('/used-auto-parts-us')
def redirectToProductPageOne(request):
    return redirect('/used-auto-parts-us')
def redirectToBlog(request):
    return redirect('/blogs/benefits-of-buying-used-auto-parts')

# Engine ###########

def categoryEngine(request):
    pass

