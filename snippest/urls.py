from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippest import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetails.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
