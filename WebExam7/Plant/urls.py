from django.urls import path

from WebExam7.Plant.views import plant_create, plant_details, plant_edit, plant_delete

urlpatterns = (
    path('create/', plant_create, name='plant-create'),
    path('details/<int:id>/', plant_details, name='plant-details'),
    path('edit/<int:id>/', plant_edit, name='plant-edit'),
    path('delete/<int:id>/', plant_delete, name='plant-delete'),
)
