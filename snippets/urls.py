from django.urls import path

from snippets.views import snippet_create, snippet_delete, snippet_detail, snippet_edit, snippet_list
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', snippet_list, name='snippet_list'),
    path('<int:pk>/', snippet_detail, name='snippet_detail'),
    path('create/', snippet_create, name='snippet_create'),
    path('<int:pk>/edit/', snippet_edit, name='snippet_edit'),
    path('<int:pk>/delete/', snippet_delete, name='snippet_delete'),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
]