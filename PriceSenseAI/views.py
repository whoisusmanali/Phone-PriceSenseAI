import joblib
from django.shortcuts import render
from django.http import JsonResponse

# Load the model (place the correct model path here)
model = joblib.load('/Users/usmanali/Uwindsor/AI/PhonePriceSenseAI/Pickle files/FlipCart_mobile_model(XG).pkl')

# Label encoder dictionary for 'Company Name'
company_encoder = {'POCO': 0, 'realme': 1, 'SAMSUNG': 2, 'OPPO': 3, 'Google': 4, 'vivo': 5,
                   'Nothing': 6, 'REDMI': 7, 'Mi': 8, 'Nokia': 9, 'MOTOROLA': 10,
                   'OnePlus': 11, 'Huawei': 12, 'Nexus': 13, 'Alcatel': 14, 'Lenovo': 15,
                   'Infinix': 16}


def predict_price(request):
    if request.method == 'POST':
        rating = float(request.POST['rating'])
        num_ratings = int(request.POST['num_ratings'])
        company = request.POST['company']
        ram_size = float(request.POST['ram_size'])
        storage_size = float(request.POST['storage_size'])
        battery_size = float(request.POST['battery_size'])

        company_encoded = company_encoder.get(company, 0)

        input_data = [[rating, num_ratings, company_encoded, ram_size, storage_size, battery_size]]

        predicted_price = model.predict(input_data)
        predicted_price = float(predicted_price[0])
        predicted_price = round(predicted_price/62.19,2)

        #return JsonResponse({'predicted_price': predicted_price})
        return render(request, 'PriceSenseAI/index.html', {'prediction': predicted_price})
    else:
        return render(request, 'PriceSenseAI/index.html')
