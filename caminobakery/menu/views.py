from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from .models import ItemTypeGroup, BreadSchedule, Day, ItemType

class AlcoholView(ListView):
	""" View to display wine and beer items based on their item type. """

	context_object_name = "alcohol_list"
	queryset = ItemType.objects.filter(itemtypegroup__title__exact="Wine & Beer")
	template_name = "menu/alcohol_list.html"

	def get_context_data(self, **kwargs):
		context = super(AlcoholView, self).get_context_data(**kwargs)
		context['alcohol_group'] = ItemTypeGroup.objects.get(title__exact="Wine & Beer")
		return context

class CakesView(ListView):
	""" View to display all cake items based on their item type. """

	context_object_name = "cake_list"
	queryset = ItemType.objects.filter(itemtypegroup__title__exact="Cakes")
	template_name = "menu/cake_list.html"

	def get_context_data(self, **kwargs):
		context = super(CakesView, self).get_context_data(**kwargs)
		context['cake_group'] = ItemTypeGroup.objects.get(title__exact="Cakes")
		return context

class CateringView(ListView):
	""" View to display all catering items based on their item type. """

	context_object_name = "catering_list"
	queryset = ItemTypeGroup.objects.filter(title__exact="Catering")
	template_name = "menu/catering_list.html"

	def get_context_data(self, **kwargs):
		context = super(CateringView, self).get_context_data(**kwargs)
		context['catering_group'] = ItemTypeGroup.objects.get(title__exact="Catering")
		return context

class ItemListView(ListView):
	""" View to display all live items excluding cakes and catering. """

	context_object_name = "item_list"
	queryset = ItemTypeGroup.objects.all().exclude(item_types__title__contains="Cakes").exclude(item_types__title__contains="Catering").exclude(item_types__title__contains="Bread").exclude(title__exact="Wine & Beer")
	template_name = "menu/item_list.html"

class SandwichView(ListView):
	""" View to display sandwichs. """

	context_object_name = "sandwich_list"
	queryset = ItemType.objects.all().filter(title__contains="Sandwiches")
	template_name = "menu/sandwich_list.html"

	def get_context_data(self, **kwargs):
		context = super(SandwichView, self).get_context_data(**kwargs)
		context['sandwich_type'] = ItemType.objects.get(title__exact="Sandwiches")
		return context
	
class BreadView(ListView):
	""" View to display the bread list and schedule. """

	context_object_name = "bread_list"
	queryset = ItemType.objects.all().filter(title__exact="Bread")
	template_name = "menu/bread_list.html"

	def get_context_data(self, **kwargs):
		context = super(BreadView, self).get_context_data(**kwargs)
		context['day_list'] = Day.objects.all()
		context['breadschedule'] = BreadSchedule.objects.all()
		context['bread_type'] = ItemType.objects.get(title__exact="Bread")
		return context