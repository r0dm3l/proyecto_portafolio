from django.shortcuts import render
from django.views.generic import TemplateView, FormView,View
from django.shortcuts import redirect
from .forms import ProyectForm
from .models import *
# Create your views here.

'''class PortafolioView(View):
    def get(self, request):
        proyectos = Proyecto.objects.all()[:100]
        context = {"proyectos":proyectos}
        return render(request, "index.html",context)'''
class PortafolioView(TemplateView):
    template_name = "index.html"
    '''extra_context = {
        "proyectos":Proyecto.objects.all(),
        "Tecnologias":Tecnologia.objects.all(),
        "RedesSociales":RedSocial.objects.all(),
        "Educaciones":Educacion.objects.all(),
        "Idiomas":Idioma.objects.all(),
        "Usuarios":Usuario.objects.all(),
      


        }'''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["proyectos"] = Proyecto.objects.all()
        
        context["tecnologias"]=Tecnologia.objects.all(),
        context["redesSociales"]=RedSocial.objects.all(),
        context["educaciones"]=Educacion.objects.all(),
        context["idiomas"]=Idioma.objects.all(),
        context["usuarios"]=Usuario.objects.all(),
        print(context["idiomas"])
        return context

class Proyectocreate(FormView):
    model = Proyecto
    template_name = 'create.html'
    form_class = ProyectForm
    

    def form_valid(self, form):
        Proyecto.objects.create(**form.cleaned_data)
        return redirect("index")