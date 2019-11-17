from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from perfiles.models import Perfil
from perfiles.forms import PerfilForm


def logout_view(request):
	return render(request, 'perfiles/login.html')

@login_required
def perfil_view(request):
	user = User.objects.get(username=request.user)
	perfil = Perfil.objects.filter(user=user.id)
	print(perfil)
	return render(request, 'perfiles/perfil.html', {'perfil':perfil})

def logup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserCreationForm()

	return render(request,'registration/logup.html', {'form':form})

@login_required
def update_profile(request):
	user = User.objects.get(username=request.user)
	perfil = Perfil.objects.filter(user=user.id)

	if request.method == 'POST':
		form = PerfilForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.cleaned_data
			perfil.biografia = data['biografia']
			perfil.sitio_web = data['sitio_web']
			perfil.sexo = data['sexo']
			perfil.telefono = data['telefono']
			perfil.foto_perfil = data['foto_perfil']
			perfil.save()

			return redirect(request, 'perfiles/perfil.html', {'perfil':perfil})

	else:
		form = PerfilForm()

	return render(
		request=request,
		template_name = 'perfiles/update_profile.html',
		context = {
			'perfil': perfil,
			'user':	user,
			'form' : form
			}
		)
