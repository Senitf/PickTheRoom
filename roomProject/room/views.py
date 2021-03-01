from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from room.forms import SearchForm
from room.models import *
from room.funcs import crawling

class Index(generic.TemplateView):
    template_name = 'room/index.html'


class SearchView(generic.View):
    post_template_name = 'room/result.html'
    get_template_name = 'room/search.html'
    form_class = SearchForm

    def post(self, request):
        result = request.POST
        form = self.form_class(request.POST)
        context = {
            'result': result
        }
        if form.is_valid():
            return render(request, self.post_template_name, context)
        else:
            return render(request, self.get_template_name, context)

    def get(self, request):
        result = request.GET
        context ={
            'result' : result
        }
        return render(request, self.get_template_name, context)


class ScrapListView(generic.ListView):
    template_name = 'room/scrap.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, '로그인이 필요합니다')
            return HttpResponseRedirect('/accounts/login/')
        return super(ScrapListView, self).dispatch(request, *args, **kwargs)