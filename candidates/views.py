from rest_framework import generics
from django.db.models import Case, When, Value, IntegerField, F
from django.db.models.functions import Lower
from .models import Candidate
from .serializers import CandidateSerializer
from django.db.models import Sum

class CandidateCreateAPIView(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    lookup_field = 'id'

class CandidateDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    lookup_field = 'id'




class CandidateSearchAPIView(generics.ListAPIView):
    serializer_class = CandidateSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if not query:
            return Candidate.objects.all()

        words = query.lower().split()
        qs = Candidate.objects.all()

        for idx, word in enumerate(words):
            qs = qs.annotate(**{
                f"match_{idx}": Case(
                    When(name__icontains=word, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField()
                )
            })

        relevance_expr = None
        for idx in range(len(words)):
            field = F(f"match_{idx}")
            relevance_expr = field if relevance_expr is None else relevance_expr + field

        qs = qs.annotate(relevance=relevance_expr)

        return qs.filter(relevance__gt=0).order_by('-relevance', 'name')