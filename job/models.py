from django.db import models

# Create your models here.

JOB_TYPE = (
    ("F", "Full Time"),
    ("P", "Part Time"),
    ("R", "Remote"),
)


class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=1, choices=JOB_TYPE)
    description = models.TextField(max_length=10000, default="")
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.title)
