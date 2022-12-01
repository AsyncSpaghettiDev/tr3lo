from django.urls import path
from .views import (
    IssueBoardView,
    IssueDetailView,
    IssueCreateView,
    IssueUpdateView,
    IssueDeleteView,
)

urlpatterns = [
    path('', IssueBoardView.as_view(), name='board'),
    path('create/', IssueCreateView.as_view(), name='create'),
    path('<int:pk>/', IssueDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', IssueUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', IssueDeleteView.as_view(), name='delete'),
]
