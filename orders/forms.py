from . import models 
from . import constants
from django.forms import ModelForm
from django.http import HttpRequest


class BaseMultiForm():
	def get_id(self, request:HttpRequest) -> int:
		'''using first: is_valid()\n
		second step: get_id'''
		if self.is_valid_id(request): return int(request.POST.get(constants.TAG_NAME_HTML_ID_ORDER))
		return None
	
	def get_table_number(self, request:HttpRequest) -> int:
		'''using first: is_valid()\n
		second step: get_table_number'''
		if self.is_valid_table_number(request): return int(request.POST.get(constants.TAG_NAME_HTML_NEW_ORDER_TABLE_NUMBER))
		return None
	
	def get_list_items(self, request:HttpRequest) -> list[models.Item]:
		'''
		convert text from request to array Items from models\n
		data split to row - SYMBOL_SPLIT_TO_ROWS "\\n"\n
		data split to title and price - SYMBOL_SPLIT_TO_NAME_PRICE "' "\n
		'Green Tea' 19.90\\n\n
		[ {title:str('Green Tea'),price:float(19.90)} ]
		'''
		if self.is_valid_items == False: return None

		data_for_order = request.POST.get(constants.TAG_NAME_HTML_NEW_ORDER_LIST_ITEMS, default="")
		data_for_order = data_for_order.strip().split(constants.SYMBOL_SPLIT_TO_ROWS)
		new_items = []
		for line in data_for_order:
			title_item = line.split(constants.SYMBOL_SPLIT_TO_NAME_PRICE)[0][1:].strip()
			price_item = float(line.split(constants.SYMBOL_SPLIT_TO_NAME_PRICE)[1].strip())
			item = models.Item(title=title_item, price=price_item)
			item.save()
			new_items.append(item)
		return new_items

	def is_valid_id(self, request:HttpRequest) -> bool:
		data = request.POST.get(constants.TAG_NAME_HTML_ID_ORDER).strip()
		if data != "":
			if data.isdigit():
				return True
		return False
	
	def is_valid_table_number(self, request:HttpRequest) -> bool:
		data = request.POST.get(constants.TAG_NAME_HTML_NEW_ORDER_TABLE_NUMBER).strip()
		if data != "":
			if data.isdigit():
				if int(data) > 0:
					return True
		return False
	
	def is_valid_items(self, request:HttpRequest) -> bool:
		data = request.POST.get(constants.TAG_NAME_HTML_NEW_ORDER_LIST_ITEMS).strip()
		if len(data.split(constants.SYMBOL_SPLIT_TO_ROWS)) > 0:
			return 	True
		return False

class OrderSearchForm(ModelForm, BaseMultiForm):
	class Meta:
		model = models.Order
		fields = [constants.TAG_NAME_HTML_ID_ORDER]

		
class OrderDeleteForm(ModelForm, BaseMultiForm):
	class Meta:
		model = models.Order
		fields = [constants.TAG_NAME_HTML_ID_ORDER]
	
class OrderEditForm(ModelForm, BaseMultiForm):
	class Meta:
		model = models.Order
		fields = [constants.TAG_NAME_HTML_ID_ORDER]

class OrderUpdateForm(ModelForm, BaseMultiForm):
	class Meta:
		model = models.Order
		fields = [
			constants.TAG_NAME_HTML_NEW_ORDER_TABLE_NUMBER, 
			constants.TAG_NAME_HTML_NEW_ORDER_LIST_ITEMS]

class OrderNewForm(ModelForm, BaseMultiForm):
	class Meta:
		model = models.Order
		fields = [constants.TAG_NAME_HTML_ID_ORDER]
	
class OrderStatusForm(ModelForm, BaseMultiForm):
	class Meta:
		model = models.Order
		fields = [constants.TAG_NAME_HTML_ID_ORDER]

	def switch(self, id:int, status:str) -> None:
		temp_order = models.Order.objects.get(id=id)
		temp_order.status = status
		temp_order.save()
	