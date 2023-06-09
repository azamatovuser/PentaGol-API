# Generated by Django 4.2 on 2023-04-30 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=221)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=221)),
                ('image', models.ImageField(upload_to='team_image/')),
                ('played_games', models.IntegerField()),
                ('goals', models.IntegerField()),
                ('scores', models.IntegerField()),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.league')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_side_goals', models.IntegerField()),
                ('opposite_side_goals', models.IntegerField()),
                ('created_date', models.DateTimeField()),
                ('first_side', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_side', to='team.team')),
                ('opposite_side', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opposite_side', to='team.team')),
            ],
        ),
    ]
