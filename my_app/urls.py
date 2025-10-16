from django.urls import path

from my_app.views.company_views import CreateCompanyView, DeleteCompanyView, GetAllCompaniesView, GetCompanyByIdView, UpdateCompanyView


urlpatterns = [
    path('company/', CreateCompanyView.as_view(), name='create-company'),
    path('companies/', GetAllCompaniesView.as_view(), name='get-all-companies'),
    path('company/<str:company_id>/', GetCompanyByIdView.as_view(), name='get-company-by-id'),
    path('company/<str:company_id>/update/', UpdateCompanyView.as_view(), name='update-company'),
    path('company/<str:company_id>/delete/', DeleteCompanyView.as_view(), name='delete-company'),
]
