# Generated by Django 2.2 on 2019-04-29 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'ordering': ['pk'], 'verbose_name': 'faq', 'verbose_name_plural': 'faqs'},
        ),
        migrations.RemoveField(
            model_name='faq',
            name='position',
        ),
    ]