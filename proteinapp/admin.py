from django.contrib import admin
from django.contrib.admin.options import ModelAdmin 
from .models import * 
# Register your models here.

class PfamAdmin (admin.ModelAdmin):
    list_diplay = ['pfam_id','pfam_description']

class OrganismAdmin (admin.ModelAdmin):
    list_display = ['organism_id','organism_genus','organism_sp','organism_clade']

class DomainAdmin (admin.ModelAdmin):
    list_display = ['domain_start','domain_end','domain_description','domain_id']

class ProteinAdmin (admin.ModelAdmin):
    list_display = ['protein_id','protein_sequence','protein_length','organism']

admin.site.register(Pfam,PfamAdmin)
admin.site.register(Organism,OrganismAdmin)
admin.site.register(Domain,DomainAdmin)
admin.site.register(Protein,ProteinAdmin)