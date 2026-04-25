from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lions', '0002_alter_lion_name_alter_lion_track'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lion',
            options={'ordering': ['-created_at']},
        ),
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
