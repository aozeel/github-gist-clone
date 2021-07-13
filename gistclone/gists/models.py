from django.db import models
from pygments.formatters.html import HtmlFormatter

# Create your models here.

class Gist(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank= False)
    description = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField(blank=True,default='')
    owner = models.ForeignKey('auth.User', related_name='gists', on_delete=models.CASCADE)


    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        """
        Use the 'pygments' library to create a highlighted HTML
        representation of the code snippet
        """
        super(Gist,self).save(*args, **kwargs)

