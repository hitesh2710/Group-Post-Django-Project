from django.db.models import fields
from .models import Post
from django.forms import ModelForm,Textarea



class postcreateform(ModelForm):
    class Meta():
        model=Post
        fields=('Message','Group')
        widgets = {
            'Message': Textarea(attrs={'cols': 150, 'rows': 5}),
        }
