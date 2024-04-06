from django.shortcuts import render, redirect
from .models import Recipe

# Create your views here.

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