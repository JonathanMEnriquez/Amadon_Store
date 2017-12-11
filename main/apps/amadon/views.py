# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'amadon/index.html')

def process(request):
    if request.method == 'POST':
        try:
            request.session['count'] += 1
        except:
            request.session['count'] = 1
        try:
            request.session['orders']
        except:
            request.session['orders'] = []
        new_order = {}

        for k, v in request.POST.iteritems():
            if k != 'csrfmiddlewaretoken':
                new_order[k] = v
        new_order['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
        new_order['order_number'] = request.session['count']
        new_order['price'] = float(request.POST['price']) * float(request.POST['quantity'])
        temp = []
        temp = request.session['orders']
        temp.append(new_order)
        request.session['orders'] = temp
        request.session['price'] = new_order['price']
        print request.session['orders']
        return redirect('/orders')
    else:
        return redirect('/')

def orders(request):
    return render(request, 'amadon/orders.html')