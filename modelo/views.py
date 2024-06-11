from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import model_from_json
from tcn import tcn
import os

# Create your views here.
loaded_model = open(os.getcwd()+'/assets/ModeloAppDjangoDefinitivo/model.json', "r").read()
reloaded_model = model_from_json(loaded_model, custom_objects={'TCN': tcn.TCN})
reloaded_model.load_weights(os.getcwd()+'/assets/ModeloAppDjangoDefinitivo/weights.h5')
output_shape = reloaded_model.output_shape

@csrf_exempt
def index(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        if "mensaje" in data:
            return JsonResponse({'respuesta':  'Prueba funciona!!'})
        else:
            print("Haciendo prediccion")

            # CON PRESION

            # print("windowsPres ", data['windowsPres'])
            # pres_original = data['windowsPres']
            # dup_pres = np.repeat(pres_original, 10, axis=0)
            # print(len(dup_pres.tolist()))
            # xArrayTensors = [tf.constant([data['windowsAcelX']]), tf.constant([data['windowsAcelY']]), tf.constant([data['windowsAcelZ']]), tf.constant([data['windowsMagX']]), tf.constant([data['windowsMagY']]), tf.constant([data['windowsMagZ']]), tf.constant([data['windowsGirosX']]), tf.constant([data['windowsGirosY']]), tf.constant([data['windowsGirosZ']]), tf.constant([dup_pres.tolist()[:500]])]
            
            # SIN PRESION

            for elem in data:
                print(elem, " --> ", data[elem][:10], "\n")
            
            xArrayTensors = [tf.constant([data['windowsAcelX']]), tf.constant([data['windowsAcelY']]), tf.constant([data['windowsAcelZ']]), tf.constant([data['windowsMagX']]), tf.constant([data['windowsMagY']]), tf.constant([data['windowsMagZ']]), tf.constant([data['windowsGirosX']]), tf.constant([data['windowsGirosY']]), tf.constant([data['windowsGirosZ']])]
            prediction = reloaded_model.predict(xArrayTensors)
            print(prediction)
            predicted_class = np.argmax(prediction[0])
            print(predicted_class)
            return JsonResponse({'respuesta': prediction.tolist(), 'clase': int(predicted_class)})
            # return JsonResponse({'respuesta': [1,2,3,4,5,6,7,8], 'clase': int(8)})
    
    else:
        return JsonResponse({'error': 'Solo se aceptan peticiones POST'})