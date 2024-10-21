from django.db import models


class About(models.Model):
    content = models.TextField()

    def __str__(self):
        return "About Me"


class Address(models.Model):
    city = models.CharField(max_length=100)
    region = models.CharField(
        max_length=100, blank=True, null=True
    )  # optional if you dont want to specify region
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}"


class SocialLink(models.Model):
    social_media_name = models.CharField(max_length=50)
    username_url = models.URLField()
    social_logo = models.ImageField(
        upload_to="social_logos/"
    )  # Ensure you have Pillow installed

    def __str__(self):
        return self.social_media_name


class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    details = models.TextField()

    def __str__(self):
        return f"{self.degree} from {self.institution}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    problem_statement = models.TextField(null=True, blank=True)  # optional
    tags = models.ManyToManyField("Tag", related_name="projects")
    skills_used = models.ManyToManyField("Skill", related_name="projects")
    explored = models.TextField()

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    tags = models.ManyToManyField("Tag", related_name="skills")
    description = models.TextField()  # "What I have done with it"

    def __str__(self):
        return self.name


class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"


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
