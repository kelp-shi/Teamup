from django.contrib import admin
from .models import CustomUser, PostProject, ProjectTags

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(PostProject),
admin.site.register(ProjectTags),