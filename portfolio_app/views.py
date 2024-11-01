from django.shortcuts import render


def dynamic_page(request, page_name):
    # Mapping page names to template files
    pages = {
        "home": "home.html",
        "education": "education.html",
        "experience": "experience.html",
        "about": "about.html",
    }

    # Get the template for the requested page or default to 'home.html'
    template_to_include = pages.get(page_name, "home.html")

    return render(request, "index.html", {"page": template_to_include})
