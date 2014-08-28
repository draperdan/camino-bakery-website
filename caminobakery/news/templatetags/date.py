from django import template
from news.models import Story

class StoryYearListNode(template.Node):
	def __init__(self, varname):
		self.varname = varname
	
	def render(self, context):
		context[self.varname] = Story.live.datetimes("pub_date", "year", order='ASC', tzinfo=None).reverse()
		return ''

def do_get_story_year_list(parser, token):
	"""
	Gets a list of years in which stories are published.
	
	Syntax::
	
		{% get_story_year_list as [varname] %}
		
	Example::
	
		{% get_story_year_list as year_list %}
	"""
	bits = token.contents.split()
	if len(bits) != 3:
		raise template.TemplateSyntaxError, "'%s' tag takes two arguements" % bits[0]
	if bits[1] != "as":
		raise template.TemplateSyntaxError, "First arguement to '%s' tag must be 'as'" % bits[0]
	return StoryYearListNode(bits[2])

class StoryMonthListNode(template.Node):
	def __init__(self, varname):
		self.varname = varname
	
	def render(self, context):
		context[self.varname] = Story.live.datetimes("pub_date", "month", order='ASC', tzinfo=None).reverse()
		return ''

def do_get_story_month_list(parser, token):
	"""
	Gets a list of months in which stories are published.
	
	Syntax::
	
		{% get_story_month_list as [varname] %}
		
	Example::
	
		{% get_story_month_list as month_list %}
	"""
	bits = token.contents.split()
	if len(bits) != 3:
		raise template.TemplateSyntaxError, "'%s' tag takes two arguements" % bits[0]
	if bits[1] != "as":
		raise template.TemplateSyntaxError, "First arguement to '%s' tag must be 'as'" % bits[0]
	return StoryMonthListNode(bits[2])
	
register = template.Library()
register.tag('get_story_month_list', do_get_story_month_list)
register.tag('get_story_year_list', do_get_story_year_list)