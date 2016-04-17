from django.conf.urls import url

from .views import Home, Results, Fixtures, Contact, About, Photos, Players, News

urlpatterns = [
    url(r'^$', Home.as_view(), name='home_url'),
    url(r'^about', About.as_view(), name='about_url'),
    url(r'^contact', Contact.as_view(), name='contact_url'),
    url(r'^results', Results.as_view(), name='results_url'),
    url(r'^fixtures', Fixtures.as_view(), name='fixtures_url'),
    url(r'^photos', Photos.as_view(), name='photos_url'),
    url(r'^players', Players.as_view(), name='players_url'),
    url(r'^news', News.as_view(), name='news_url'),
]
