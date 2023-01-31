from django.shortcuts import render
import pickle
import numpy as np


model = pickle.load(open('./model/house_price_pred_model.p','rb'))

# Create your views here.
def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")

def result(request):

    lo = float(request.GET['n1'])
    la = float(request.GET['n2'])
    m_g = float(request.GET['n3'])
    r = float(request.GET['n4'])
    b_r = float(request.GET['n5'])
    p = float(request.GET['n6'])
    h = float(request.GET['n7'])
    m_i = float(request.GET['n8'])

    test_data = np.array([[lo, la, m_g, r, b_r, p, h, m_i]])

    pred = model.predict(test_data)
    pred = pred[0]

    price = "Predicted Price: $ "+str(pred)
    return render(request, "predict.html", {"result2":price})