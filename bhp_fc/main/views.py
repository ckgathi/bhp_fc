from django.views import generic
from django.shortcuts import render_to_response
from django.template import RequestContext


class Home(generic.ListView):

    def __init__(self):
        self.context = {}
        self.template_name = 'index.html'
        self.title = 'BHP FC'

    def get(self, request, *args, **kwargs):
        self.context.update({
        })
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

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
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

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
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

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
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

    def get_context_data(self, **kwargs):

        return super(Home, self).get_context_data(**kwargs)


class Fixtures(generic.ListView):

    def __init__(self):
        self.context = {}
        self.template_name = 'fixtures.html'
        self.title = 'BHP FC'

    def get(self, request, *args, **kwargs):
        self.context.update({
        })
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

    def get_context_data(self, **kwargs):

        return super(Home, self).get_context_data(**kwargs)


class Results(generic.ListView):

    def __init__(self):
        self.context = {}
        self.template_name = 'results.html'
        self.title = 'BHP FC'

    def get(self, request, *args, **kwargs):
        self.context.update({
        })
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

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
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

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
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        self.context.update({
            'title': self.title
        })
        return render_to_response(self.template_name, self.context, context_instance=RequestContext(request))

    def get_context_data(self, **kwargs):

        return super(Home, self).get_context_data(**kwargs)
