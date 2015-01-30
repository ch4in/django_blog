#-*- coding:utf-8 -*-
import datetime
from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from markdown import markdown

class Category(models.Model):
    """A content category"""
    label = models.CharField(blank = True, max_length = 50)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'categories' #定义复数形式

    def __unicode__(self):
        return self.label

#1、2不可见，3、4可见，1.7用get_queryset
VIEWABLE_STATUS = [3, 4]
class ViewableManager(models.Manager):
    def get_queryset(self):
        return super(ViewableManager, self).get_queryset().filter(status__in=VIEWABLE_STATUS)

class Story(models.Model):
    """docstring for Story"""
    STATUS_CHOICES = {
        (1, "Needs Edit"),
        (2, "Needs Approval"),
        (3, "Published"),
        (4, "Archived"),
    }

    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    category = models.ForeignKey(Category)
    markdown_content = models.TextField()
    html_content = models.TextField(editable = False) #不会显示在admin
    owner = models.ForeignKey(User)
    status = models.IntegerField(choices = STATUS_CHOICES, default = 1)
    created = models.DateTimeField(default = datetime.datetime.now)
    modified = models.DateTimeField(default = datetime.datetime.now)

    class Meta:
        ordering = ['modified']
        verbose_name_plural = 'stories' 

    @permalink
    def get_absolute_url(self):
        return ('cms-story', (), {'slug': self.slug})

    #保存到数据库是会执行
    def save(self):
        self.html_content = markdown(self.markdown_content)
        self.modified = datetime.datetime.now()
        super(Story, self).save()

    admin_objects = models.Manager() #default manager
    objects = ViewableManager() #Story.objects
    object_list = ViewableManager() #ListView