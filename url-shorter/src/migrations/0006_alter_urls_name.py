# Generated by Django 4.0.5 on 2022-06-28 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_alter_urls_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='name',
            field=models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False),
        ),
    ]
