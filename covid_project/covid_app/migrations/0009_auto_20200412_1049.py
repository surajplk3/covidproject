# Generated by Django 3.0.3 on 2020-04-12 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_app', '0008_covid_ind_date_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='covid_data_anal',
            old_name='daily_decease',
            new_name='conf_cum_plot',
        ),
        migrations.RenameField(
            model_name='covid_data_anal',
            old_name='daily_recov',
            new_name='dailyconf_dist_15mar',
        ),
        migrations.AddField(
            model_name='covid_data_anal',
            name='decease_daily_plot',
            field=models.ImageField(blank=True, upload_to='graphs'),
        ),
        migrations.AddField(
            model_name='covid_data_anal',
            name='deceased_cum_plot',
            field=models.ImageField(blank=True, upload_to='graphs'),
        ),
        migrations.AddField(
            model_name='covid_data_anal',
            name='heat_map',
            field=models.ImageField(blank=True, upload_to='graphs'),
        ),
        migrations.AddField(
            model_name='covid_data_anal',
            name='pair_plot',
            field=models.ImageField(blank=True, upload_to='graphs'),
        ),
        migrations.AddField(
            model_name='covid_data_anal',
            name='recov_daily_plot',
            field=models.ImageField(blank=True, upload_to='graphs'),
        ),
        migrations.AddField(
            model_name='covid_data_anal',
            name='recovered_cum_plot',
            field=models.ImageField(blank=True, upload_to='graphs'),
        ),
    ]
