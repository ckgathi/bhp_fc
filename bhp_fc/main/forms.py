from django import forms

from .models import Fixture, Result, SlideShow


class FixtureForm (forms.ModelForm):

    class Meta:
        model = Fixture
        fields = '__all__'


class ResultForm (forms.ModelForm):

    class Meta:
        model = Result
        fields = '__all__'


class SlideShowForm (forms.ModelForm):

    class Meta:
        model = SlideShow
        fields = '__all__'
