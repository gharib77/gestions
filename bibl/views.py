from django.shortcuts import render
from django.http import HttpResponse
from bibl.models import Personne
from bibl.forms import FormPers
from bibl.filters import FpersFilter
# Create your views here.
def index(request):
    personnes = Personne.objects.all()
    filter = FpersFilter(request.GET, queryset=personnes)

    return render(request, 'index.html', {'filter': filter})
    
