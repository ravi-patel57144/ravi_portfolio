from django.contrib import admin
from django.db import models

from website.models import Resource, About, Skill, ResumeEducation, ResumeExperience, ResumeProject, Resume, Project, \
    Contact


# Register your models here.
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'resume', 'github_link', 'linkedin_link', 'instagram_link', 'twitter_link', 'skype_link']


class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'phone', 'email', 'website', 'birthday', 'age', 'city', 'freelancer']


class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']


class ResumeAdmin(admin.ModelAdmin):
    list_display = ['objective']


class ResumeEducationAdmin(admin.ModelAdmin):
    list_display = ['education_title']


class ResumeExperienceAdmin(admin.ModelAdmin):
    list_display = ['experience_title']


class ResumeProjectAdmin(admin.ModelAdmin):
    list_display = ['project_title']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['contact_name', 'contact_email', 'contact_subject', 'contact_message']


admin.site.register(Resource, ResourceAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(ResumeEducation, ResumeEducationAdmin)
admin.site.register(ResumeExperience, ResumeExperienceAdmin)
admin.site.register(ResumeProject, ResumeProjectAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact,ContactAdmin)
