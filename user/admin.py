from django.contrib import admin
from user.models import Profile,Message,Skill

# Register your models here.

admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Skill)

