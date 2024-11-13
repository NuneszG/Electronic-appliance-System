from django.urls import path
from .views import (
    Home,
    Form,
    Create,
    Edit,
    Update,
    Delete,

)

urlpatterns = [
    path('', Home, name='home'),
    path('form/', Form, name='form'),
    path('Create/', Create, name='create'),
    path('Edit/<int:id>/', Edit, name='edit'),
    path('Update/<int:id>/', Update, name='update'),
    path('Delete/<int:id>/', Delete, name='delete'),

]