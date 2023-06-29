from django.urls import path
from .views import HomePageView, MachinePageView, MachineDetailView, NewStatusView, UpdateStatusView, \
    DeleteStatusView, DocumentListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('machines/', MachinePageView.as_view(), name='machines'),
    path('machine/<int:pk>/', MachineDetailView.as_view(), name='machine_detail'),
    path('new/', NewStatusView.as_view(), name='new_status'),
    path('machine/<int:pk>/update/', UpdateStatusView.as_view(), name='update_status'),
    path('machine/<int:pk>/delete/', DeleteStatusView.as_view(), name='delete_status'),
    path('machines/documents/', DocumentListView.as_view(), name='documents'),
]
