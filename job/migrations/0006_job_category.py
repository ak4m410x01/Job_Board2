# Generated by Django 4.2.4 on 2023-08-11 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0005_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="category",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="job.category",
            ),
        ),
    ]
