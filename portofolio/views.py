from django.shortcuts import render
# Importar los objetos del proyecto
from .models import Project

# Create your views here.
def home(request):
	# Generar una lista con los objetos
	projects = Project.objects.all() 
	return render(request, 'portofolio/home.html', {'projects':projects})