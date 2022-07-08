from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import *

class PostProteinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields= ['protein_id','protein_sequence','protein_length','organism']

class PfamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pfam
        fields = ['pfam_id', 'pfam_description']

class DomainSerializer(serializers.ModelSerializer):
    domain_id = PfamSerializer()
    class Meta:
        model = Domain
        fields = ['domain_id', 'domain_start', 'domain_end', 'domain_description']

class OrganismSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organism
        fields = ['organism_id', 'organism_genus', 'organism_sp', 'organism_clade']

class ProteinSerializer(serializers.ModelSerializer):
    organism = OrganismSerializer()
    domain = DomainSerializer(many=True)
    class Meta:
        model = Protein
        fields = ['protein_id', 'protein_sequence',  'organism', 'protein_length', 'domain']

class ProteinIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ['id', 'protein_id']