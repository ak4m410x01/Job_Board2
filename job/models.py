from django.db import models

# Create your models here.

JOB_TYPE = (
    ("F", "Full Time"),
    ("P", "Part Time"),
    ("R", "Remote"),
)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=1, choices=JOB_TYPE)
    description = models.TextField(max_length=10000, default="")
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
