from django.contrib import admin

# Register your models here.
from sudokuScanner.models import user, sudoku, image

class userAdmin(admin.ModelAdmin):
    list_display = ('userID','username', 'password')

class sudokuAdmin(admin.ModelAdmin):
    list_display = ('sudokuID', 'row1', 'row2', 'row3', 'row4', 'row5', 'row6', 'row7', 'row8', 'row9', 'user')

class imageAdmin(admin.ModelAdmin):
    list_display = ('imageID', 'imageValue')

admin.site.register(user, userAdmin)
admin.site.register(sudoku, sudokuAdmin)
admin.site.register(image, imageAdmin)

