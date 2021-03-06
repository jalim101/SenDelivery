from cust.models import Client
from Dish.models import MainDish
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Order
import datetime
import random


def purchase(request, my_name):
    username = request.user.username
    user = User.objects.get(username=username)
    data = Client.objects.get(user=user)
    maindish = MainDish.objects.get(name=my_name)
    if data.prime == True:
        price = maindish.price * 1

    else:
        price = maindish.price
    context = {'client': data, 'price': price, 'dish': maindish}
    return render(request, "purchase.html", context)


def placed(request, my_name):
    if request.method == 'POST':
        username = request.user.username
        form_data = request.POST
        quantity = form_data['quantity']
        user = User.objects.get(username=username)
        client = Client.objects.get(user=user)
        maindish = MainDish.objects.get(name=my_name)

        deliver = datetime.datetime.strptime(
            f"{form_data['delivery-date']} {form_data['delivery-time']}",
            "%Y-%m-%d %H:%M")
        delivery_time = deliver.strftime("%H:%M:%S ")
        delivery_date = deliver.strftime("%m-%d-%Y")
        delivery_datetime = deliver.strftime("%m-%d-%Y %H:%M:%S")

        now = datetime.datetime.now()
        current_date = now.strftime("%m-%d-%Y")
        current_time = now.strftime("%H:%M:%S")

        if client.prime:
            total_price = maindish.price * int(quantity) + 200

        else:
            total_price = maindish.price * int(quantity) + 200

        Order.objects.create(
            user=client, cuisine=maindish, quantity=quantity, placed_time=current_time,
            delivery_datetime=delivery_datetime, delivery_date=delivery_date, delivery_time=delivery_time,
            total_price=total_price, placed_date=current_date)
        order = Order.objects.get(
            user=client, cuisine=maindish, quantity=quantity, placed_time=current_time,
            delivery_datetime=delivery_datetime, delivery_time=delivery_time, total_price=total_price,
            delivery_date=delivery_date, placed_date=current_date)
        context = {'client': client, 'order': order, 'total_price': total_price}
        return render(request, "placed.html", context)
    else:
        messages.info(request, 'Check Your History For Placed Orders')
        return redirect('/')


def delete(request):
    username = request.user.username
    user = User.objects.get(username=username)
    client = Client.objects.get(user=user)
    order_data = Order.objects.filter(user=client)
    order_data.delete()
    return redirect('/user/history/')


def cancel(request, my_id):
    username = request.user.username
    user = User.objects.get(username=username)
    client = Client.objects.get(user=user)
    order_data = Order.objects.get(user=client, order_id=my_id)
    order_data.delete()
    return redirect('/user/history')
