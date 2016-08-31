"""Django VIEWS module."""
from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    """Render the home page."""
    return render(request, 'home.html')


def view_list(request, list_id):
    """Render the view list page."""
    _list = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': _list})


def new_list(request):
    """Handler for creating a new list."""
    _list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=_list)
    return redirect('/lists/%d/' % (_list.id,))


def add_item(request, list_id):
    """Handler for adding an item to an existing list."""
    _list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=_list)
    return redirect('/lists/%d/' % (_list.id,))
