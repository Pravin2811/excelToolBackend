from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse({'products':serializer.data})
        #return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
'''class ProductView(APIView):
    def post(self, request, *args, **kwargs):
        input_data = request.data

        # Search for existing product with matching details
        existing_products = Product.objects.filter(
            productName=input_data['productName'],
            weight=input_data['weight']
        )

        if existing_products.exists():
            existing_product = existing_products.first()
            serializer = ProductSerializer(existing_product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = ProductSerializer(data=input_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''
        
'''class ProductView(APIView):
    def post(self, request, *args, **kwargs):
        input_data = request.data
 
        # Check for matches in the order of fields
        matching_fields = ['productName', 'hsnCode', 'weight', 'mrp', 'sellPrice', 'gstPercent', 'productCategory']
        matching_products = []

        for field in matching_fields:
            if input_data.get(field):
                matching_products.extend(Product.objects.filter(**{field: input_data[field]}))

        if matching_products:
            # Matches found for one or more fields, return the matched products
            serialized_data = ProductSerializer(matching_products, many=True).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(input_data, status=status.HTTP_404_NOT_FOUND)
        else:
            # No matches found, proceed to create a new product
            serializer = ProductSerializer(data=input_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''
        

'''class ProductView(APIView):
    def post(self, request, *args, **kwargs):
        input_data = request.data

        # Case-insensitive partial matching for productName
        product_name = input_data.get('productName', '')
        matching_products = Product.objects.filter(productName__icontains=product_name)

        if matching_products.exists():
            # If multiple matches found, prioritize by additional criteria
            matching_product = self.get_most_relevant_product(matching_products, input_data)
            serializer = ProductSerializer(matching_product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'No matching product found'}, status=status.HTTP_404_NOT_FOUND)

    def get_most_relevant_product(self, matching_products, input_data):
        # Prioritize based on 'weight'
        weight = input_data.get('weight', '')
        matching_product = None

        for product in matching_products:
            # Check if 'weight' is provided and matches
            if weight and product.weight.lower() == weight.lower():
                return product

        # If 'weight' match is not found, check other criteria
        for product in matching_products:
            # For example, if 'mrp' is provided and matches, use that product
            mrp = input_data.get('mrp', '')
            if mrp and product.mrp.lower() == mrp.lower():
                return product

            # Add more conditions for other fields as needed
            sell_price = input_data.get('sellPrice', '')
            if sell_price and product.sellPrice.lower() == sell_price.lower():
                return product

            # If no match found based on other criteria, use the first matching product
            if not matching_product:
                matching_product = product

        return matching_product'''

class ProductView(APIView):
    def post(self, request, *args, **kwargs):
        input_data_array = request.data

        result_data = []

        for input_data in input_data_array:
            # Case-insensitive partial matching for productName
            product_name = input_data.get('productName', '')
            matching_products = Product.objects.filter(productName__icontains=product_name)

            if matching_products.exists():
                # If multiple matches found, prioritize by additional criteria
                matching_products_list = self.get_matching_products(matching_products, input_data)

                if matching_products_list:
                    # You may want to implement additional logic to choose the most relevant product from the list
                    matching_product = matching_products_list[0]
                    serializer = ProductSerializer(matching_product)
                    result_data.append(serializer.data)
                else:
                    result_data.append({'input': input_data, 'detail': f'No matching product found'})
            else:
                result_data.append({'input': input_data, 'detail': f'No matching product found'})

        return Response(result_data, status=status.HTTP_200_OK)

    def get_matching_products(self, matching_products, input_data):
        # Prioritize based on 'weight'
        weight = input_data.get('weight', '')
        matching_products_list = []

        for product in matching_products:
            # Check if 'weight' is provided and matches
            if weight and product.weight.lower() == weight.lower():
                matching_products_list.append(product)

        # If 'weight' match is not found, check other criteria
        for product in matching_products:
            # For example, if 'mrp' is provided and matches, use that product
            mrp = input_data.get('mrp', '')
            if mrp and product.mrp.lower() == mrp.lower():
                matching_products_list.append(product)

            # Add more conditions for other fields as needed
            sell_price = input_data.get('sellPrice', '')
            if sell_price and product.sellPrice.lower() == sell_price.lower():
                matching_products_list.append(product)

        return matching_products_list