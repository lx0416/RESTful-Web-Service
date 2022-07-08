from django.urls import reverse
from rest_framework.test import APITestCase
from .model_factories import *
from .serializers import *

class PfamSerialiserTest(APITestCase):
    pfam1 = None
    pfamserializer = None

    def setUp(self):
        self.pfam1 = PfamFactory.create(pfam_id="PF1234", pfam_description="pfamd1")
        self.pfamserializer = PfamSerializer(instance=self.pfam1)

    def test_pfamSerilaiserFields(self):
        data = self.pfamserializer.data
        self.assertEqual(set(data.keys()), set(['pfam_id', 'pfam_description']))

    def test_pfamSerilaiserData(self):
        data = self.pfamserializer.data
        self.assertEqual(data['pfam_id'], "PF1234")

    def test_pfamDetailReturnsSuccess(self):
        url = reverse('pfam_details', kwargs={'pfam_id':'PF1234'})
        response = self.client.get(url)
        response.render()
        self.assertEqual(response.status_code, 200)

    def test_pfamDetailReturnsFailOnBadID(self):
        url = "api/pfam/H"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class OrganismSerialiserTest(APITestCase):
    org1 = None
    orgserializer = None

    def setUp(self):
        self.org1 = OrganismFactory.create(organism_id=123456, organism_genus = "Loxosceles", organism_sp = "Fuerteventura-Lanzarote", organism_clade = "E")
        self.orgserializer = OrganismSerializer(instance=self.org1)

    def test_orgSerilaiserFields(self):
        data = self.orgserializer.data
        self.assertEqual(set(data.keys()), set(['organism_id', 'organism_genus', 'organism_sp', 'organism_clade']))

    def test_orgSerilaiserData(self):
        data = self.orgserializer.data
        self.assertEqual(data['organism_id'], 123456)

    def test_orgDetailReturnsSuccess(self):
        url = reverse('pfam_details_from_OID', kwargs={'organism_id':123456})
        response = self.client.get(url)
        response.render()
        self.assertEqual(response.status_code, 200)

    def test_orgDetailReturnsFailOnBadID(self):
        url = "api/pfams/H"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

class DomainSerialiserTest(APITestCase):
    pfam1 = None
    dom1 = None
    domserializer = None

    def setUp(self):
        self.pfam1 = PfamFactory.create(pfam_id="PF1234")
        self.dom1 = DomainFactory.create(domain_id=self.pfam1, domain_start = 1, domain_end = 2, domain_description = "abcdefg")
        self.domserializer = DomainSerializer(instance=self.dom1)

    def test_domSerilaiserFields(self):
        data = self.domserializer.data
        self.assertEqual(set(data.keys()), set(['domain_id', 'domain_start', 'domain_end', 'domain_description']))

    def test_domSerilaiserData(self):
        data = self.domserializer.data
        self.assertEqual(data['domain_description'], "abcdefg")

class ProteinSerialiserTest(APITestCase):
    protein = None
    domain = None
    pfam = None
    organism = None
    proteinserialiser = None

    # def setUp(self):
    #     self.pfam = PfamFactory.create(pfam_id="PF1234")
    #     self.domain = DomainFactory.create(domain_id=self.pfam, domain_start = 1, domain_end = 2, domain_description = "abcdefg")
    #     self.organism = OrganismFactory.create(organism_id=123456, organism_genus = "Loxosceles", organism_sp = "Fuerteventura-Lanzarote", organism_clade = "E")
    #     self.protein = ProteinFactory.create(protein_id="A0A01234", protein_sequence="abcdefg", protein_length=1, organism=self.organism, domain=self.domain)
    #     self.proteinserializer = ProteinSerializer(instance=self.protein)

    def test_proteinDetailReturnFailOnBadID(self):
        url = "api/protein/H"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # def test_proteinDetailReturnsSuccess(self):
    #     self.pfam = PfamFactory.create(pfam_id="PF1234")
    #     self.domain = DomainFactory.create(domain_id=self.pfam, domain_start = 1, domain_end = 2, domain_description = "abcdefg")
    #     self.organism = OrganismFactory.create(organism_id=123456, organism_genus = "Loxosceles", organism_sp = "Fuerteventura-Lanzarote", organism_clade = "E")
    #     self.protein = ProteinFactory.create(protein_id="A0A01234", protein_sequence="abcdefg", protein_length=1, organism=self.organism)
    #     self.protein.save()
    #     self.protein.domain.add(self.domain)

    #     url = reverse('getProtein', kwargs={'protein_id':"A0A01234"})
    #     response = self.client.get(url)
    #     response.render()
    #     self.assertEqual(response.status_code, 200)
