from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Game

def index(request):

    return HttpResponse("Hello, world. You're at the games admin index.")

#def get_data(request):
 # mydata = Game.objects.all()
  #context = {
   # 'mymembers': mydata,
  #}
  #return render(request, 'games.html', context)
  
def get_data(request):
    if request.method == 'POST':
        data = request.POST
        game_ID = data.get('game_ID')
        game_name = data.get('game_name')
        genre = data.get('genre')

        Game.objects.create(
            game_ID=game_ID,
            game_name=game_name
            genre=genre,
        )
        return redirect('/')

    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get('search'))

    context = {'recipes': queryset}
    return render(request, 'recipes.html', context)