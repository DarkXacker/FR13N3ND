from aiohttp import request
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render

from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'article/article_list.html'
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'