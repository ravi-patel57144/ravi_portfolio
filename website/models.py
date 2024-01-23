from datetime import date

from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class Resource(models.Model):
    name = models.CharField(max_length=200)
    resume = models.FileField(upload_to='resume/', validators=[FileExtensionValidator(['pdf'])],
                              help_text='File Must Be in PDF format')
    github_link = models.URLField()
    linkedin_link = models.URLField()
    instagram_link = models.URLField()
    twitter_link = models.URLField()
    skype_link = models.URLField()

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=200)
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    website = models.URLField()
    education = models.CharField(max_length=200)
    birthday = models.DateField()
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    freelancer = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        self.age = age
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.name


class Resume(models.Model):
    objective = models.TextField()


class ResumeEducation(models.Model):
    education_title = models.CharField(max_length=200)
    time_period = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)


class ResumeExperience(models.Model):
    experience_title = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    company_description = models.TextField()
    roles_and_responsibility = models.TextField(blank=True, null=True)


class ResumeProject(models.Model):
    project_title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    project_period = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    project_link = models.URLField(blank=True, null=True)


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.TextField(blank=True, null=True)
    project_image = models.ImageField(upload_to='project_images/')
    project_link = models.URLField(blank=True, null=True)
    project_technology = models.CharField(max_length=200)
    project_bio = models.CharField(max_length=400)


class Contact(models.Model):
    contact_name = models.CharField(max_length=200)
    contact_email = models.EmailField()
    contact_subject = models.CharField(max_length=200)
    contact_message = models.TextField()
