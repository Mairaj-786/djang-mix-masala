from django.contrib import admin
from .models import Plot,Question,Choice,Answer,Post,Comment
# Register your models here.

admin.site.register(Plot)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(Post)
admin.site.register(Comment)
