from django.contrib import admin
from .models import Post
from leaflet.forms.widgets import LeafletWidget

admin.site.register(Post)