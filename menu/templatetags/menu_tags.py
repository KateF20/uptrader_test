from django import template

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu_item.html', takes_context=True)
def render_menu(context, category='', parent_id=0):
    current_path = context['request'].path if 'request' in context else ''
    if parent_id != 0:
        menu_list = context['menu_list']
    else:
        all_menu_items = MenuItem.objects.filter(category=category)

        menu_list = []
        for menu_item in all_menu_items:
            is_active = current_path.startswith(menu_item.url)
            is_parent = MenuItem.objects.filter(parent=menu_item).exists()
            menu_list.append({
                'id': menu_item.pk,
                'url': menu_item.url,
                'name': menu_item.name,
                'parent': menu_item.parent_id or 0,
                'is_active': is_active,
                'is_parent': is_parent,
            })

    context = {
        'menu_list': menu_list,
        'menu_level': [item for item in menu_list if item['parent'] == parent_id],
    }

    return context
