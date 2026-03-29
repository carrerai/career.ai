# Generated migration for adding ai_guidance field to Result model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_testsession_remove_question_trait_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='ai_guidance',
            field=models.JSONField(default=dict),
        ),
    ]
