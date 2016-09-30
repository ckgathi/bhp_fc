from django.contrib import admin

from .models import Fixture, Result, SlideShow

from .forms import FixtureForm, ResultForm, SlideShowForm


class FixtureAdmin(admin.ModelAdmin):

    form = FixtureForm
    fields = ['bhp_team', 'team_agaist', 'game_datetime', 'grounds']

admin.site.register(Fixture, FixtureAdmin)


class ResultAdmin(admin.ModelAdmin):

    form = ResultForm
    fields = ['fixture', 'bhp_score', 'team_agaist_score']

admin.site.register(Result, ResultAdmin)


class SlideShowAdmin(admin.ModelAdmin):

    form = SlideShowForm
    fields = ['image_name', 'image_title', 'pic_discription']

admin.site.register(SlideShow, SlideShowAdmin)
