from django.http import JsonResponse


def send_fruits(request):
    fruits = [
        {
            "name": "Apfel", 
            "gewicht":150,
            "farbe":"Rot",
            "icon": "🍎"
        },
        {
            "name":"Banane", 
            "gewicht": 120,
            "farbe":"Gelb",
            "icon": "🍌"
        },
        {
            "name": "Orange", 
            "gewicht":160,
            "farbe": "Orange",
            "icon": "🟠"
        },
        {
            "name":"Birne",
            "gewicht": 160,
            "farbe": "Grün",
            "icon": "🍐"
        },
        {
            "name": "Erdbeere",
            "gewicht": 20,
            "farbe": "Rot",
            "icon": "🍓"
        }

    ]
    return JsonResponse(fruits, safe=False)

# Create your views here.
