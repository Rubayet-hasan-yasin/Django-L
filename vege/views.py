from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login")
def recipes(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("recipe_name")
        description = data.get("recipe_description")
        image = request.FILES.get("recipe_image")

        Recipe.objects.create(
            recipe_name = name,
            recipe_description = description,
            recipe_image = image
        )

        return redirect("/recipes")
    
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get("search"))

    context = {"recipes": queryset}
    
    return render(request, 'recipe.html', context)


def Delete_recipes(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect("/recipes")

def Update_recipes(request, id):
    queryset = Recipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        name = data.get("recipe_name")
        description = data.get("recipe_description")
        image = request.FILES.get("recipe_image")

        queryset.recipe_name = name
        queryset.recipe_description = description
        
        if image:
            queryset.recipe_image= image
        
        queryset.save()
        return redirect("/recipes")


    context = {"recipe": queryset}

    return render(request, "update_recipes.html", context)


def Login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")


        user = User.objects.filter(username= username)

        if not user.exists():
            messages.info(request, "Invalid Username")
            return redirect("/login")
        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, "Invalid Password")
            return redirect("/login")
        else:
            login(request, user)
            return redirect("/recipes")


    return render(request, "login.html")


def Logout_page(request):
    logout(request)
    return redirect("/login")


def Register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")


        user = User.objects.filter(username= username)

        if user.exists():
            messages.info(request, "username alredy taken")
            return redirect("/register")

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Register success")
        return redirect("/login")


    return render(request, "register.html")