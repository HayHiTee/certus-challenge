# Generated by Django 2.0.5 on 2019-11-03 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordVault',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_store', models.BooleanField()),
                ('password', models.CharField(max_length=200)),
                ('general_info', models.CharField(max_length=200)),
                ('include_symbols', models.BooleanField()),
                ('include_numbers', models.BooleanField()),
                ('include_lower', models.BooleanField()),
                ('include_upper', models.BooleanField()),
                ('exclude_similar', models.BooleanField()),
                ('exclude_char', models.BooleanField()),
                ('website', models.URLField(default='')),
            ],
        ),
    ]
