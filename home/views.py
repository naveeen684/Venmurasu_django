from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from .models import Word
from django.conf import settings
from django.db.models import Q
from django.views.generic import ListView
from .forms import CharForm, IntForm


class HomeView(ListView):
    model = Word
    template_name = 'home/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'words'
    ordering = ['id']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['subtitle'] = 'All Words'
        return context


def Search(request, x):
    if(x == 'starts-with'):
        form = CharForm
        title = 'Starts With'
        legend = 'Letter/Word'
    elif(x == 'word-contains'):
        form = CharForm
        title = 'Word Contains'
        legend = 'Letter/Word'
    elif(x == 'exact-match'):
        form = CharForm
        title = 'Exact Match'
        legend = 'Word'
    elif(x == 'longest'):
        form = IntForm
        title = 'Longest Words'
        legend = 'Limit'
    elif(x == 'smallest'):
        form = IntForm
        title = 'Smallest Words'
        legend = 'Limit'
    elif(x == 'most'):
        form = IntForm
        title = 'Most Frequent'
        legend = 'Limit'
    elif(x == 'least'):
        form = IntForm
        title = 'Least Frequent'
        legend = 'Limit'
    else:
        form = None
        title = '404'
        legend = 'Invalid Keyword'

    context = {
        'form': form,
        'title': title,
        'legend': legend
    }

    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            if title == 'Starts With':
                return redirect('Starts With', form.cleaned_data['word'])
            elif title == 'Word Contains':
                return redirect('Word Contains', form.cleaned_data['word'])
            elif title == 'Exact Match':
                return redirect('Exact Match', form.cleaned_data['word'])
            elif title == 'Longest Words':
                return redirect('Longest Words', n=form.cleaned_data['length'])
            elif title == 'Smallest Words':
                return redirect('Smallest Words', n=form.cleaned_data['length'])
            elif title == 'Most Frequent':
                return redirect('Most Frequent', n=form.cleaned_data['length'])
            elif title == 'Least Frequent':
                return redirect('Least Frequent', n=form.cleaned_data['length'])
            else:
                return redirect('home')
        else:
            return render(request, 'home/form.html', context)
    else:
        return render(request, 'home/form.html', context)


class LongestWordList(ListView):
    model = Word
    template_name = 'home/home.html'
    context_object_name = 'words'
    ordering = ['-length']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        n = self.kwargs.get('n')
        context = super().get_context_data(**kwargs)
        context['title'] = 'Top '+str(n)
        context['subtitle'] = 'Logest Words'
        return context

    def get_queryset(self):
        n = self.kwargs.get('n')
        return Word.objects.all().order_by('-length')[:n]


class MostFrequentWordList(ListView):

    model = Word
    template_name = 'home/home.html'
    context_object_name = 'words'
    ordering = ['-frequency']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        n = self.kwargs.get('n')
        context = super().get_context_data(**kwargs)
        context['title'] = 'Top '+str(n)
        context['subtitle'] = 'Most Frequent'
        return context

    def get_queryset(self):
        n = self.kwargs.get('n')
        return Word.objects.all().order_by('-frequency')[:n]


class SmallestWordList(ListView):

    model = Word
    template_name = 'home/home.html'
    context_object_name = 'words'
    ordering = ['length']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        n = self.kwargs.get('n')
        context = super().get_context_data(**kwargs)
        context['title'] = 'Top '+str(n)
        context['subtitle'] = 'Smallest Words'
        return context

    def get_queryset(self):
        n = self.kwargs.get('n')
        return Word.objects.all().order_by('length')[:n]


class LeastFrequentWordList(ListView):

    model = Word
    template_name = 'home/home.html'
    context_object_name = 'words'
    ordering = ['frequency']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        n = self.kwargs.get('n')
        context = super().get_context_data(**kwargs)
        context['title'] = 'Top '+str(n)
        context['subtitle'] = 'Least Frequent'
        return context

    def get_queryset(self):
        n = self.kwargs.get('n')
        return Word.objects.all().order_by('frequency')[:n]


class SearchWithWordList(ListView):
    model = Word
    template_name = 'home/home.html'
    context_object_name = 'words'
    ordering = ['-length']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        x = self.kwargs.get('x')
        context = super(SearchWithWordList, self).get_context_data(**kwargs)
        context['title'] = 'Exact Match of'
        context['subtitle'] = '\"'+str(x)+'\"'
        return context

    def get_queryset(self):
        x = str(self.kwargs.get('x'))
        print(x)
        return Word.objects.filter(word=x)


class WordContainsWordList(ListView):

    model = Word
    template_name = 'home/home.html'
    context_object_name = 'words'
    ordering = ['-length']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        x = self.kwargs.get('x')
        context = super().get_context_data(**kwargs)
        context['title'] = 'Words Contains'
        context['subtitle'] = '\"'+str(x)+'\"'
        return context

    def get_queryset(self):
        x = self.kwargs.get('x')
        query = Q()
        query = Q(word__icontains=x)
        return Word.objects.filter(query).all()


class StartWithWordList(ListView):

    model = Word
    template_name = 'home/home.html'
    context_object_name = 'words'
    ordering = ['-length']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        x = self.kwargs.get('x')
        context = super().get_context_data(**kwargs)
        context['title'] = 'Words Contains'
        context['subtitle'] = '\"'+str(x)+'\"'
        return context

    def get_queryset(self):
        x = self.kwargs.get('x')
        query = Q()
        query = Q(word__startswith=x)
        return Word.objects.filter(query).all()
