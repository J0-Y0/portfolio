from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.admin import ModelAdmin, TabularInline

from .models import *


# --- Inlines ---
class SocialLinkInline(TabularInline):
    model = SocialLink
    extra = 1  # Allows one empty form for new entries


class JobTaskInline(TabularInline):
    model = JobTask
    extra = 1  # Allows one empty form for new entries


# Define many-to-many through inline (if needed)
class ProjectSkillsInline(TabularInline):
    model = Project.skills_used.through  # Use the intermediary table
    extra = 1


class ProjectTagsInline(TabularInline):
    model = Project.tags.through  # Use the intermediary table
    extra = 1


# --- ModelAdmin Classes ---
@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ["first_name", "last_name", "heading", "sub_heading"]


@admin.register(Address)
class AddressAdmin(ModelAdmin):
    list_display = ["city", "region", "country"]


@admin.register(SocialLink)
class SocialLinkAdmin(ModelAdmin):

    list_display = ["social_media_name", "logo_svg"]
    search_fields = ["social_media_name"]

    def logo_svg(self, obj):
        if obj.logo:  # assuming `logo` is the field storing the SVG file
            return format_html(
                '<a href ="{}" target="_blank" style = " display:flex; align-items:center; height:fit-content;"> <img src="{}" width="30" height="30" /> <h4 style  ="padding-left:10px"> {} </h4> </a> ',
                obj.your_address,
                obj.logo.url,
                obj.social_media_name,
            )
        return "-"

    logo_svg.short_description = "Logo"  # optional column header


@admin.register(Education)
class EducationAdmin(ModelAdmin):
    list_display = ["institution", "degree", "start_date", "end_date"]
    search_fields = ["institution", "degree"]
    list_filter = ["start_date", "end_date"]


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    inlines = [ProjectSkillsInline, ProjectTagsInline]
    filter_horizontal = ["skills_used", "tags"]  # Manage M2M relationships
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Skill)
class SkillAdmin(ModelAdmin):
    list_display = [
        "name",
        "logo_svg",
    ]
    search_fields = ["name"]
    filter_horizontal = ["tags"]  # Manage M2M relationship with tags

    def logo_svg(self, obj):
        if obj.logo:  # assuming `logo` is the field storing the SVG file
            return format_html(
                '<div style = " display:flex; align-items:center; height:fit-content;"> <img src="{}" width="30" height="30" /> <h4 style  ="padding-left:10px">{}</h4> </div> ',
                obj.logo.url,
                obj.name,
            )
        return "-"

    logo_svg.short_description = "Logo"  # optional column header


@admin.register(Experience)
class ExperienceAdmin(ModelAdmin):
    list_display = ["position", "company", "start_date", "end_date"]
    search_fields = ["position", "company"]
    list_filter = ["start_date", "end_date"]
    inlines = [
        JobTaskInline,
    ]


@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ["title", "published_date", "publisher"]
    search_fields = ["title", "publisher"]
    list_filter = ["published_date"]
    filter_horizontal = ["tags"]


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Certifications)
class CertificationsAdmin(ModelAdmin):
    list_display = ["title", "issued_on", "certificate_link"]
    search_fields = ["title"]


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
