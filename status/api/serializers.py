

from rest_framework import serializers

from status.models import Status


class CustomSerializer(serializers.Serializer):
    content=serializers.CharField()
    email= serializers.EmailField()

data={'email':'hello@teamcfe.com','content':"please delete me"}
create_obj_serializer=CustomSerializer(data=data)
if create_obj_serializer.is_valid():
    data=create_obj_serializer.data
    print(data)


class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model=Status
        fields=[
            'user',
            'content',
            'image'
        ]

    def validate_content(self,value):
        if len(value)>1000000:
            raise serializers.ValidationError("This is way too long")
        return value
    
    def validate(self,data):
        content=data.get("content",None)
        if content=="":
            content=None
        
        image=data.get("image",None)
        if content is None and image is None:
            raise serializers.validationError("Content or image is required.")
        return data

