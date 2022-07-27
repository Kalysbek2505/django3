from rest_framework.decorators import api_view
from Test1.models import Post
from rest_framework.response import Response

from config.serializers import PostSerializer

@api_view(['GET'])
def posts_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)