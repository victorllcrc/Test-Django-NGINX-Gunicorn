from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .form import RegModelForm, ContactForm, MatriculaForm

from django.contrib.auth import authenticate,login
from .models import Registrado, Maricula, matricula_cn
from tercero.models import anio_academico, alumno, grado ,institucion, curso, matricula


# Create your views here.
def inicio(request):
    titulo = "HOLA"
    if request.user.is_authenticated: #para verificar si estas logeado
        titulo = "Bienvenido %s " %(request.user)

    # FORMULARIOS EN RegForm form =RegForm(request.POST or None)
    form = RegModelForm(request.POST or None)
   # print(dir(form)) // para ver los comandos que se puede añadir al FOMR

    context = {
        "titulo": titulo,
        "el_form": form,  # es el nombre que se da para ser llamada en la plantilla de html
    }

    if form.is_valid():

        '''*******Cuando utilizamos RegForm-**********
        print (form.cleaned_data) #mire la consola
        # imprime los datos de manera limpia ... mire la consola
        form_data = form.cleaned_data
        abc = form_data.get("email")
        abc1 = form_data.get("nombre")
        obj = Registrado.objects.create(email=abc, nombre=abc1)
        '''

        #********* Cuando utilizamos RegModelForm**********
        instance = form.save(commit=False)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")

        if not instance.nombre:
            instance.nombre = "PERSONA"

        instance.save()
        context = {
            "titulo": "Gracias %s!" %(nombre)
        }

        if not nombre:
            context = {
                "titulo": "Gracias %s" %(email)
            }
        print(instance)
        print(instance.timestamp)


    return render(request,"inicio.html", context)

# lo que estamos llamando en especifico


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_nombre = form.cleaned_data.get("nombre")
        form_mensaje = form.cleaned_data.get("mensaje")
        asunto = 'hola esto es una prueba'
        email_from =settings.EMAIL_HOST_USER
        email_to = ["victorllcrc@gmail.com",]
        email_mensaje = "Ella no te ama"
        send_mail(asunto,
                  email_mensaje,
                  email_from,
                  email_to,
                  fail_silently=False,
                  )
        #for key, value in form.cleaned_data.items():
        #   print(key, value)

    context = {
        "form": form,
    }

    return render(request, "forms.html", context)



#******PARA LOGIN*****



def login(request):
    context ={

    }

    return render(request,"login.html", context)

'''
def matricula (request):

    if request.method == "POST":
        form = MatriculaForm(request.POST)
        if form.is_valid():
            fdni = form.cleaned_data.get("Dni") # devuelve el valor encriptado

            alumno = Maricula.objects.get(dni=fdni) # el metodo post devuelve un setQuery una especie de diccionrario


    else:
        form = MatriculaForm(request.POST)
        alumno = ""


    context = {
        'form2': form,
        'alumno': alumno,
    }
    return render(request, "asd.html",context)
'''
def matricula (request):

    if request.method == "POST":
        form = MatriculaForm(request.POST)
        if form.is_valid():
            fdni = form.cleaned_data.get("Dni") # devuelve el valor encriptado

            alumno = matricula_cn.objects.filter(matricula__alumno__dni=fdni)
            data=alumno[0].matricula_id

            data1 = matricula.object.get(pk=data)
            print(data1)
            print("hola")
            for e in alumno:
                print(e.matricula_id)


    else:
        form = MatriculaForm(request.POST)
        alumno = ""


    context = {
        'form2': form,
        'alumno': alumno,

    }
    return render(request, "asd.html",context)