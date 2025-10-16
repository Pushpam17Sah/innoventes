from rest_framework import serializers

from my_app.models.company import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'email', 'code', 'strength',
                  'website_url', 'created_at', 'updated_at']

    def validate_code(self, value):
        if len(value) != 5:
            raise serializers.ValidationError(
                "Code must be exactly 5 characters long.")
        if not (value[0].isalpha() and value[1].isalpha()):
            raise serializers.ValidationError(
                "The first two characters must be alphabets.")
        if not (value[2].isdigit() and value[3].isdigit()):
            raise serializers.ValidationError(
                "The third and fourth characters must be digits.")
        if value[4] not in ['E', 'N']:
            raise serializers.ValidationError(
                "The fifth character must be either 'E' or 'N'.")
        return value
