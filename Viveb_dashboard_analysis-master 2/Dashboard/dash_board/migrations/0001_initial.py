# Generated by Django 4.2.9 on 2024-01-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SagaFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='saga_files/')),
                ('file_type', models.CharField(choices=[('saga', 'Saga File'), ('saga_instance', 'Saga Instance File'), ('saga_log', 'Saga Log File')], max_length=20)),
            ],
        ),
    ]