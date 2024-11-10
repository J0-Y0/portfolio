from django.contrib import admin
from .models import *


# --- Inlines ---
class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1  # Allows one empty form for new entries


# Define many-to-many through inline (if needed)
class ProjectSkillsInline(admin.TabularInline):
    model = Project.skills_used.through  # Use the intermediary table
    extra = 1


class ProjectTagsInline(admin.TabularInline):
    model = Project.tags.through  # Use the intermediary table
    extra = 1


# --- ModelAdmin Classes ---
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "intro"]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ["city", "region", "country"]


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ["social_media_name", "username_url"]
    search_fields = ["social_media_name"]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["institution", "degree", "start_date", "end_date"]
    search_fields = ["institution", "degree"]
    list_filter = ["start_date", "end_date"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    inlines = [ProjectSkillsInline, ProjectTagsInline]
    filter_horizontal = ["skills_used", "tags"]  # Manage M2M relationships
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    filter_horizontal = ["tags"]  # Manage M2M relationship with tags


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["job_title", "company", "start_date", "end_date"]
    search_fields = ["job_title", "company"]
    list_filter = ["start_date", "end_date"]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "published_date", "publisher"]
    search_fields = ["title", "publisher"]
    list_filter = ["published_date"]
    filter_horizontal = ["tags"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Certifications)
class CertificationsAdmin(admin.ModelAdmin):
    list_display = ["title", "issued_on", "certificate_link"]
    search_fields = ["title"]
