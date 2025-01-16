from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Inbox
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
        "social_links": SocialLink.objects.order_by("-id"),
        "educations": Education.objects.all(),
        "certifications": Certifications.objects.all(),
        "experiences": Experience.objects.order_by("-start_date"),
        "page": template_to_include,
    }

    return render(request, "index.html", context=context)


def message(request):
    if request.method == "POST":
        # Extract data from the POST request
        message = request.POST.get("message")
        email = request.POST.get("email")

        # Validate that email and message are not empty
        if not email or not message:
            return JsonResponse(
                {"error": "Email and message cannot be empty."}, status=400
            )

        # Validate email format
        try:
            validate_email(email)  # Check if the email is valid
        except ValidationError:
            return JsonResponse({"error": "Invalid email format."}, status=400)

        # Save the message to the database
        try:
            Inbox.objects.create(sender_email=email, message=message)
            return JsonResponse({"message": "Message sent successfully!"}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse(
                {"error": "An error occurred while saving the message."}, status=500
            )

    return JsonResponse({"error": "Invalid request method."}, status=405)
