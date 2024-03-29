from django.db import models
from django.utils.text import slugify

# Create your models here.

JOB_TYPE = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
    ("Remote", "Remote"),
)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=10000, default="")
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f"jobs/%Y/%m/%d/", default="")
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Apply(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to="apply/")
    cover_letter = models.TextField(max_length=500)
    job = models.ForeignKey(Job, related_name="apply", on_delete=models.CASCADE)
    applyed_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
