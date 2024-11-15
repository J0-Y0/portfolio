from django.shortcuts import render
from .models import *


def dynamic_page(request, page_name=""):
    # Mapping page names to template files
    pages = {
        "": "pages/landing.html",
        "education": "pages/education.html",
        "experience": "pages/experience.html",
        "about": "pages/about.html",
        "projects": "pages/projects.html",
        "contact": "pages/contact.html",
    }

    # Get the template for the requested page or default to 'home.html'
    template_to_include = pages.get(page_name)

    context = {
        "profile": Profile.objects.first(),
        "skills": Skill.objects.all(),
        "page": template_to_include,
    }

    return render(request, "index.html", context=context)
