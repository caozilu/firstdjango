from django.shortcuts import render
from django.http import Http404

from inventory.models import Item

def home(request):
	items = Item.objects.all()
	return render(request, 'home.html', {
		'items': items,
	})

def item_detail(request, id):
	try:
		item = Item.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist')
	return render(request, 'item_detail.html', {
		'item': item,
	})