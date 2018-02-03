from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Word


class WordList(generic.ListView):
    model = Word

class WordCreate(generic.edit.CreateView):
    model = Word
    fields = ['language', 'category', 'word', 'pronounciation', 'translation']
    success_url = reverse_lazy('wordlist:index')

class WordUpdate(generic.edit.UpdateView):
    model = Word
    fields = ['language', 'category', 'word', 'pronounciation', 'translation']
    success_url = reverse_lazy('wordlist:index')

class WordDelete(generic.edit.DeleteView):
    model = Word
    success_url = reverse_lazy('wordlist:index')
