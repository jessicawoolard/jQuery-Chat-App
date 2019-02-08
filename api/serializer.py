from rest_framework.serializers import ModelSerializer

from chat.models import Message
# above may not be right.


class MessageSerializer(ModelSerializer):
    model = Message
