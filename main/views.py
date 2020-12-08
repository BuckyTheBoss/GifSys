from django.shortcuts import render, redirect, get_object_or_404
from .models import Gif, Category
from .forms import GifForm


# Create your views here.
def add_gif(request):
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            gif = Gif.objects.create(
                title=form.cleaned_data['title'],
                url=form.cleaned_data['url'],
                uploader_name=form.cleaned_data['uploader_name'],
            )
            for cat in form.cleaned_data['categories']:
                cat.gifs.add(gif)
            return redirect('view_gif', gif.id)
    return render(request, 'add_gif.html', {'form': GifForm()})


def view_gif(request, id):
    gif = get_object_or_404(Gif, pk=id)
    return render(request, 'show_gif.html', {'gif':gif})


def view_category(request, id):
    category = get_object_or_404(Category, pk=id)
    context = {
        'gif_list': category.gifs.all(),
        'page_title': f'{category.name} GIF\'s',
        'page_heading': f'all GIF\'s of the category {category.name}:'
    }
    return render(request, 'show_gifs.html', context)


def view_categories(request):
    cats = Category.objects.all()
    return render(request, 'show_categories.html', {'categories': cats})


def homepage(request):
    context = {
        'gif_list': Gif.objects.all(),
        'page_title': 'Homepage',
        'page_heading': 'Our GIF\'s'
    }
    return render(request, 'show_gifs.html', context)


def like_gif(request, id, mode):
    gif = get_object_or_404(Gif, pk=id)
    gif.likes += 1 if mode else -1
    gif.save()
    return redirect('view_gif', gif.id)


def view_gifs_by_like(request):
    context = {
        'gif_list': Gif.objects.filter(likes__gte=1).order_by('likes'),
        'page_title': 'Trending',
        'page_heading': 'Not hated GIF\'s'
    }
    return render(request, 'show_gifs.html', context)