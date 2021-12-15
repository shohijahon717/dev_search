from django.forms import ModelForm
from django import forms
from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
         'title',
         'featured_image', 
         'description', 
          'demo_link',
          'source_link',
        #   'vote_total', 
        #   'vote_ratio'
        ]

        

    def __init__(self, *args, **kwargs):  # formani chiroyli ko'rinishga
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ReviewForm(ModelForm):
    class Meta:
        model=Review
        fields = [
            'value',
            'body'   
        ]
        labels = {
            'value': "Izoh qoldiring",
            'body':"Ovoz bering",
        }
    def __init__(self, *args, **kwargs):  # formani chiroyli ko'rinishga
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


    