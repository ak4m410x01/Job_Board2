# Generated by Django 4.2.4 on 2023-08-11 13:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0007_alter_job_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="job_type",
            field=models.CharField(
                choices=[
                    ("Full Time", "Full Time"),
                    ("Part Time", "Part Time"),
                    ("Remote", "Remote"),
                ],
                max_length=15,
            ),
        ),
    ]