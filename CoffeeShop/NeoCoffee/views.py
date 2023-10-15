from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from django.shortcuts import render
from django.http import JsonResponse
from .models import Category


# class CategoryListView(generics.ListAPIView):
#     queryset = Category.objects.filter(parent=None)  # Only top-level categories
#     serializer_class = CategorySerializer

# class SubCategoryListView(generics.ListAPIView):
#     serializer_class = CategorySerializer

#     def get_queryset(self):
#         parent_id = self.kwargs['parent_id']
#         return Category.objects.filter(parent_id=parent_id)
    
def show_categories(request):
    return render(request, "categories.html")

def top_categories(request):
    # Retrieve top-level categories (categories without a parent)
    top_cats = Category.objects.filter(parent=None)

    # Serialize the categories
    data = [{"id": cat.id, "name": cat.name} for cat in top_cats]

    # for d in data:
    #     print(d)

    return JsonResponse(data, safe=False)

def sub_categories(request, parent_id):
    # Retrieve sub-categories of the given parent category
    sub_cats = Category.objects.filter(parent__id=parent_id)

    # Serialize the categories
    data = [{"id": cat.id, "name": cat.name} for cat in sub_cats]

    return JsonResponse(data, safe=False)