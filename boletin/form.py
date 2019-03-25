from django import forms
from .models import Registrado

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre", "email"]

    # Estas son alas validaciones para los campos respectivos
    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveeder = email.split("@")
        dominio, extension = proveeder.split(".")
        if not  extension == "edu":
            raise forms.ValidationError("Por favor utiliza un email con la extension .edu")
        return email

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        return nombre


''''********* lo comentamos
class RegForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
'''

class ContactForm(forms.Form):
    nombre = forms.CharField(required=False)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)


class MatriculaForm(forms.Form):
    Dni = forms.CharField(max_length=10,  required= False)








