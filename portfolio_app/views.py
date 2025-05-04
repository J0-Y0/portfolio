from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.core.validators import validate_email
from .models import Inbox
from .models import *


def get_common_context():
    """
    A helper function to prepare the common context for all pages.
    """
    return {
        "profile": Profile.objects.first(),
        "skills": Skill.objects.all(),
        "social_links": SocialLink.objects.order_by("-id"),
        "educations": Education.objects.all(),
        "certifications": Certifications.objects.all(),
        "experiences": Experience.objects.order_by("-start_date"),
    }


def landing(request):

    context = get_common_context()
    return render(request, "pages/landing.html", context)


def home(request):
    projects = Project.objects.all()

    context = {**get_common_context(), "projects": projects}
    return render(request, "index.html", context)


def project_detail(request, slug):

    project = Project.objects.filter(slug=slug).first()

    context = {**get_common_context(), "project": project}
    #
    # context.update({"project_slug": slug})  # Add slug-specific context if needed
    return render(request, "pages/project_detail.html", context)


def contact(request):

    context = {
        "error": "",
        "success": "",
        "form_data": {},  # To preserve user input
    }

    if request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")
        success_trigger = ""

        # Preserve input data in case of errors
        context["form_data"] = {"email": email, "message": message}

        if not email or not message:
            context["error"] = "Email and message cannot be empty."
        else:
            try:
                validate_email(email)
                Inbox.objects.create(sender_email=email, message=message)
                success_trigger = "success"
                context["form_data"] = {}
            except ValidationError:
                context["error"] = "Invalid email format."
            except IntegrityError as e:
                if "UNIQUE constraint" in str(e):
                    context["error"] = (
                        "It looks like you've already sent a message. Thank you!"
                    )
                else:
                    context["error"] = f"Database error: {e}"
            except Exception:
                context["error"] = "An error occurred while saving the message."

    response = render(request, "partials/contact-form-content.html", context)
    response["HX-trigger"] = success_trigger
    return response
