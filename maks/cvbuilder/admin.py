from django.contrib import admin
from .models import Resume, Experience, Template
from unfold.admin import ModelAdmin
from allauth.account.models import EmailAddress
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(Resume)
class ResumeAdmin(ModelAdmin):
    pass


@admin.register(Experience)
class ExperienceAdmin(ModelAdmin):
    pass


@admin.register(Template)
class TemplateAdmin(ModelAdmin):
    pass


admin.site.unregister(EmailAddress)
admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


admin.site.site_header = 'CV builder admin panel'
admin.site.index_title = 'CV builder admin panel'
admin.site.site_title = 'CV builder admin panel'