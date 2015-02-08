from django.shortcuts import render
from django.views.generic.list import ListView
from liveupdate.models import Update
from django.core import serializers
from django.http import HttpResponse

class UpdateListView(ListView):
    model = Update
    def get_context_data(self, **kwargs):
        context = super(UpdateListView, self).get_context_data(**kwargs)
        context['object'] = Update.objects.all()
        return context

def update_after(request, id):
    res = HttpResponse()
    res['Content-Type'] = 'text/javascript'
    res.write(serializers.serialize('json', Update.objects.filter(id__gt=id)))
    return res
