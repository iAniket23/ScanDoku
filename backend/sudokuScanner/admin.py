from django.contrib import admin

# Register your models here.
from sudokuScanner.models import user, sudoku

class userAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'numberOfSudokus')

class sudokuAdmin(admin.ModelAdmin):
    list_display = ('id', 'digits', 'user')

admin.site.register(user, userAdmin)
admin.site.register(sudoku, sudokuAdmin)
