from django.db import models

from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(_("title"), max_length=250)
    excerpt = models.TextField(_("excerpt"),null=True)
    slug = models.SlugField(_("slug"), max_length=250,unique_for_date='publish')
    publish = models.DateTimeField(_("publish"), default=timezone.now)
    author = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.CASCADE)
    content = models.TextField(_("content"))
    status = models.CharField(_("status"), max_length=50, choices=options,default='draft')
    objects = models.Manager()
    newmanager = NewManager()

    def get_absolute_url(self):
        return reverse("blog:post_single", args={self.slug})
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-publish',)
