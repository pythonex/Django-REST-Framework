from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, 
						view_name='snippet-detail',
						read_only='True')
    
    class Meta:
	model = User
	fields = ('url', 'pk', 'username', 'snippets')


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner1 = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
	model = Snippet
	fields = ('url', 'pk','highlight', 'title', 'code', 'linenos', 'language', 'style','owner1')