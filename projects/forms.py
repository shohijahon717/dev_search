from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
         'title',
         'featured_image', 
         'description', 
         'tags',
          'demo_link',
          'source_link',
          'vote_total', 
          'vote_ratio'
        ]

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),  # taglarni ptichka bn belgilanadigan qilish un
        }

    def __init__(self, *args, **kwargs):  # formani chiroyli ko'rinishga
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

    