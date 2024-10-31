# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration

    # path for login
     path(route='login', view=views.login_user, name='login'),
     # Path for logout
     path(route='logout', view=views.logout_request, name='logout'),
    # path for dealer reviews view
     path(route='register', view=views.registration, name='register'),
     # path for get_dealership
     path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),
     path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
     # Path for get_dealer_details
     path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),
    # Path for get_dealer_reviews
     path('dealer_reviews/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),
    # path for get_cars
     path('get_cars/', views.get_cars, name='get_cars'),
    # path for add a review view
     path(route='add_review', view=views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
