from rest_framework import serializers

from .models import user as User
from .models import sudoku as Sudoku
from .models import image as Image

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SudokuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sudoku
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

