
from .utils import code_generator, create_shortcode
from django.db import models

# Create your models here.
class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items = None):
        qs = KirrURL.objects.filter(id__gte=1)
        
        if items is not None and isinstance(items,int):
            qs = qs.order_by('-id')[:items]
            
        new_codes = 0 
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)

### This model is the blueprint to save urls
class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15,unique=True, blank= True)
    updated = models.DateTimeField(auto_now=True) #every time is saved
    timestamp = models.DateTimeField(auto_now_add=True) #when model was created
    active = models.BooleanField(default=True)
    objects = KirrURLManager()
    random = KirrURLManager()
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode =  create_shortcode(self)
        super(KirrURL,self).save(*args,**kwargs)

    def __str__(self): 
        return str(self.url)

    def __unicode__(self):
        return str(self.url)    
