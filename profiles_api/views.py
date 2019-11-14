from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIview features"""
        an_apiview = [
            'Uses HTTP methods to get, post',
            'is similar to traditional jango view',
            'gives you the most control over the logic',
            'mapped manually to URLs',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
