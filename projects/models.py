from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class ProgrammingLanguage(models.Model):
    
    # Fields
    name = models.CharField(max_length=200, help_text='Enter programming language (e.g. Python)')

    # Metadata
    class Meta:
        ordering = ['-name']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return self.name
class Project(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this project')
    name = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000)
    language = models.OneToOneField(ProgrammingLanguage, help_text='Select a programming language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this project."""
        return reverse('project-detail', args=[str(self.id)])

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'