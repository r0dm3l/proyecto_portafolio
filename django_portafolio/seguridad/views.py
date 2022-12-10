from django.shortcuts import render, redirect

from .forms import USerRegisterForm

def page_login(request):
    return render(request, "login.html")


def page_register(request):
    if request.method == "POST":
        form = USerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            #messages.success(request, f"usuario {username} creado")
            return redirect("/portafolio")
    else:
        form = USerRegisterForm()
    context = {"form": form}
    return render(request, "register.html", context)

# Create your views here.
