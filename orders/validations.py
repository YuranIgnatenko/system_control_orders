from django.http import HttpRequest

from .constants import *

def validate_request_list_items(request:HttpRequest) -> bool:
	data = request.POST.get(TAG_NAME_HTML_NEW_ORDER_LIST_ITEMS, default="").strip()
	print(f">{data}<")
	if len(data.split(SYMBOL_SPLIT_TO_ROWS)) > 0:
		return 	True
	return False

def validate_request_table_number(request:HttpRequest) -> bool:
	data = request.POST.get(TAG_NAME_HTML_NEW_ORDER_TABLE_NUMBER, default="").strip()
	if data != "":
		if data.isdigit():
			return True
	return False

def validate_request_id_order(request:HttpRequest) -> bool:
	data = request.POST.get(TAG_NAME_HTML_ID_ORDER, default="").strip()
	if data != "":
		if data.isdigit():
			return True
	return False

def id_validate(id:int) -> bool:
	if id != -1: return True
	return False