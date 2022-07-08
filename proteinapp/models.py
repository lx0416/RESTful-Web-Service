from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields.related import ManyToManyField

class Pfam(models.Model):
    pfam_id = models.CharField(max_length=25, null=True, blank=True)
    pfam_description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return str(self.pfam_id)

class Organism(models.Model):
    organism_id = models.IntegerField(null=True, blank=True)
    organism_genus = models.CharField(max_length=256, null=True, blank=True)
    organism_sp = models.CharField(max_length=256, null=True, blank=True)
    organism_clade = models.CharField(max_length=1, null=True, blank=True, default="E")

    def __str__(self):
        return str(self.organism_id)

class Domain(models.Model):
    domain_start = models.IntegerField(null=True, blank=True)
    domain_end = models.IntegerField(null=True, blank=True)
    domain_description = models.CharField(max_length=256, null=True, blank=True)

    domain_id = models.OneToOneField(Pfam, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.domain_id

class Protein(models.Model):
    protein_id = models.CharField(max_length=256, null=True, blank=True)
    protein_sequence = models.CharField(max_length=256, null=True, blank=True)
    protein_length = models.IntegerField(null=True, blank=True)

    organism = models.ForeignKey(Organism, on_delete=models.DO_NOTHING)
    domain = models.ManyToManyField(Domain, through="ProteinDomainLink")

    def __str__(self):
        return self.protein_id

# link protein and domains
class ProteinDomainLink(models.Model):
    protein_id = models.ForeignKey(Protein, on_delete=models.DO_NOTHING)
    domain = models.ForeignKey(Domain, on_delete=models.DO_NOTHING)