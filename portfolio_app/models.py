from django.db import models
from django.core.exceptions import ValidationError
import os


def validate_image_file(value):
    allowed_extensions = [".svg", ".png", ".jpg", ".jpeg"]
    allowed_mime_types = ["image/svg+xml", "image/png", "image/jpeg"]

    # Check file extension
    ext = os.path.splitext(value.name)[1]  # Extracts the file extension
    if ext.lower() not in allowed_extensions:
        raise ValidationError(
            f"Unsupported file format. Allowed types: {', '.join(allowed_extensions)}"
        )

    # Check MIME type if content_type is available
    if hasattr(value, "content_type") and value.content_type not in allowed_mime_types:
        raise ValidationError("Invalid image type.")


class Profile(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    heading = models.CharField(max_length=255)  # heading to your landing page
    sub_heading = models.CharField(max_length=255)  # heading to your profile
    about = models.TextField()
    # for about page
    profile_picture = models.FileField(
        upload_to="profile_pic/", validators=[validate_image_file], null=True
    )  # Ensure you have Pillow installed
    # for side bar
    profile_picture_mini = models.FileField(
        upload_to="profile_pic/", validators=[validate_image_file], null=True
    )  # Ensure you have Pillow installed

    def __str__(self):
        return "About Me"


class Address(models.Model):
    city = models.CharField(max_length=100)
    region = models.CharField(
        max_length=100, blank=True, null=True
    )  # optional if you dont want to specify region
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city},{self.region},{self.country}"


class SocialLink(models.Model):
    social_media_name = models.CharField(max_length=50)
    your_address = models.CharField(unique=True, max_length=255)
    logo = models.FileField(
        upload_to="social_logos/",
        validators=[validate_image_file],
    )  # Ensure you have Pillow installed

    def __str__(self):
        return self.social_media_name


class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    website = models.URLField(max_length=300, blank=True)
    address = models.CharField(max_length=255)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} from {self.institution}"


class Certifications(models.Model):
    title = models.CharField(max_length=200, null=False)
    issued_by = models.CharField(max_length=255, null=False)
    issued_on = models.DateField()
    certificate_link = models.URLField()


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=False)
    short_description = models.TextField(max_length=400)
    problem_of_statement = models.TextField(null=True, blank=True)  # optional
    solution_detail = models.TextField(null=True, blank=True)  # optional
    video_link = models.URLField(null=True, blank=True)
    tags = models.ManyToManyField("Tag", related_name="projects", null=True, blank=True)
    skills_used = models.ManyToManyField("Skill", related_name="projects")

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT, null=True)

    image_list = models.ImageField(
        upload_to="ProjectImage/",
        validators=[validate_image_file],
        null=True,
        blank=True,
    )


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tags = models.ManyToManyField("Tag", related_name="skills", null=True, blank=True)
    logo = models.FileField(
        upload_to="skill_logos/",
        validators=[validate_image_file],
        blank=True,
        default="skill_default.svg",
    )  # Ensure you have Pillow installed

    description = models.TextField(null=True, blank=True)  # "What I have done with it"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.logo:
            self.logo.name = "skill_logos/skill_default.svg"
        return super().save(*args, **kwargs)


class Experience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"

    def formatted_end_date(self):
        return self.end_date if self.end_date else "Present"


class JobTask(models.Model):
    experience = models.ForeignKey(
        Experience, on_delete=models.CASCADE, related_name="tasks"
    )
    task = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.task}"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateField()
    publisher = models.CharField(max_length=100)  # Optional
    tags = models.ManyToManyField("Tag", related_name="blogs")

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Inbox(models.Model):
    sender_email = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    delivered_time = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)

    class Meta:
        unique_together = ("sender_email", "message")
