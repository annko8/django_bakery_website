from django.http import HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import redirect, render
from django.urls import reverse
from carts.models import Cart

from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                # messages.success(request, f"{username}, рады видеть Вас снова!")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get("next", None)
                if redirect_page and redirect_page != reverse("user:logout"):
                    return HttpResponseRedirect(request.POST.get("next"))
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {"title": "Login", "form": form}
    return render(request, "users/login.html", context)


def logout(request):
    # messages.success(request, f"{request.user.username}, до скорых встреч!")
    auth.logout(request)
    return redirect(reverse("main:index"))


def registration(request):

    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            # messages.success(request, f"{user.username}, добро пожаловать!")
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    context = {"title": "Registration", "form": form}
    return render(request, "users/registration.html", context)


def profile(request):
    context = {"title": "Profile"}
    return render(request, "users/profile.html", context)
