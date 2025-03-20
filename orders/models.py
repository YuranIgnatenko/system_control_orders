from django.db import models
from .constants import *
from . import constants

# python manage.py makemigrations orders && python manage.py migrate orders

class Item(models.Model):
	title = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	def __str__(self):
		return f"'{self.title}' {self.price}\n"

class Order(models.Model):
	table_number = models.IntegerField()
	items = models.ManyToManyField(Item)
	status = models.CharField(max_length=10, default=STATUS_ORDER_IN_WAITING)
	total_price = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		result_str = ""
		for item in self.items.all():
			result_str += str(item)
		self.description = result_str.strip()
		print(self.description)
		return result_str.strip()
	
def NewOrder(table_number:int, list_items:list[Item]):
	order = Order(table_number=table_number,
			   status=constants.STATUS_ORDER_IN_WAITING)
	order.total_price = get_total_price_from_list_items(list_items)
	order.save()
	order.items.set(list_items)

def get_total_price_from_list_items(list_items:list[Item]) -> float:
	'''get summa all fields 'price' from items list'''
	return sum([float(item.price) for item in list_items])

def get_str_data_order(id:int) -> str:
	order = Order.objects.filter(id=id).get()
	result_str = ""
	for item in order.items.all():
		result_str += str(item)
	return result_str.strip()

def list_items_titles_to_str(list_items:list[Item]) -> str:
	'''
	get and join fields 'title' from all items\n
	using join symbol from var (SYMBOL_JOIN_TITLES_ITEMS = ", ")\n
	[ {title:str('Green Tea'), price:float(11.00)}, \n
	 {title:str('Black Tea'), price:float(12.10)} ]
	Green Tea, Black Tea
	'''
	return SYMBOL_JOIN_TITLES_ITEMS.join([item.title for item in list_items])



def switch_status_order(id:int, status:str):
	temp_order = Order.objects.get(id=id)
	temp_order.status = status
	temp_order.save()
