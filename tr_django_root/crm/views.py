from django.shortcuts import render
from .models import Order
from.forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import sendtelegram

def first_page(request):
    slider = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    context = {'slider':slider, 'pc_1':pc_1, 'pc_2': pc_2, 'pc_3':pc_3, 'price_table':price_table, 'form': form}
    return render(request, 'index.html', context)

def thanks(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        sendtelegram(name, phone)
        return render(request,'thanks.html', {'name':name, 'phone':phone})
    return render(request,'thanks.html')