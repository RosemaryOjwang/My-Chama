from django.db import models
from django.urls import reverse

# Create your models here.
class Group(models.model):
    groupName = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
                            unique=True)
    
    class Meta:
        ordering = ['groupName']
        indexes = [
            models.Index(fields=['groupName']),
        ]
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return self.groupName
    
    def get_absolute_url(self):
        return reverse('App_bankingSolution:group_list_by_Name',
                       args=[self.slug])
