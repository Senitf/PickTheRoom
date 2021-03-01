from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages
from urllib.parse import urlparse
from room.forms import SearchForm
from room.models import *
from room.funcs import *

class Index(generic.TemplateView):
    template_name = 'room/index.html'


class SearchView(generic.View):
    post_template_name = 'room/result.html'
    get_template_name = 'room/search.html'
    form_class = SearchForm

    def post(self, request):
        result = request.POST
        form = self.form_class(request.POST)

        if form.is_valid():
            _input = [int(result['distance']), int(result['charge']), int(result['rating'])]
            room_list = Room.objects.filter(region = result['region'])
            for room in room_list:
                score = [room.distance_score, room.charge_score, room.rating_score]
                room.SAW_score = calc(set_weight(_input), score)
                room.save()

            if request.user.is_authenticated:
                context = {
                    'result': result,
                    'rooms': Room.objects.filter(region = result['region'])[0:3],
                    'scraps': request.user.scrap.all()
                }
            else:
                context = {
                    'result': result,
                    'rooms': Room.objects.filter(region = result['region'])[0:3]
                }

            return render(request, self.post_template_name, context)
        else:
            context = {
                'result': result
            }
            return render(request, self.get_template_name, context)

    def get(self, request):
        result = request.GET
        context ={
            'result' : result
        }
        return render(request, self.get_template_name, context)


class Scrap(generic.View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, '로그인이 필요합니다')
            return HttpResponseRedirect('/accounts/login/')
        else:
            room = Room.objects.get(pk=kwargs['pk'])
            if request.user in room.scrap.all():
                room.scrap.remove(request.user)
            else:
                room.scrap.add(request.user)
            return HttpResponseRedirect('/room/scraplist/')


class ScrapListView(generic.ListView):
    model = Room
    context_object_name = 'scraplist'
    template_name = 'room/scraplist.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, '로그인이 필요합니다')
            return HttpResponseRedirect('/accounts/login/')
        return super(ScrapListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.scrap.all()


class RoomListView(generic.ListView):
    model = Room
    context_object_name = 'roomlist'
    template_name = 'room/roomlist.html'

    def post(self, request):
        result = request.POST
        if request.user.is_authenticated:
            context = {
            'result': result,
            'roomlist': Room.objects.filter(region = result['region']),
            'scraps': request.user.scrap.all()
        }
        else:
            context = {
                'result': result,
                'roomlist': Room.objects.filter(region = result['region'])
            }
        return render(request, self.template_name, context)

    def get(self, request):
        def get_queryset(self):
            return Room.objects.filter(region = result['region'])


class Crawler(generic.View):
    def get(self, request):
        room_list = crawling('서울')

        for idx in room_list:
            new_content = Room()
            new_content.region = '서울'
            new_content.title = idx[0]
            if idx[1] == '':
                new_content.rating = 0.0
            else:
                new_content.rating = float(idx[1])
            new_content.distance = idx[2]
            new_content.charge = int(idx[3].replace(",",""))
            new_content.image = idx[4]

            #score 계산
            if new_content.distance.find('km') == -1:
                new_content.distance_score = 5
            else:
                start = new_content.distance.find('km') - 3
                end = new_content.distance.find('km')
                distance = float(idx[3][start:end])
                if distance > 1.8:
                    new_content.distance_score = 1
                elif distance > 1.5:
                    new_content.distance_score = 2
                elif distance > 0.9:
                    new_content.distance_score = 3
                elif distance > 0.6:
                    new_content.distance_score = 4
                else:
                    new_content.distance_score = 5

            if new_content.charge == '' or new_content.charge > 60000:
                new_content.charge_score = 1
            elif new_content.charge > 50000:
                new_content.charge_score = 2
            elif new_content.charge > 40000:
                new_content.charge_score = 3
            elif new_content.charge > 30000:
                new_content.charge_score = 4
            else:
                new_content.charge_score = 5

            if new_content.rating == '' or new_content.rating < 7.2:
                new_content.rating_score = 1
            elif new_content.rating < 7.8:
                new_content.rating_score = 2
            elif new_content.rating < 8.2:
                new_content.rating_score = 3
            elif new_content.rating < 9.0:
                new_content.rating_score = 4
            else:
                new_content.rating_score = 5

            new_content.save()

        return HttpResponseRedirect('/room/')