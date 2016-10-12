from datetime import date

from django.views import generic
from django.shortcuts import render
from django.views import View
from bhp_fc.main.models import SlideShow
from .models import Fixture, Result


class Home(View):

    def __init__(self):
        self.context = {}
        self.template_name = 'index.html'
        self.title = 'BHP FC'

    def get(self, request, *args, **kwargs):
        slides = SlideShow.objects.all()
        self.context.update({
            'slides': slides,
        })
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):
        return super(Home, self).get_context_data(**kwargs)


class About(generic.ListView):

    def __init__(self):
        self.context = {}
        self.template_name = 'about.html'
        self.title = 'BHP FC'

    def get(self, request, *args, **kwargs):
        self.context.update({
        })
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):

        return super(Home, self).get_context_data(**kwargs)


class Contact(generic.ListView):

    def __init__(self):
        self.context = {}
        self.template_name = 'contact.html'
        self.title = 'BHP FC'

    def get(self, request, *args, **kwargs):
        self.context.update({
        })
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):

        return super(Home, self).get_context_data(**kwargs)


class Photos(generic.ListView):

    def __init__(self):
        self.context = {}
        self.template_name = 'photos.html'
        self.title = 'BHP FC'

    def get(self, request, *args, **kwargs):
        self.context.update({
        })
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):

        return super(Home, self).get_context_data(**kwargs)


class Fixtures(generic.ListView):

    def __init__(self):
        self.context = {}
        self.template_name = 'fixtures.html'
        self.title = 'BHP FC'

    def get(self, request, *args, **kwargs):
        fixtures = Fixture.objects.all().order_by('game_datetime')
        fixtures_list = []
        for fixture in fixtures:
            if fixture.game_datetime:
                if fixture.game_datetime.date() >= date.today():
                    fixtures_list.append([
                        fixture.bhp_team,
                        fixture.team_agaist,
                        fixture.game_datetime.strftime('%A, %B %d, %Y at %H:%M hours'),
                        fixture.grounds])
        self.context.update({
            'fixtures_list': fixtures_list,
        })
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):

        return super(Home, self).get_context_data(**kwargs)


class Results(generic.ListView):

    def __init__(self):
        self.context = {}
        self.template_name = 'results.html'
        self.title = 'BHP FC'

    def get(self, request, *args, **kwargs):
        results = Result.objects.all().order_by('fixture__game_datetime')
        results_list = []
        win_or_loss = 1
        for result in results:
            if result.bhp_score < result.team_agaist_score:
                win_or_loss = 0
            else:
                win_or_loss = 1
            results_list.append([
                result.fixture.team_agaist,
                result.fixture.grounds,
                result.fixture.game_datetime.strftime('%A, %B %d, %Y at %H:%M hours'),
                result.bhp_score,
                result.team_agaist_score,
                win_or_loss])
        self.context.update({
            'results': results_list,
        })
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):

        return super(Home, self).get_context_data(**kwargs)


class News(generic.ListView):

    def __init__(self):
        self.context = {}
        self.template_name = '404.html'
        self.title = 'BHP FC'

    def get(self, request, *args, **kwargs):
        self.context.update({
        })
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):

        return super(Home, self).get_context_data(**kwargs)


class Players(generic.ListView):

    def __init__(self):
        self.context = {}
        self.template_name = '404.html'
        self.title = 'BHP FC'

    def get(self, request, *args, **kwargs):
        self.context.update({
        })
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render(request, self.template_name, self.context)

    def get_context_data(self, **kwargs):

        return super(Home, self).get_context_data(**kwargs)


def slides():
    images = [
        ['images/slide/Ima.png', 'Ima', 'Before our game against BNSC as Ima warms up for the game.'],
        ['images/slide/fan1.png', 'One of our loyal Fan', 'The team is greatful for our fans attend games, Team Lab representing'],
        ['images/slide/killer4.png', 'Killer4', 'Before our game against BNSC as killer4 warms up for the game.'],
        ['images/slide/mosco.png', 'Skhoza', 'Before our game against BNSC as Skhoza warms up for the game.'],
        ['images/slide/new_kit2.png', 'BHP FC Team, new Kit', 'The team is greatful for the BHP management for sponsoring the team with a kit.'],
        ['images/slide/phil.png', 'Phil', 'Before our game against BNSC as Phil warms up for the game. Also a great goal keeper with the most clean sheets'],
        ['images/slide/sets.png', 'Sets Anderson', 'Before our game against BNSC as Sets Anderson warms up for the game. One of our great defenders'],
        ['images/slide/slider2.png', 'BHP FC on old kit', 'As the team was still grwing on an old kit. Match agaist UB IT at notwane grounds'],
        ['images/slide/SirOne.png', 'SirOne', 'Before our game against BNSC as SirOne warms up for the game. Still on injury, we await his return to the grounds.'],
        ['images/slide/keeper.png', 'Kepper', 'Before our game against BNSC as Keeper warms up for the game. Also a great goal keeper'],
        ['images/slide/mogwele.png', 'Mogwele', 'Before our game against BNSC as Mogwele warms up for the game.'],
        ['images/slide/new_kit1.png', 'BHP FC Team, new Kit', 'The team is greatful for the BHP management for sponsoring the team with a kit.'],
        ['images/slide/nkozana.png', 'Nkozana', 'Before our game against BNSC as Nkozana warms up for the game.'],
        ['images/slide/roni.png', 'Ronald', 'Before our game against BNSC as Roni warms up for the game.'],
        ['images/slide/slider1.png', 'BHP FC on old kit', 'As the team was still grwing on an old kit. Match agaist UB IT at notwane grounds'],
        ['images/slide/slider3.png', 'BHP FC on old kit', 'As the team was still grwing on an old kit. Match agaist UB IT at notwane grounds'],
        ['images/slide/keeper-weddings.png', 'Keeper Install Wife 1.0', 'Congratulations to our goal keeper for successful installation of wife 1.0. We wish you all the best and take good care of your wife Sir. Please always apply for Visa well in advance. We are waiting for your return to the grounds'],]
    for image in images:
        if not SlideShow.objects.filter(image_name=image[0]):
            SlideShow.objects.create(
                image_name=image[0],
                image_title=image[1],
                pic_discription=image[2])
