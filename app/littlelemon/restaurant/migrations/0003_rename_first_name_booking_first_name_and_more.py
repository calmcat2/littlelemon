# Generated by Django 5.0.2 on 2024-09-20 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menu_description_alter_booking_bookingdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='first_name',
            new_name='First_name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='reservation_date',
            new_name='Reservation_date',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='reservation_slot',
            new_name='Reservation_slot',
        ),
    ]
