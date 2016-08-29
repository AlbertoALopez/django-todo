from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    """Render the home page."""
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', '')
    })
