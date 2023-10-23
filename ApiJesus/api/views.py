from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.http import HttpRequest
from django.http import HttpResponse
from .forms import Registro_Form
from .forms import register as registros
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import send_mail



#@login_required

class Home (APIView):
    template_name="login.html"
    def get(self, request):
        return render(request,self.template_name)
    
class index (APIView):
    template_name="index.html"
    def get(self, request):
        return render(request,self.template_name)
    
class login (APIView):
    template_name="login.html"
    def get(self, request):
        return render(request,self.template_name)
    
class icono (APIView):
    template_name="icons.html"
    def get(self, request):
        return render(request,self.template_name)
    
class blank (APIView):
    template_name="blank.html"
    def get(self, request):
        return render(request,self.template_name)
    
class buttons (APIView):
    template_name="buttons.html"
    def get(self, request):
        return render(request,self.template_name)

class flot (APIView):
    template_name="flot.html"
    def get(self, request):
        return render(request,self.template_name)

class forms (APIView):
    template_name="forms.html"
    def get(self, request):
        return render(request,self.template_name)
    
class grid (APIView):
    template_name="grid.html"
    def get(self, request):
        return render(request,self.template_name)
    
class morris (APIView):
    template_name="morris.html"
    def get(self, request):
        return render(request,self.template_name)
    
class notifications (APIView):
    template_name="notifications.html"
    def get(self, request):
        return render(request,self.template_name)
    
class panels (APIView):
    template_name="panels-wells.html"
    def get(self, request):
        return render(request,self.template_name)
    
class tables (APIView):
    template_name="tables.html"
    def get(self, request):
        return render(request,self.template_name)
    
class typography (APIView):
    template_name="typography.html"
    def get(self, request):
        return render(request,self.template_name)
    
class forgot (APIView):
    template_name="forgot-password.html"
    def get(self, request):
        return render(request,self.template_name)
    
class register(APIView):
    template_name="register.html"
    def get(self, request):
        return render(request,self.template_name)
    

class RegistroUsuarioView(HttpRequest):
    def index(request):
        Usuario = Registro_Form
        return render(request, "register.html", {"form":Usuario})
    def procesar_formulario(request):
        Usuario = Registro_Form(request.POST)
        if Usuario.is_valid():
            Usuario.save()
            Usuario = Registro_Form()
        return render(request, "login.html", {"form":Usuario, "mensaje":"OK"})


def register(request):
    if request.method == 'POST':
        form = registros(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
            'Bienvenido',    # Asunto del correo
            'Felicidades te has registrado con exito',    # Cuerpo del correo
            'jesus480@gmail.com',   # Dirección de correo remitente
            [request.POST['email']],  # Lista de direcciones de correo de destinatarios
            fail_silently=False,     # Si se establece en True, los errores en el envío de correo no generarán una excepción
            )
            
            return redirect('login')   
    else: 
        form = registros()
        
    context = { 'form' : form}
    return render(request, 'register.html', context) 
    


 
        

    
#def salir(request):
#    logout(request)
#    return redirect('login')

#def iniciar_sesion(request):
#    if request.method == 'POST':
#        correo1 = request.POST['username']
#        contra1 = request.POST['password']
        
       
#        user = authenticate(request, username=correo1, password=contra1)
       
#        if user is not None:
#            login(request, user)
#            print("acceso ")
#            return redirect('index.html')
            
        
#        else:
#             error_message = 'Credenciales incorrectas. Inténtalo de nuevo.'
#             print("sin acceso")
#             return render(request, 'login.html', {'error_message': error_message})
             
             
#    return render(request, 'login.html')