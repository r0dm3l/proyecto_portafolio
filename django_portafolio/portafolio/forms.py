from django import forms
class ProyectForm(forms.Form):
    titulo = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class": "form-control mb-3"}))
    descripcion = forms.CharField(max_length=300,widget=forms.TextInput(attrs={"class": "form-control mb-3"}))
    imagen = forms.URLField(blank=True,widget=forms.TextInput(attrs={"class": "form-control mb-3"}))
    url = forms.URLField(blank=True,widget=forms.TextInput(attrs={"class": "form-control mb-3"}))

