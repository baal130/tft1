# Generated by Django 2.2.6 on 2022-09-13 07:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Students', '0004_auto_20220912_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='aproved_by',
            field=models.ManyToManyField(related_name='aproved', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='aproved_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='noteforadmin',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='gradeaverage',
            field=models.DecimalField(decimal_places=2, default=3.0, max_digits=4, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='totalgraduationgrade',
            field=models.DecimalField(decimal_places=2, default=3.0, max_digits=4, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
