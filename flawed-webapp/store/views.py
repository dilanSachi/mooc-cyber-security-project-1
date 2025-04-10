from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Item, Order
import sqlite3
import logging

logger = logging.getLogger(__name__)

@login_required
def index(request):
    # logger.info("Received request for home page")
    return render(request, 'pages/home.html', {'items': Item.objects.all})

@login_required
def admin(request):
    # logger.info("Received request for admin")
    # if (getattr(User.objects.filter(username=request.user)[0], 'is_staff') != True):
    #     return render(request, 'pages/invalid.html')
    return render(request, 'pages/admin.html')

# 2); update store_item set name=(select password from auth_user where id=1) where item_code=123;--
@login_required
def order(request):
    # logger.info("Received new order: " + str(request.body))
    user_id = getattr(User.objects.filter(username=request.user)[0], 'id')
    sql_statement = "INSERT INTO store_order('user_id', 'item_code_id', 'item_count') VALUES (" + str(user_id) + ", " + str(request.POST.get('item_code')) + ", " + str(request.POST.get('amount')) + ")"
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        cursor.executescript(sql_statement) # use execute with parameterized query option.
        db.commit()
        cursor.close()
    return redirect('/store/')
