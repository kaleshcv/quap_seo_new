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
    path('products-shops',productsHomePage),
    path('products-shops-local',productShopLocalArea),
    path('States',storeLocator),
    path('blog-details-right-sidebar/<int:pk>',blogDetailsRightSidebar),
    #path('download-cities',downloadCities),
    path('Used-Auto-Parts/<str:statename>',displayCities),
    path('Used-Auto-Parts/<str:statename>/<str:cityname>',cityDetailswithProducts),
    path('select-city/<str:statename>',storeLocatorCounties),
    path('quap-all-blogs',blogHomePage),
    path('subscribe-quap-emails',subscribeNow),
    path('get-instant-quote',contactWithPart),
    path('contact-us',contactUS),
    path('contact-us/<str:part>',contactUsWithPartName),
    path('order-part-now/<str:part>',orderPartNow),
    path('about-us',aboutUS),

    # Test
    path('cp',changeProductName),
]

