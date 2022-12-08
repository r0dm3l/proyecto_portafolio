from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.shortcuts import redirect
from .forms import ProyectForm
from .models import Proyecto
# Create your views here.
class PortafolioView(TemplateView):
    template_name = "portafolio/index.html"
    extra_context = {"proyectos":Proyecto.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["proyectos"] = Proyecto.objects.all()

        return context

class Proyectocreate(FormView):
    model = Proyecto
    template_name = "portafolio/createProyect.html"
    form_class = ProyectForm

    def form_valid(self, form):
        Proyecto.objects.create(**form.cleaned_data)
        return redirect("index")