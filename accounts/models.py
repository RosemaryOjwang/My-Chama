from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
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

class Add_Members(models.Model):
    user = models.ForeignKey(User, 
                             related_name='group_user',
                             on_delete=models.CASCADE)
    groupName = models.ForeignKey(Group,
                                 related_name='group',
                                 on_delete=models.CASCADE)
    memberName = models.CharField(max_length=255)
    slug = models.SlugField(max_length=155) 
    thumbnail = models.ImageField(upload_to='img', blank=True)
    
    occupation = models.CharField(max_length=1000)
    
    available = models.BooleanField(default=True)
    member_contact = models.DecimalField(max_digits=10,
                                         decimal_places=0)
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-joined']
        
    def __str__(self):
        return self.memberName
    
    def get_absolute_url(self):
        return reverse('accounts:add_member', args=[self.id, self.slug])
