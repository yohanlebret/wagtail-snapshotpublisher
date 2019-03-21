# Generated by Django 2.1.7 on 2019-03-21 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailsnapshotpublisher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content_release', models.ForeignKey(blank=True, default=None, limit_choices_to={'status': 0}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='testmodel_content_release', to='wagtailsnapshotpublisher.WSSPContentRelease')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content_release', models.ForeignKey(blank=True, default=None, limit_choices_to={'status': 0}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='testpage_content_release', to='wagtailsnapshotpublisher.WSSPContentRelease')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]