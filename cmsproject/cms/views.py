from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from cms.models import Story, Category
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class StoryListView(ListView):
    model = Story
    def get_context_data(self, **kwargs):
        context = super(StoryListView, self).get_context_data(**kwargs)
        context['story_list'] = Story.objects.all()
        return context

class StoryDetailView(DetailView):
    model = Story
    def get_context_data(self, **kwargs):
        context = super(StoryDetailView, self).get_context_data(**kwargs)
        context['story_list'] = Story.objects.all()
        return context

def category(request, slug):
    '''Given a category slug, display all items in a category.'''
    category =  get_object_or_404(Category, slug = slug)
    story_list = Story.objects.filter(category = category)
    heading = 'Category: %s' % category.label
    return render(request, 'cms/story_list.html', locals())

def search(request):
    ''' return a list of stories that match the provided search term in either the title or the main content. '''
    if 'q' in request.GET:
        term = str(request.GET['q'])
        story_list = Story.objects.filter(Q(title__contains=term) | Q(markdown_content__contains=term))
        heading = 'Search Results'
    return render(request, 'cms/story_list.html', locals())