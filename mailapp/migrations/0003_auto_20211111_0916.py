# Generated by Django 3.2.9 on 2021-11-11 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailapp', '0002_remove_email_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='recipients',
        ),
        migrations.AddField(
            model_name='email',
            name='receiver',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='receivers', to='auth.user'),
            preserve_default=False,
        ),
    ]
