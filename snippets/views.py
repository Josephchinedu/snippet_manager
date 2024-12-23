from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Snippet, Tag
from .forms import SnippetForm

# Create your views here.



@login_required
def snippet_list(request):
    snippets = Snippet.objects.filter(user=request.user)
    return render(request, 'snippets/snippet_list.html', {'snippets': snippets})

@login_required
def snippet_detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk, user=request.user)
    return render(request, 'snippets/snippet_detail.html', {'snippet': snippet})

@login_required
def snippet_create(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
            form.save_m2m()
            return redirect('snippet_list')
    else:
        form = SnippetForm()
    return render(request, 'snippets/snippet_form.html', {'form': form})

@login_required
def snippet_edit(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect('snippet_list')
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippets/snippet_form.html', {'form': form})

@login_required
def snippet_delete(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk, user=request.user)
    snippet.delete()
    return redirect('snippet_list')