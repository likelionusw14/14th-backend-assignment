from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lion',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='lion',
            name='track',
            field=models.CharField(
                choices=[
                    ('Django', 'Django'),
                    ('SpringBoot', 'SpringBoot'),
                    ('Frontend', 'Frontend'),
                ],
                max_length=100,
            ),
        ),
    ]
