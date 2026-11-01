from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_time',
            field=models.CharField(default='09:00 AM', help_text='e.g. 10:00 AM', max_length=100),
        ),
    ]
