from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from my_app.builders.response_builder import ResponseBuilder
from my_app.serializers.company_serializer import CompanySerializer
from my_app.services.company_service import CompanyService
from my_app.utils.pagination import StandardResultsSetPagination


class GetAllCompaniesView(ListAPIView):
    serializer_class = CompanySerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return CompanyService.get_all_companies()


class GetCompanyByIdView(APIView):
    def get(self, request, company_id):
        company = CompanyService.get_company_by_id(company_id)
        if not company:
            return ResponseBuilder().fail().not_found_404().message("Company not found.").get_response()
        serializer = CompanySerializer(company)

        return ResponseBuilder().success().result_object(serializer.data).message("Company retrieved successfully.").get_response()


class CreateCompanyView(APIView):
    def post(self, request):
        company, errors = CompanyService.create_company(request.data)
        if errors:
            return ResponseBuilder().fail().bad_request_400().message("Invalid data.").result_object(errors).get_response()
        serializer = CompanySerializer(company)

        return ResponseBuilder().success().result_object(serializer.data).message("Company created successfully.").get_response()


class UpdateCompanyView(APIView):
    def put(self, request, company_id):
        company, errors = CompanyService.update_company(
            company_id, request.data)
        if errors:
            return ResponseBuilder().fail().bad_request_400().message("Invalid data or Company not found.").result_object(errors).get_response()
        serializer = CompanySerializer(company)

        return ResponseBuilder().success().result_object(serializer.data).message("Company updated successfully.").get_response()


class DeleteCompanyView(APIView):
    def delete(self, request, company_id):
        success, error = CompanyService.delete_company(company_id)
        if error:
            return ResponseBuilder().fail().not_found_404().message(error).get_response()

        return ResponseBuilder().success().message("Company deleted successfully.").get_response()
