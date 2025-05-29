from django.urls import path
from .views import (
    CandidateCreateAPIView,
    CandidateUpdateAPIView,
    CandidateDeleteAPIView,
    CandidateSearchAPIView
)

urlpatterns = [
    path('create/', CandidateCreateAPIView.as_view(), name='candidate-create'),
    path('update/<int:id>/', CandidateUpdateAPIView.as_view(), name='candidate-update'),
    path('delete/<int:id>/', CandidateDeleteAPIView.as_view(), name='candidate-delete'),
    path('search/', CandidateSearchAPIView.as_view(), name='candidate-search'),
]
