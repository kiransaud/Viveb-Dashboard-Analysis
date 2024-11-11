# Generated by Django 5.0 on 2024-01-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash_board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VivebFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='viveb_files/')),
                ('file_type', models.CharField(choices=[('saga', 'Saga File'), ('saga_instance', 'Saga Instance File'), ('saga_log', 'Saga Log File')], max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='SagaFile',
        ),
    ]