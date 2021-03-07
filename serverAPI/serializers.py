from rest_framework import serializers
# from serverAPI.models import Users
from haq.models import *

# We won't use below, because we are directly getting data from JSON file
# or if we were dealing directly with database then we use below
class TopicsSerializer(serializers.ModelSerializer):

    #  below require=False will work when we will be updating data, it wont ask all fields
    _topic = serializers.CharField(required=False)

    
    class Meta:
        model = Topic
        fields = '__all__'  # by this we can fetch all the FIELDS
        #  if to display only specifics fields then we have to do like as below
        # fields = ('name', 'employee_id') # this is a ways to get specific FIELDS