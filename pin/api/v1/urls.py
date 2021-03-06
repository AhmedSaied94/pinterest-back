
from django.http.response import HttpResponse
from django.urls import path, include
from django.conf import settings
from . import views


urlpatterns = [

    #path('', hello_world),
    ## Pin URLs
    #Create
    path('create', views.pin_create),
    path('link_board', views.link_board),

    #Read
    ## List all Pins 
    path('pins/', views.pin_list),
    ## List a specific pin 
    path('<int:pk>/', views.single_pin),
    ## List a users' pins
    path('<int:user_id>/', views.user_pins),

    #Update
    path('update/<int:pk>/', views.update_pin),

    #Delete
    path('delete/<int:pk>/', views.delete_pin),

    ## Note URLS
    # Create
    path('<int:pin_id>/pin_notes', views.note_create),

    #Update
    path('<int:pin_id>/pinnote/update/<int:pk>/', views.update_note),

     #Delete
    path('<int:pin_id>/pinnote/delete/<int:pk>/', views.delete_note),

     ## Category URLS
    # Create
    path('<int:pin_id>/pin_categories', views.category_create),

    #Update
    path('<int:pin_id>/pincategory/update/<int:pk>/', views.update_category),

     #Delete
    path('<int:pin_id>/pincategory/delete/<int:pk>/', views.delete_category),


     ## Section URLS
    # Create
    path('<int:pin_id>/pin_sections', views.section_create),

    #Update
    path('<int:pin_id>/pinsection/update/<int:pk>/', views.update_section),

     #Delete
    path('<int:pin_id>/pinsection/delete/<int:pk>/', views.delete_section),



] 
