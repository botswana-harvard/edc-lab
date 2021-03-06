# Generated by Django 2.0.1 on 2018-01-14 12:38

import _socket
from django.db import migrations, models
import django.db.models.deletion
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.utils


class Migration(migrations.Migration):

    dependencies = [
        ('edc_lab', '0011_delete_identifierhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('display_name', models.CharField(max_length=50)),
                ('lab_profile_name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('lab_profile_name', 'name'),
            },
        ),
        migrations.RemoveField(
            model_name='historicalresult',
            name='panel_name',
        ),
        migrations.RemoveField(
            model_name='result',
            name='panel_name',
        ),
        migrations.AlterUniqueTogether(
            name='panel',
            unique_together={('name', 'lab_profile_name')},
        ),
        migrations.AddField(
            model_name='historicalresult',
            name='panel',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_lab.Panel'),
        ),
        migrations.AddField(
            model_name='result',
            name='panel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='edc_lab.Panel'),
        ),
    ]
