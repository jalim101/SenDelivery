from django.shortcuts import render
from django.http import HttpResponse
from cust.models import Client
from django.contrib.auth.models import User
from Dish.models import MainDish


def details(request, my_name):
    data = MainDish.objects.get(name=my_name)
    username = request.user.username
    user = User.objects.get(username=username)
    client = Client.objects.get(user=user)
    if client.prime == True:
        price = data.price * 1
    else:
        price = data.price
    context = {'data': data, 'client': client, 'price': price}
    return render(request, 'details.html', context)


def base(request):
    username = request.user.username
    try:
        user = User.objects.get(username=username)
        data = Client.objects.get(user=user)
        context = {'client': data}
        return render(request, 'base.html', context)

    except:

        context = {}
        return render(request, 'base.html', context)


def index(request):
    username = request.user.username

    dish_European = MainDish.objects.filter(type="European")
    dish_Barmenu = MainDish.objects.filter(type="Bar menu")
    dish_Breakfasts = MainDish.objects.filter(type="Breakfasts")
    dish_Salads = MainDish.objects.filter(type="Salads")
    dish_Firstcourse = MainDish.objects.filter(type="First course")
    dish_Lagman = MainDish.objects.filter(type="Lagman")
    dish_Pizza = MainDish.objects.filter(type="Pizza")
    dish_Eastern = MainDish.objects.filter(type="Eastern")
    dish_Snack = MainDish.objects.filter(type="Snack")
    dish_Meat = MainDish.objects.filter(type="Steak Grill Shashlick")
    dish_Panasian = MainDish.objects.filter(type="Pan Asian")
    dish_Bakery = MainDish.objects.filter(type="Bakery")
    dish_Garnish = MainDish.objects.filter(type="Garnish Sauces")

    number_European = len(dish_European)
    if number_European % 4 == 0:
        European_result = number_European // 4
    else:
        European_result = number_European // 4 + 1

    number_Barmenu = len(dish_Barmenu)
    if number_Barmenu % 4 == 0:
        Barmenu_result = number_Barmenu // 4
    else:
        Barmenu_result = number_Barmenu // 4 + 1

    number_Breakfasts = len(dish_Breakfasts)
    if number_Breakfasts % 4 == 0:
        Breakfasts_result = number_Breakfasts // 4
    else:
        Breakfasts_result = number_Breakfasts // 4 + 1

    number_Salads = len(dish_Salads)
    if number_Salads % 4 == 0:
        Salads_result = number_Salads // 4
    else:
        Salads_result = number_Salads // 4 + 1

    number_Firstcourse = len(dish_Firstcourse)
    if number_Firstcourse % 4 == 0:
        Firstcourse_result = number_Firstcourse // 4
    else:
        Firstcourse_result = number_Firstcourse // 4 + 1

    number_Ladman = len(dish_Lagman)
    if number_Ladman % 4 == 0:
        Lagman_result = number_Ladman // 4
    else:
        Lagman_result = number_Ladman // 4 + 1

    number_Pizza = len(dish_Pizza)
    if number_Pizza % 4 == 0:
        Pizza_result = number_Pizza // 4
    else:
        Pizza_result = number_Pizza // 4 + 1

    number_Eastern = len(dish_Eastern)
    if number_Eastern % 4 == 0:
        Eastern_result = number_Eastern // 4
    else:
        Eastern_result = number_Eastern // 4 + 1

    number_Snack = len(dish_Snack)
    if number_Snack % 4 == 0:
        Snack_result = number_Snack // 4
    else:
        Snack_result = number_Snack // 4 + 1

    number_Meat = len(dish_Meat)
    if number_Meat % 4 == 0:
        Meat_result = number_Meat // 4
    else:
        Meat_result = number_Meat // 4 + 1

    number_Panasian = len(dish_Panasian)
    if number_Panasian % 4 == 0:
        Panasian_result = number_Panasian // 4
    else:
        Panasian_result = number_Panasian // 4 + 1

    number_Bakery = len(dish_Bakery)
    if number_Bakery % 4 == 0:
        Bakery_result = number_Bakery // 4
    else:
        Bakery_result = number_Bakery // 4 + 1

    number_Garnish = len(dish_Garnish)
    if number_Garnish % 4 == 0:
        Garnish_result = number_Garnish // 4
    else:
        Garnish_result = number_Garnish // 4 + 1

    try:
        user = User.objects.get(username=username)
        data = Client.objects.get(user=user)
        context = {

            'client': data, 'dish_European': dish_European, 'dish_Barmenu': dish_Barmenu, 'dish_Salads': dish_Salads,
            'dish_Breakfasts': dish_Breakfasts, 'dish_Firstcourse': dish_Firstcourse,
            'dish_Lagman': dish_Lagman, 'dish_Pizza': dish_Pizza, 'dish_Eastern': dish_Eastern,
            'dish_Snack': dish_Snack, 'dish_Meat': dish_Meat, 'dish_Panasian': dish_Panasian,
            'dish_Bakery': dish_Bakery, 'dish_Garnish ': dish_Garnish,
            'range_European': range(0, European_result),
            'range_Barmenu': range(0, Barmenu_result),
            'range_Salads': range(0, Salads_result),
            'range_Breakfasts': range(0, Breakfasts_result),
            'range_Firstcourse': range(0, Firstcourse_result),
            'range_Lagman': range(0, Lagman_result),
            'range_Pizza': range(0, Pizza_result),
            'range_Eastern': range(0, Eastern_result),
            'range_Snack': range(0, Snack_result),
            'range_Meat': range(0, Meat_result),
            'range_Panasian': range(0, Panasian_result),
            'range_Bakery': range(0, Bakery_result),
            'range_Garnish': range(0, Garnish_result)

        }
        return render(request, 'index.html', context)

    except:

        context = {'dish_European': dish_European, 'dish_Barmenu': dish_Barmenu, 'dish_Salads': dish_Salads,
                   'dish_Breakfasts': dish_Breakfasts, 'dish_Firstcourse': dish_Firstcourse,
                   'dish_Lagman': dish_Lagman, 'dish_Pizza': dish_Pizza, 'dish_Eastern': dish_Eastern,
                   'dish_Snack': dish_Snack, 'dish_Meat': dish_Meat, 'dish_Panasian': dish_Panasian,
                   'dish_Bakery': dish_Bakery, 'dish_Garnish ': dish_Garnish,
                   'range_European': range(0, European_result),
                   'range_Barmenu': range(0, Barmenu_result),
                   'range_Salads': range(0, Salads_result),
                   'range_Breakfasts': range(0, Breakfasts_result),
                   'range_Firstcourse': range(0, Firstcourse_result),
                   'range_Lagman': range(0, Lagman_result),
                   'range_Pizza': range(0, Pizza_result),
                   'range_Eastern': range(0, Eastern_result),
                   'range_Snack': range(0, Snack_result),
                   'range_Meat': range(0, Meat_result),
                   'range_Panasian': range(0, Panasian_result),
                   'range_Bakery': range(0, Bakery_result),
                   'range_Garnish': range(0, Garnish_result)}
        return render(request, 'index.html', context)


def aboutus(request):
    username = request.user.username
    try:
        user = User.objects.get(username=username)
        data = Client.objects.get(user=user)
        context = {'client': data}
        return render(request, 'aboutus.html', context)

    except:
        user = None
        context = {'client': user}
        return render(request, 'aboutus.html', context)
