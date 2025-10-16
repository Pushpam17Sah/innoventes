from django.forms import ValidationError
from my_app.models.company import Company
from my_app.serializers.company_serializer import CompanySerializer
from my_app.utils.utils import get_or_none


class CompanyService:
    @staticmethod
    def create_company(data):
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            return serializer.save(), None
        return None, serializer.errors

    @staticmethod
    def get_all_companies():
        return Company.objects.all()

    @staticmethod
    def get_company_by_id(company_id):
        try:
            return get_or_none(Company, id=company_id)
        except ValidationError:
            return None

    @staticmethod
    def update_company(company_id, data):
        company = CompanyService.get_company_by_id(company_id)
        if not company:
            return None, {'error': 'Company not found.'}

        serializer = CompanySerializer(company, data=data, partial=True)
        if serializer.is_valid():
            return serializer.save(), None
        return None, serializer.errors

    @staticmethod
    def delete_company(company_id):
        company = CompanyService.get_company_by_id(company_id)
        if not company:
            return False, 'Company not found.'
        company.delete()
        return True, None
