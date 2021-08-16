from django.shortcuts import render

# Create your views here.

def indexPage(request):
    return render(request,'index.html')
def productsHomePage(request):
    return render(request,'shop-left-sidebar.html')
def storeLocator(request):
    return render(request,'store-locator-home-page.html')