# Generated by Django 4.1.2 on 2022-10-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0002_works_type_repair'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='status',
            field=models.CharField(choices=[('CREATED', 'Новая заявка от клиента'), ('CONFIRMED', 'Подтверждена техником'), ('READY_TO_WORK', 'Готова к работе'), ('PROGRESS', 'В работе'), ('VERIFICATION', 'Ремонт выполнен'), ('TESTS', 'На тестировании'), ('RE_REPAIR', 'На доработку')], default='CREATED', max_length=20),
        ),
    ]