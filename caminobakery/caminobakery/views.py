from django.views.generic import TemplateView
from specials.models import Special
from hours.models import Schedule
from menu.models import Item, ItemType

class HomePageView(TemplateView):
	
	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		context['special_list'] = Special.today.all()
		context['hours_list'] = Schedule.objects.all()
		return context

class RobotsView(TemplateView):
	
	template_name = "robots.txt"
	
	def render_to_response(self, context, **kwargs):
		return super(RobotsView, self).render_to_response(context, content_type='text/plain', **kwargs)