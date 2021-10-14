"""quap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('',indexPage),

    path('robots.txt',TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml',TemplateView.as_view(template_name="sitemap.xml", content_type="text/plain")),
    path('sitemap.html',TemplateView.as_view(template_name="sitemap.html")),

    path('used-auto-parts-search',productsSearchPage),
    path('used-auto-parts-search/<str:part>',productsSearchPageCategory),
    path('used-auto-parts-us',productHomePage),
    path('used-auto-parts-us/<str:pname>',singleProductPage),

    path('products-shops-local',productShopLocalArea),
    path('states',storeLocator),
    path('blogs/<str:title>',blogDetailsRightSidebar),
    #path('download-cities',downloadCities),
    path('used-auto-parts/<str:statename>',displayCities),
    path('used-auto-parts/<str:statename>/<str:cityname>',cityDetailswithProducts),
    path('select-city/<str:statename>',storeLocatorCounties),
    path('blogs',blogHomePage),
    path('subscribe-quap-emails',subscribeNow),
    path('get-instant-quote',contactWithPart),
    path('contact-us',contactUS),
    path('contact-us/<str:part>',contactUsWithPartName),
    path('order-part-now/<str:part>',orderPartNow),
    path('about-us',aboutUS),

    path('order-completed',orderCompleted),

    # Test
    path('cp',changeProductName),
]

