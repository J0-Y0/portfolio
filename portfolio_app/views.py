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
        "tags": Tag.objects.exclude(skills__isnull=True),
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


# views.py
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from .models import Resume
import os


def download_latest_resume(request):
    try:
        # Get the most recent resume
        resume = get_object_or_404(Resume.objects.order_by("-created_at"))

        # Verify file exists
        if not resume.resume or not os.path.exists(resume.resume.path):
            raise Http404("Resume file not found on server")

        # Generate a clean filename
        original_name = os.path.basename(resume.resume.name)
        name, ext = os.path.splitext(original_name)
        clean_name = slugify(name) + ext

        # Create response
        response = FileResponse(
            resume.resume.open("rb"),
            as_attachment=True,
            filename=f"resume_{clean_name}",
        )

        # Set appropriate content type
        content_types = {
            ".pdf": "application/pdf",
            ".doc": "application/msword",
            ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            ".txt": "text/plain",
        }
        response["Content-Type"] = content_types.get(
            ext.lower(), "application/octet-stream"
        )

        return response

    except Exception as e:
        # Log error to your error tracking system
        # logger.error(f"Resume download failed: {str(e)}")
        raise Http404("Could not process your download request")
