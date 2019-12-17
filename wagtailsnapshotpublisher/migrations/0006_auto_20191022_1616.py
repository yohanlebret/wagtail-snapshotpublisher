# Generated by Django 2.2.6 on 2019-10-22 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailsnapshotpublisher', '0005_wsspcontentrelease_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='wsspcontentrelease',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='release_publisher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wsspcontentrelease',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='release_author', to=settings.AUTH_USER_MODEL),
        ),
    ]