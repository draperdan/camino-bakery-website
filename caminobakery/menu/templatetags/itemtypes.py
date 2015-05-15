from django import template
from menu.models import ItemType


class ItemTypeListNode(template.Node):
    def __init__(self, varname):
        self.varname = varname

    def render(self, context):
        context[self.varname] = ItemType.objects.all()
        return ''


def do_get_itemtype_list(parser, token):
    """
    Gets a list of all item types, and passes it into a custom variable.

    Syntax::

        {% get_itemtype_list as [varname] %}

    Example::

        {% get_itemtype_list as itemtype_list %}
    """
    bits = token.contents.split()
    if len(bits) != 3:
        raise template.TemplateSyntaxError, "'%s' tag takes two arguements" % bits[0]
    if bits[1] != "as":
        raise template.TemplateSyntaxError, "First arguement to '%s' tag must be 'as'" % bits[0]
    return ItemTypeListNode(bits[2])

register = template.Library()
register.tag('get_itemtype_list', do_get_itemtype_list)
