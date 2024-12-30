from models import News_Post
from django.forms import ModelForm


class NewsPostForm(ModelForm):
    class Meta:
        model = News_Post
        fields = ['title', 'short_description', 'text', 'pub_date']
