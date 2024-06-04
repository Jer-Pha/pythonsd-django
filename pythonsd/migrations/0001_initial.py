# Generated by Django 3.2.25 on 2024-05-31 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('meetup_url', models.URLField(blank=True, max_length=255)),
                ('linkedin_url', models.URLField(blank=True, max_length=255)),
                ('active', models.BooleanField(default=True, help_text='Set to False to hide this organizer from the organizers page')),
                ('photo', models.ImageField(help_text='Recommended size of 400*400px or larger square', upload_to='organizers/')),
            ],
        ),
    ]
