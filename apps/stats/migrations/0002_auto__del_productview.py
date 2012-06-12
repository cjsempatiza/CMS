# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ProductView'
        db.delete_table('stats_productview')


    def backwards(self, orm):
        # Adding model 'ProductView'
        db.create_table('stats_productview', (
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Product'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('tracking_id', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('stats', ['ProductView'])


    models = {
        
    }

    complete_apps = ['stats']