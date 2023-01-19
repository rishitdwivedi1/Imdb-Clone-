from django.contrib import admin
from .models import Movies,Actors,Producer
# Register your models here.
@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display=['id','movie','year_of_release','producer','actors','plot']

@admin.register(Actors)
class ActorsAdmin(admin.ModelAdmin):
    list_display=['id','name','gender','dob','bio']
@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display=['id','name','gender','dob','bio']

