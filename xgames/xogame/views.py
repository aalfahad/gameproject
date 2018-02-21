from django.shortcuts import render, redirect
from .models import Model
from .froms import GameForm

# Create your views here.
def game_list(request):
	context = {
		"games": Game.objects.all()
	}
	return render(request,'game_list.html',context)

def game_detail(request, game_id):
		context = {
		"game": Game.objects.get(id=game_id)
	}
	return render(request,'game_detail.html',context)

def game_create(request):
	form = GameForm()
	if request.method=='POST':
		form= GameForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect("game_list")
	context = {
		"form": form
	}
	return render(request,'game_create.html',context)

def game_update(request, game_id):
	game= Game.objects.get(id=game_id)
	form = GameForm(instance=game)
	if request.method=='POST':
		form= GameForm(request.POST, request.FILES,instance=game)
		if form.is_valid():
			form.save()
			return redirect("game_list")
	context = {
		"game":game,
		"form": form,
	}
	return render(request,'game_update.html',context)

def game_delete(request):
