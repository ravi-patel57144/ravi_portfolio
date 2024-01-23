from django.http import HttpResponse
from django.shortcuts import render
from .models import Resource, About, Skill, Resume, ResumeEducation, ResumeExperience, ResumeProject, Project, Contact


def home(request):
    resource = Resource.objects.first()
    about = About.objects.first()
    skills = Skill.objects.all()
    resume = Resume.objects.first()
    resume_education = ResumeEducation.objects.all()
    resume_experience = ResumeExperience.objects.all()
    resume_project = ResumeProject.objects.all()
    projects = Project.objects.all()
    return render(request, 'index.html', {'resource': resource, 'about': about, 'skills': skills,
                                          'resume': resume, 'resume_education': resume_education,
                                          'resume_experience': resume_experience, 'resume_project': resume_project,
                                          'projects': projects})


def footer(request):
    resource = Resource.objects.first()
    return render(request, 'footer.html', {'resource': resource})


def contact(request):
    if request.method == 'POST':
        try:
            Contact.objects.create(
                contact_name=request.POST.get('name'),
                contact_email=request.POST.get('email'),
                contact_subject=request.POST.get('subject'),
                contact_message=request.POST.get('message')
            )
        except:
            return HttpResponse("ERROR WHILE SUBMITTING DATA")
        return render(request, 'index.html', context={'msg': 'success'})
