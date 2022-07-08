import os
import sys
import django
import csv
from collections import defaultdict

# set path
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
sys.path.append(PROJECT_ROOT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proteinweb.settings')
django.setup()

from proteinapp.models import *
datafile1 = './csv/assignment_data_sequences.csv'
datafile2 = './csv/assignment_data_set.csv'
datafile3 = './csv/pfam_descriptions.csv'

# Pfam data
with open(datafile3) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader:
        # Pfam
        if Pfam.DoesNotExist:
            record = Pfam.objects.create(pfam_id=row[0], pfam_description=row[1])
            record.save()

# Domain data
with open(datafile2) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        pfam = Pfam.objects.get(pfam_id=row[5])
        if Domain.objects.filter(domain_id=pfam).exists():
            Domain.objects.get(domain_id=pfam)
        elif Domain.DoesNotExist:
            record = Domain.objects.create(domain_id=pfam, domain_description=row[4], domain_start=row[6], domain_end=row[7])
            record.save()

# Organism data
with open(datafile2) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if Organism.objects.filter(organism_id=row[1]).exists():
            Organism.objects.get(organism_id=row[1])
        elif Organism.DoesNotExist:
            sci = row[3].split(" ")
            if len(sci) == 2: # if scientific name equals 2 words
                genus = sci[0]
                sp = sci[1]
            elif len(sci) > 2: # if scientific name more than 2 words
                for i in range(len(sci)):
                    if sci[i] == 'sp.':
                        g = sci[:i]
                        s = sci[i+1:]
                genus = ""
                for i in g: # form genus
                    genus += i
                    genus += " "
                sp = ""
                for i in s: # form species
                    sp += i
                    sp += " "
            else:
                print("f")
            record = Organism.objects.create(organism_id=row[1], organism_clade=row[2], organism_genus=genus, organism_sp=sp)
            record.save()

# Protein data
temp = []
with open(datafile1) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader:
        # Protein
        if Protein.objects.filter(protein_id=row[0]).exists():
            Protein.objects.get(protein_id=row[0])
        elif Protein.DoesNotExist:
            temp.append([row[0], row[1]])

with open(datafile2) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader:
        # Protein
        if Protein.objects.filter(protein_id=row[0]).exists(): # for adding additional domains to existing protein
            protein = Protein.objects.get(protein_id=row[0])
            domainId = Domain.objects.get(domain_id=Pfam.objects.get(pfam_id=row[5]))
            protein.domain.add(domainId)
            protein.save()
        elif Protein.DoesNotExist:
            idprotein = row[0]
            seq = None
            for i in temp: 
                if i[0] == row[0]: # if protein_id in datafile1 matches protein_id in datafile2
                    idprotein = row[0]
                    seq = i[1]
            record = Protein.objects.create(protein_id=idprotein, protein_sequence=seq, protein_length=row[8], organism=Organism.objects.get(organism_id=row[1]))
            domainId = Domain.objects.get(domain_id=Pfam.objects.get(pfam_id=row[5]))
            record.domain.add(domainId)
            record.save()            