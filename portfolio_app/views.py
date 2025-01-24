from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ValidationError
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


def about(request):
    context = get_common_context()
    return render(request, "pages/about.html", context)


def education(request):
    context = get_common_context()
    return render(request, "pages/education.html", context)


def experience(request):
    context = get_common_context()
    return render(request, "pages/experience.html", context)


def projects(request):
    context = get_common_context()
    return render(request, "pages/portfolio.html", context)


def project_detail(request, slug):
    context = get_common_context()
    context.update({"project_slug": slug})  # Add slug-specific context if needed
    return render(request, "pages/project_detail.html", context)


# def message(request):
#     if request.method == "POST":
#         # Extract data from the POST request
#         message = request.POST.get("message")
#         email = request.POST.get("email")

#         # Validate that email and message are not empty
#         if not email or not message:
#             return JsonResponse(
#                 {"error": "Email and message cannot be empty."}, status=400
#             )

#         # Validate email format
#         try:
#             validate_email(email)  # Check if the email is valid
#         except ValidationError:
#             return JsonResponse({"error": "Invalid email format."}, status=400)

#         # Save the message to the database
#         try:
#             Inbox.objects.create(sender_email=email, message=message)
#             return JsonResponse({"message": "Message sent successfully!"}, status=200)
#         except Exception as e:
#             print(e)
#             return JsonResponse(
#                 {"error": "An error occurred while saving the message."}, status=500
#             )

#     return JsonResponse({"error": "Invalid request method."}, status=405)


def contact(request):
    context = {
        "error": "",
        "success": "",
        "form_data": {},  # To preserve user input
    }

    if request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Preserve input data in case of errors
        context["form_data"] = {"email": email, "message": message}

        if not email or not message:
            context["error"] = "Email and message cannot be empty."
        else:
            try:
                validate_email(email)
                Inbox.objects.create(sender_email=email, message=message)
                context["success"] = True
                context["form_data"] = {}
            except ValidationError:
                context["error"] = "Invalid email format."
            except Exception:
                context["error"] = "An error occurred while saving the message."

    return render(request, "pages/contact.html", context)


def flowbit(request):
    return render(
        request,
        "flowbit.html",
    )


def project_detail(request, slug):
    return render(
        request,
        "pages/project_detail.html",
    )
