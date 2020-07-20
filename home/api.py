from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Q
from tamil import utf8
# Create your views here.

import json
from .models import Word
from .serializer import WordSerializer


class WordList(APIView):
    def get(self, request):
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class LongestWordList(APIView):
    def get(self, request, n):
        words = Word.objects.all().order_by('-length')[:n]
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class MostFrequentWordList(APIView):
    def get(self, request, n):
        words = Word.objects.all().order_by('-frequency')[:n]
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class SmallestWordList(APIView):
    def get(self, request, n):
        words = Word.objects.all().order_by('length')[:n]
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class LeastFrequentWordList(APIView):
    def get(self, request, n):
        words = Word.objects.all().order_by('frequency')[:n]
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class SearchWithWordList(APIView):
    def get(self, request, x):
        words = Word.objects.filter(word=x)

        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class WordContainsWordList(APIView):

    def get(self, request, x):
        query = Q()
        query = Q(word__icontains=x)
        words = Word.objects.filter(query).all()
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class StartWithWordList(APIView):

    def get(self, request, x):
        query = Q()
        query = Q(word__startswith=x)
        words = Word.objects.filter(query).all()
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)

    def post(self):
        pass
