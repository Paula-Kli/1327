from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

def lists_index(request):
	if not request.user.is_superuser:
		raise PermissionDenied
	return render(request, 'lists_index.html')
