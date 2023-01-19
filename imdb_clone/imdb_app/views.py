from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework.parsers import JSONParser 
from django.http.response import JsonResponse
from .models import Movies,Actors,Producer
from .serializer import MovieSerializer,ActorSerializer,ProducerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

# Create your views here.
@csrf_exempt 

def get_all_movies_details(request):
    if request.method=="GET":
        movie_list=Movies.objects.all()
        movie_list=MovieSerializer(movie_list,many=True)

        movie_list=movie_list.data
        print(type(movie_list))
        movie_list=json.dumps(list(movie_list), indent=4, sort_keys=True, default=str)

        return HttpResponse(movie_list,content_type='application/json')


def get_all_actor_details(request):
    if request.method=="GET":
        actor_list=Actors.objects.all().values()
        print(actor_list)

        actor_list=json.dumps(list(actor_list), indent=4, sort_keys=True, default=str)
        print(actor_list)
        return HttpResponse(actor_list,content_type='application/json')


def get_all_producer_details(request):
    if request.method=="GET":
        producer_list=Producer.objects.all().values()
        print(producer_list)
   
        producer_list=json.dumps(list(producer_list), indent=4, sort_keys=True, default=str)
        print(producer_list)
        return HttpResponse(producer_list,content_type='application/json')
        

@csrf_exempt 
@api_view(('POST',))

def add_movies( request):
      
      if request.method=="POST":
         data=request.data 
         producer=data["producer"]
         producer_obj=Producer.objects.get(name=producer["name"])
         new_movie=Movies.objects.create(movie=data["movie"],year_of_release=data["year_of_release"],producer=producer_obj,plot=data["plot"])
         new_movie.save()


         for actor in data["actor"]:
            actor_obj=Actors.objects.get(name=actor["name"])
            new_movie.actor.add(actor_obj)

     
        #  new_movie.producer.add(producer_obj)
         serializer=MovieSerializer(new_movie)
         return Response(serializer.data)
@csrf_exempt
@api_view(('POST',))

def add_actor(request):
    if request.method=="POST":
        data=request.data 
        new_actor=Actors.objects.create(name=data["name"],dob=data["dob"],gender=data["gender"],bio=data["bio"])
        new_actor.save()
        serializer=ActorSerializer(new_actor)
        return Response(serializer.data)

    else:   
      return Response(status=status.HTTP_400_BAD_REQUEST)

      
@csrf_exempt
@api_view(('POST',))

def add_producer(request):
    if request.method=="POST":
        data=request.data 
        new_producer=Producer.objects.create(name=data["name"],dob=data["dob"],gender=data["gender"],bio=data["bio"])
        new_producer.save()
        serializer=ProducerSerializer(new_producer)
        return Response(serializer.data)

 
@csrf_exempt
@api_view(('DELETE',))

def delete_movie(request,id):
    if request.method=="DELETE":
     try: 
        movie_object = Movies.objects.get(id=id)
        movie_object.delete() 
        return JsonResponse({'message': 'Movie was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
     
     except Movies.DoesNotExist: 
        return JsonResponse({'message': ' Movie  id does not exists'}, status=status.HTTP_404_NOT_FOUND)  

    
    else:   
      return Response(status=status.HTTP_400_BAD_REQUEST)     
        
@csrf_exempt
@api_view(('DELETE',))

def delete_actor(request,id):
    if request.method=="DELETE":
     try: 
        actor_object = Actors.objects.get(id=id)
        actor_object.delete() 
        return JsonResponse({'message': 'Actor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
     
     except Movies.DoesNotExist: 
        return JsonResponse({'message': ' Actor id does not exists'}, status=status.HTTP_404_NOT_FOUND)  

    
    else:   
      return Response(status=status.HTTP_400_BAD_REQUEST) 

@csrf_exempt
@api_view(('DELETE',))

def delete_producer(request,id):
    if request.method=="DELETE":
     try: 
        producer_object = Producer.objects.get(id=id)
        producer_object.delete() 
        return JsonResponse({'message': 'Producer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
     
     except Movies.DoesNotExist: 
        return JsonResponse({'message': ' Producer id does not exists'}, status=status.HTTP_404_NOT_FOUND)  

    
    else:   
      return Response(status=status.HTTP_400_BAD_REQUEST) 

@csrf_exempt
@api_view(('PUT',))

def update_movie(request):
    if request.method=="PUT":
        data=request.data 
        # actor=Movies.objects.get(id=data["id"]).remove()

        movie_object=Movies.objects.get(id=data["id"])
        movie_object.actor.remove()
        movie_object.movie=data["movie"]
        movie_object.year_of_release=data["year_of_release"]
        movie_object.plot=data["plot"]
        producer=data["producer"]
        producer_obj=Producer.objects.get(name=producer["name"])
        movie_object.producer=producer_obj
        # movie_object.actor.delete()
        # print(actor)
        for actor in data["actor"]:
            actor_obj=Actors.objects.get(name=actor["name"])
            movie_object.actor.add(actor_obj)
        movie_object.save()
        serializer=MovieSerializer(movie_object)
   
        return Response(serializer.data)

@csrf_exempt
@api_view(('PUT',))

def update_actor(request):
    if request.method=="PUT":
        data=request.data 

        actor_object=Actors.objects.get(id=data["id"])
        actor_object.name=data["name"]
        actor_object.dob=data["dob"]
        actor_object.gender=data["gender"]
        actor_object.bio=data["bio"]

       
        actor_object.save()
        serializer=ActorSerializer(actor_object)
   
        return Response(serializer.data)

@csrf_exempt
@api_view(('PUT',))

def update_producer(request):
    if request.method=="PUT":
        data=request.data 

        producer_object=Producer.objects.get(id=data["id"])
        producer_object.name=data["name"]
        producer_object.dob=data["dob"]
        producer_object.gender=data["gender"]
        producer_object.bio=data["bio"]

       
        producer_object.save()
        serializer=ProducerSerializer(producer_object)
   
        return Response(serializer.data)





        



       
   

