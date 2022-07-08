from django.contrib import admin
from django.urls import include, path
from . import api

urlpatterns = [
    path('api/protein/<str:protein_id>',api.GetProtein.as_view(), name='getProtein'),
    path('api/pfam/<str:pfam_id>',api.PfamDetails.as_view(), name='pfam_details'),
    path('api/pfams/<int:organism_id>', api.OrgDetailFromOrganismID.as_view(), name='pfam_details_from_OID'),
    path('api/proteins/<int:organism_id>', api.GetProteinFromOrg.as_view(), name='get_protein_from_org'),
    path('api/coverage/<str:protein_id>', api.Coverage.as_view(), name='coverage'),
    path('api/protein', api.PostProtein.as_view(), name='post_protein'),
]