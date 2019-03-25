from django.contrib import admin

# Register your models here.
from .form import RegModelForm
from .models import Registrado , Maricula, matricula_cn

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email","nombre","timestamp"]  #muestra los campos en el admin
    form = RegModelForm
    #list_display_links = ["nombre"]
    list_filter = ["timestamp"]
    list_editable = ["nombre"]
    search_fields = ["email", "nombre"]

    class Meta:
        model1 = Registrado

class matricula_cn_dis(admin.ModelAdmin):
    list_display = ["matricula", "curso", "nota"]
    class Meta:
        model1 = matricula_cn


admin.site.register(Registrado, AdminRegistrado)
admin.site.register(Maricula)
admin.site.register(matricula_cn,matricula_cn_dis)