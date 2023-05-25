# Generated by Django 4.2 on 2023-05-11 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CUSTOMER', 'Сотрудник'), ('TECHNICIAN', 'Техник'), ('MASTER', 'Мастер')], default='CUSTOMER', max_length=15),
        ),
    ]