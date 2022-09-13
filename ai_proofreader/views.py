from rest_framework.views import APIView, Response
from rest_framework import status
from .utils import ai_proofreading
from .serializers import ProofreadingSerializers


class ProofreaderAPIView(APIView):
    """
    API View to get word and send

    :parameter: string-> word
    example:

    {
        "word": "Hello There"
    }

    """
    serializer_class = ProofreadingSerializers

    def post(self, request, *args, **kwargs):
        word = request.data.get('word', '')
        return Response(ai_proofreading(word), status=status.HTTP_200_OK)
