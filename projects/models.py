from django.db import models
from django.urls import reverse

# Create your models here.
class ProjectModel(models.Model):

    # Fields
    language = models.CharField(max_length=20, field='Enter programming language')

    # Metadata
    class Meta:
        ordering = ['-language']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return self.language