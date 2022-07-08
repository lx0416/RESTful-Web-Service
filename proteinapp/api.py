from django.views.generic.detail import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import mixins

class PostProtein(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Protein.objects.all()
    serializer_class = PostProteinSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class GetProtein(APIView):
    def get(self, request, protein_id, many=True):
        protein = Protein.objects.get(protein_id=protein_id)
        serializers = ProteinSerializer(protein)
        return Response(serializers.data)

class OrgDetailFromOrganismID(APIView):
    def get(self, request, organism_id):
        organism_id = Organism.objects.get(organism_id=organism_id)
        proteins = Protein.objects.filter(organism=organism_id)
        pfam = []
        for protein in proteins:
            domainId = protein.domain.all()
            for domain in domainId:
                pfam_description =domain.domain_id.pfam_description
                pfam_id = domain.domain_id
                pfam.append({'pfam_id':pfam_id,'pfam_description':pfam_description})
        serializers = PfamSerializer(pfam,many=True)
        return Response(serializers.data)

class Coverage(APIView):
    def get(self, request, protein_id):
        proteins = Protein.objects.get(protein_id=protein_id)
        sum=0
        coverage = []
        protein_length = proteins.protein_length
        domainId = proteins.domain.all()
        sum = 0 
        for domain in domainId: 
            domain_end = domain.domain_end
            domain_start = domain.domain_start
            sum += (domain_end- domain_start)
            coverage = sum/protein_length
        return Response(coverage)

class GetProteinFromOrg(APIView):
    def get(self, request, organism_id):
        organism_id = Organism.objects.get(organism_id=organism_id)
        proteins = Protein.objects.filter(organism=organism_id)
        pro = []
        for protein in proteins:
            pro.append(Protein.objects.get(protein_id=protein))
        serializer = ProteinIDSerializer(pro, many=True)
        return Response(serializer.data)

class PfamDetails (APIView):
    def get(self, request, pfam_id):
        pfamid = Pfam.objects.get(pfam_id=pfam_id)
        serializers = PfamSerializer(pfamid)
        return Response(serializers.data)