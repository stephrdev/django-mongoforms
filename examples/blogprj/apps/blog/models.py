import datetime

from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

from mongoengine import *

class BlogPost(Document):
    published = BooleanField(default=False)
    author = StringField(required=True)
    title = StringField(required=True)
    slug = StringField()
    content = StringField(required=True)
    
    datetime_added = DateTimeField(default=datetime.datetime.now)
    
    def save(self):
        if self.slug is None:
            slug = slugify(self.title)
            new_slug = slug
            c = 1
            while True:
                try:
                    BlogPost.objects.get(slug=new_slug)
                except BlogPost.DoesNotExist:
                    break
                else:
                    c += 1
                    new_slug = '%s-%s' % (slug, c)
            self.slug = new_slug
        return super(BlogPost, self).save()
    
    def get_absolute_url(self):
        #return u'%s/' % self.slug
        return reverse('apps.blog.views.show', kwargs={'slug': self.slug})
    
    @queryset_manager
    def published_posts(doc_cls, queryset):
        return queryset(published=True)

    meta = {
        'ordering': ['-datetime_added']
    }