from django.http import HttpRequest

from .models import Item, Order
from .constants import *
from .validations import *

def get_list_items(request:HttpRequest) -> list[Item]:
	print(validate_request_list_items(request))
	if validate_request_list_items(request):
		return request_to_list_items(request)
	return []

def get_table_number(request:HttpRequest) -> int:
	if validate_request_table_number(request):
		return request_to_table_number(request)
	return -1

def get_id_order(request:HttpRequest) -> int:
	if validate_request_id_order(request):
		return request_to_id_order(request)
	return -1

def request_to_list_items(request:HttpRequest) -> list[Item]:
	'''
	convert text from request to array Items from models\n
	data split to row - SYMBOL_SPLIT_TO_ROWS "\\n"\n
	data split to title and price - SYMBOL_SPLIT_TO_NAME_PRICE "' "\n
	'Green Tea' 19.90\\n\n
	[ {title:str('Green Tea'),price:float(19.90)} ]
	'''
	data_for_order = request.POST.get(TAG_NAME_HTML_NEW_ORDER_LIST_ITEMS, default="")
	data_for_order = data_for_order.strip().split(SYMBOL_SPLIT_TO_ROWS)
	new_items = []
	for line in data_for_order:
		print(line)
		title_item = line.split(SYMBOL_SPLIT_TO_NAME_PRICE)[0][1:].strip()
		price_item = float(line.split(SYMBOL_SPLIT_TO_NAME_PRICE)[1].strip())
		item = Item(title=title_item, price=price_item)
		item.save()
		new_items.append(item)
	return new_items

def request_to_table_number(request:HttpRequest) -> int:
	'''convert text from request to int (for field table_number in model Item)'''
	return int(request.POST.get(TAG_NAME_HTML_NEW_ORDER_TABLE_NUMBER, default=""))

def request_to_id_order(request:HttpRequest) -> int:
	'''get id from request and convert to int (orders ID)'''
	return int(request.POST.get(TAG_NAME_HTML_ID_ORDER, default=-1))
