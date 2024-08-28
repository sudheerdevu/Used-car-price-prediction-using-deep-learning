from django.shortcuts import render
import pickle

# Create your views here.
def predict(request):
        if request.method == 'POST':
            year = int(request.POST['year'])
            present_price = float(request.POST['present_price'])
            kms_driven = int(request.POST['kms_driven'])
            car_price_model_path = 'app/Annmodel.pkl'
            car_price_model = pickle.load(
                open(car_price_model_path, 'rb'))
            my_prediction = car_price_model.predict([[year, present_price, kms_driven, 0,0,1,1,1]])
            final_prediction = my_prediction[0]
            print(final_prediction)
            if final_prediction and final_prediction>present_price:
                final_prediction/=10
            return render(request, 'predict.html', {'final_prediction': final_prediction})
        return render(request, 'predict.html')