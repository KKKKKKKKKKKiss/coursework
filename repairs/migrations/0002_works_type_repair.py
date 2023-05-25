from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='type_repair',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='works', to='repairs.typerepair', verbose_name='Тип работы'),
        ),
    ]