from django.shortcuts import render, redirect
from .form import registration_form, CustomUserCreationForm
from .models import Student
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home(request):
    template_name = "student_management_system_app/home.html"
    return render(request, template_name)


@login_required(login_url="login")
def registration(request):
    if request.method == "POST":
        form = registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("data")
    form = registration_form()
    template_name = "student_management_system_app/registration.html"
    context = {"form": form}
    return render(request, template_name, context)


@login_required(login_url="login")
def data(request):
    stu = Student.objects.all()  # orm(object relational mapping)
    template_name = "student_management_system_app/data.html"
    context = {"stu": stu}
    return render(request, template_name, context)


def logged(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Credential!")
        else:
            login(request, user)
            send_mail(
                "Subject here",
                "Here is the message.",
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            return redirect("registration")
    template_name = "student_management_system_app/login.html"
    return render(request, template_name)


def signup(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    template_name = "student_management_system_app/signup.html"
    context = {"form": form}
    return render(request, template_name, context)


def remove(request, id):
    stu = Student.objects.get(id=id)
    stu.delete()
    return redirect("data")


def Log_Out(request):
    logout(request)
    return redirect("login")
