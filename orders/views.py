from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_protect

from . import models
from . import tools
from . import constants

@csrf_protect
def edit_order(request:HttpRequest) -> HttpResponse:
	id = tools.get_id_order(request)
	if tools.id_validate(id):
		data_for_order = models.get_str_data_order(id)
		table_number_for_order = str(models.Order.objects.filter(id=id).get().table_number)
		context = { 'data_for_order': data_for_order, 'table_number_for_order':table_number_for_order, 'id':id}
	return render(request, "edit_order.html", context)

@csrf_protect
def update_order(request:HttpRequest) -> HttpResponse:
	id = tools.get_id_order(request)
	if tools.id_validate(id):
		table_number = tools.get_table_number(request)
		list_items = tools.get_list_items(request)
		if table_number == -1 or list_items == []:
			return edit_order(request)
		models.Order.objects.filter(id=id).update(table_number=table_number)
		order = models.Order.objects.filter(id=id).get()
		order.items.set(list_items)
		order.save()
	return view_orders(request)

@csrf_protect
def create_order(request:HttpRequest) -> HttpResponse:
	return render(request, "create_order.html")

@csrf_protect
def new_order(request:HttpRequest) -> HttpResponse:
	table_number = tools.get_table_number(request)
	list_items = tools.get_list_items(request)
	if table_number == -1 or list_items == []:
		return view_orders(request)
	models.NewOrder(table_number, list_items)
	return view_orders(request)

@csrf_protect
def search_order(request:HttpRequest) -> HttpResponse:
	id = tools.get_id_order(request)
	if tools.id_validate(id):
		list_orders = models.Order.objects.filter(id=id)
		for order in list_orders:
			order.total_price = models.get_total_price_from_list_items(order.items.all())
			order.items_title = models.list_items_titles_to_str(order.items.all())
		context = { 'list_orders':list_orders}
		return render(request, "view_orders.html", context)
	return view_orders(request)

@csrf_protect
def delete_order(request:HttpRequest) -> HttpResponse:
	id = tools.get_id_order(request) 
	models.Order.objects.filter(id=id).delete()
	return HttpResponseRedirect('/view_orders/')

@csrf_protect
def view_orders(request:HttpRequest) -> HttpResponse:
	list_orders = models.Order.objects.all()
	for order in list_orders:
		order.total_price = models.get_total_price_from_list_items(order.items.all())
		order.items_title = models.list_items_titles_to_str(order.items.all())
	context = { 'list_orders':list_orders}
	return render(request, "view_orders.html", context)
	
@csrf_protect
def calc_profit(request:HttpRequest) -> HttpResponse:
	list_orders = models.Order.objects.all()
	value_summa = 0
	value_complete = 0
	value_in_waiting = 0 
	value_payment_ok = 0
	for order in list_orders:
		if order.status == constants.STATUS_ORDER_COMPLETE:
			value_complete += models.get_total_price_from_list_items(order.items.all())
		elif order.status == constants.STATUS_ORDER_IN_WAITING:
			value_in_waiting += models.get_total_price_from_list_items(order.items.all())
		elif order.status == constants.STATUS_ORDER_PAYMENT_OK:
			value_payment_ok += models.get_total_price_from_list_items(order.items.all())
		value_summa += models.get_total_price_from_list_items(order.items.all())

	
	context = { 
		'value_in_waiting':int(value_in_waiting),
		'value_payment_ok':int(value_payment_ok),
		'value_complete':int(value_complete),
		'value_summa':int(value_summa),
		}
	print(context)
	return render(request, "calc_profit.html", context)

@csrf_protect
def status_order_in_waiting(request:HttpRequest) -> HttpResponse:
	id = tools.get_id_order(request)
	if tools.id_validate(id):models.switch_status_order(id, constants.STATUS_ORDER_IN_WAITING)
	return view_orders(request)

@csrf_protect
def status_order_payment_ok(request:HttpRequest) -> HttpResponse:
	id = tools.get_id_order(request)
	if tools.id_validate(id):models.switch_status_order(id, constants.STATUS_ORDER_PAYMENT_OK)
	return view_orders(request)

@csrf_protect
def status_order_complete(request:HttpRequest) -> HttpResponse:
	id = tools.get_id_order(request)
	if tools.id_validate(id):models.switch_status_order(id, constants.STATUS_ORDER_COMPLETE)
	return view_orders(request)

	