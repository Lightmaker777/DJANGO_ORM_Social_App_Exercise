# Generated by Django 4.2.7 on 2023-11-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "social_app",
            "0003_alter_post_created_at_alter_user_age_alter_user_bio_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_at"], "verbose_name": "Post"},
        ),
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ["-joined_at", "username"],
                "verbose_name": "User from app",
            },
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.UniqueConstraint(
                fields=("username", "email"), name="unique email7username"
            ),
        ),
        migrations.AlterModelTable(
            name="user",
            table="users",
        ),
    ]
