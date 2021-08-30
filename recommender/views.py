from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from recommender.models import Movies
import pandas as pd
import numpy as np
from collections import defaultdict

def index(request):
    return render(request,'index.html')

def get(request):
    if 'n' not in request.GET:
        return render(request, 'get.html')
    else:

        df = pd.read_csv('ratings_small.csv')
        if request.GET['n'] == '':
            return render(request, 'get.html', {'error' : 'Input error!!'})
        num = int(request.GET['n'])
        if num >len(df): num = len(df)
        for i in range(num):
            if Movies.objects.filter(userId = df.iloc[i]['userId'], movieId = df.iloc[i]['movieId']).count() == 0:
                m = Movies(userId = df.iloc[i]['userId'], movieId = df.iloc[i]['movieId'], rating = df.iloc[i]['rating'])
                m.save()
        movies = Movies.objects.all()
        if len(movies) > 0:
            return render(request, 'get_n.html', locals())
        else:
            return render(request, 'get.html', {'error' : 'Database is empty.'})

def delete(request):
    if 'ok' in request.POST:
        if request.POST['userID']=='' or request.POST['movieID'] == '':
            return render(request, 'delete.html', {'error' : 'Input error!!'})
        if Movies.objects.filter(userId = request.POST['userID'], movieId = request.POST['movieID']).count() == 0:
            return render(request, 'delete.html', {'error' : 'userID or movieID is not exist.'})
        data = Movies.objects.get(userId = request.POST['userID'], movieId = request.POST['movieID'])
        data.delete()
        return render(request, 'delete.html', {'success' : 'Delete successful.'})
    else:
        return render(request, 'delete.html')

def watched(request):
    if 'userID' in request.POST:
        if request.POST['userID'] == '':
            return render(request, 'watched.html', {'error' : 'Input error!!'})
        if Movies.objects.filter(userId = request.POST['userID']).count() == 0:
            return render(request, 'watched.html', {'error' : "UserId doesn't exist."})
        watched_movie = Movies.objects.filter(userId = request.POST['userID'])
        return render(request, 'watched.html', locals())
    else:
        return render(request, 'watched.html')

def modify(request):
    if 'ok' in request.POST:
        if request.POST['userID']=='' or request.POST['movieID'] == '' or request.POST['rating'] == '':
            return render(request, 'modify.html', {'error' : 'Input error!!'})
        if Movies.objects.filter(userId = request.POST['userID'], movieId = request.POST['movieID']).count() == 0:
            return render(request, 'modify.html', {'error' : "UserId or moveId doesn't exist."})
        data = Movies.objects.get(userId = request.POST['userID'], movieId = request.POST['movieID'])
        if int(request.POST['rating']) > 5.0:
            data.rating = 5.0
        else:
            data.rating = int(request.POST['rating'])
        data.save()
        return render(request, 'modify.html', {'success' : "Modify successful."})
    else:
        return render(request, 'modify.html')

def recommend(request):
    if 'userID' in request.POST:
        if request.POST['userID'] == '':
            return render(request, 'recommend.html', {'error' : 'Input error!!'})
        df = pd.read_csv('recommend.csv')
        if request.POST['userID'] not in df.columns:
            return render(request, 'recommend.html', {'error' : "UserId doesn't exist."})

        movies = df[int(request.POST['userID'])]
        return render(request, 'recommend_2.html', locals())
    else:
        return render(request, 'recommend.html')
