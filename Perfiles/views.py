from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from Perfiles.forms import AvatarCreateForm, UserUpdateForm
from Perfiles.forms import UserRegisterForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from Perfiles.models import Avatar

# Create your views here.

def register(request):
    mensaje = ""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'BlogApp/success.html', {"mensaje": "Usuario creado con éxito"})
        else:
            mensaje = "Error en los datos ingresados"
    form = UserRegisterForm()
    return render(request, 'register.html', {"form": form, "mensaje": mensaje})

def login_request(request): 
    next_url = request.GET.get('next')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data["username"]
            clave = form.cleaned_data["password"]
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                if next_url:
                    return redirect(next_url)
                return redirect(reverse('inicio'))
            else:
                return render(request, 'login.html', {"form": AuthenticationForm(), "mensaje": "Datos incorrectos"})
        else:
            return render(request, 'login.html', {"form": AuthenticationForm(), "mensaje": "Formulario inválido"})
    form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url =  reverse_lazy('inicio')
    template_name = 'update-user.html'

    def get_object(self, queryset=None):
        return self.request.user

@login_required
def userCreateAvatar(request):
    if request.method == 'POST':
        form = AvatarCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            avatar = form.save()
            avatar.user = request.user
            avatar.save()
            return redirect(reverse('inicio'))  # type: ignore
    form = AvatarCreateForm()
    return render(request, "user_create_avatar.html", {'form': form})

class AvatarUpdateView(LoginRequiredMixin, UpdateView):
    model = Avatar
    fields= ['imagen']
    success_url = reverse_lazy('inicio')
    template_name= "user_create_avatar.html"