# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import powerdns.utils
import django.core.validators
import dj.choices.fields


class PostgresOnlyRunSQL(migrations.RunSQL):
    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        if not schema_editor.connection.vendor.startswith('postgres'):
            return
        super(PostgresOnlyRunSQL, self).database_forwards(app_label, schema_editor, from_state, to_state)

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        if not schema_editor.connection.vendor.startswith('postgres'):
            return
        super(PostgresOnlyRunSQL, self).database_backwards(app_label, schema_editor, from_state, to_state)


class Migration(migrations.Migration):

    dependencies = [
        ('powerdns', '0008_auto_20150821_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='name',
            field=models.CharField(unique=True, verbose_name='name', max_length=255, validators=[django.core.validators.RegexValidator('^([A-Za-z0-9-]+\\.)*([A-Za-z0-9])+$')]),
        ),
        PostgresOnlyRunSQL(
            (
                "ALTER TABLE records ALTER COLUMN auto_ptr TYPE INTEGER USING auto_ptr::integer, ALTER COLUMN auto_ptr SET DEFAULT 1;",
                "ALTER TABLE records ALTER COLUMN auto_ptr DROP DEFAULT;",
            ),
            migrations.RunSQL.noop
        ),
        migrations.AlterField(
            model_name='record',
            name='auto_ptr',
            field=dj.choices.fields.ChoiceField(default=2, choices=powerdns.utils.AutoPtrOptions, verbose_name='Auto PTR record'),
        ),
        PostgresOnlyRunSQL(
            migrations.RunSQL.noop,
            (
                "ALTER TABLE records ALTER COLUMN auto_ptr TYPE BOOLEAN USING CASE WHEN auto_ptr = 0 THEN FALSE ELSE TRUE END, ALTER COLUMN auto_ptr SET DEFAULT TRUE;",
                "ALTER TABLE records ALTER COLUMN auto_ptr DROP DEFAULT;",
            )
        ),
        PostgresOnlyRunSQL(
            (
                "ALTER TABLE powerdns_recordtemplate ALTER COLUMN auto_ptr TYPE INTEGER USING auto_ptr::integer, ALTER COLUMN auto_ptr SET DEFAULT 1;",
                "ALTER TABLE powerdns_recordtemplate ALTER COLUMN auto_ptr DROP DEFAULT;",
            ),
            migrations.RunSQL.noop
        ),
        migrations.AlterField(
            model_name='recordtemplate',
            name='auto_ptr',
            field=dj.choices.fields.ChoiceField(default=2, choices=powerdns.utils.AutoPtrOptions, verbose_name='Auto PTR field'),
        ),
        PostgresOnlyRunSQL(
            migrations.RunSQL.noop,
            (
                "ALTER TABLE powerdns_recordtemplate ALTER COLUMN auto_ptr TYPE BOOLEAN USING CASE WHEN auto_ptr = 0 THEN FALSE ELSE TRUE END, ALTER COLUMN auto_ptr SET DEFAULT TRUE;",
                "ALTER TABLE powerdns_recordtemplate ALTER COLUMN auto_ptr DROP DEFAULT;",
            )
        ),
    ]
