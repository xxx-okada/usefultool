#---P443---
from django.forms import ModelForm
from .models import ToolPost

class ToolPostForm(ModelForm):
    class Meta:
        model = ToolPost
        fields = ['category','title','for_user','comment','image1','image2']