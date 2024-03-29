from rest_framework import serializers
from home.models import *
import shutil
class FileListSerializer(serializers.Serializer):
    # files = serializers.ListField(
    #     child = serializers.FileField(max_length =1000000,allow_empty_file = False, use_url= False)  
    # )
    files = serializers.ListField(child=serializers.FileField())

    def zip_folder(self, folder):
        shutil.make_archive(f'media/{folder}', 'zip',f'media/{folder}')

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        files_objs = []
        for file in files:
            files_obj = File.objects.create(folder = folder, file = file)
            files_objs.append(files_obj)

        self.zip_folder(folder.uid)
        return {'file':{}, 'folder':str(folder.uid)}