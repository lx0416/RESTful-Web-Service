import factory
from random import randint
from .models import *

class PfamFactory(factory.django.DjangoModelFactory):
    pfam_id = "PF1234"
    pfam_description = "coil prediction"

    class Meta:
        model = Pfam

class OrganismFactory(factory.django.DjangoModelFactory):
    organism_id = 123456
    organism_genus = "Loxosceles"
    organism_sp = "Fuerteventura-Lanzarote"
    organism_clade = "E"

    class Meta:
        model = Organism

class DomainFactory(factory.django.DjangoModelFactory):
    domain_start = randint(1, 100000)
    domain_end = domain_start+randint(1, 10000)
    domain_description = "disorder_prediction"
    domain_id = factory.SubFactory(PfamFactory)

    class Meta:
        model = Domain

class ProteinFactory(factory.django.DjangoModelFactory):
    protein_id = "A0A01234"
    protein_sequence = "abcdefg"
    protein_length = randint(1, 1000)

    organism = factory.SubFactory(OrganismFactory)
    domain = factory.SubFactory(DomainFactory)

    class Meta:
        model = Protein