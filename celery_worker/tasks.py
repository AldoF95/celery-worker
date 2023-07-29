import os
import time
from celery import Celery
from sklearn.linear_model import LogisticRegression
import pickle

CELERY_BROKER = os.environ.get('CELERY_BROKER', 'redis://redis:6379/0')
CELERY_BACKEND = os.environ.get('CELERY_BACKEND', 'redis://redis:6379/1')
MODEL_PATH = os.environ.get('MODEL_PATH', 'celery_worker\model\logReg_model')

celery =  Celery('tasks', broker=CELERY_BROKER, backend=CELERY_BACKEND)


@celery.task(name='run_prediction', trail=True)
def predict():
    time.sleep(3)
    #data extracted from dataset for testing
    test_data = [6, 148, 72, 35, 0, 33.6, 0.627, 50]
    model = pickle.load(open(MODEL_PATH, 'rb'))
    res = model.predict([test_data])
    return res[0] if res[0] else 404
                        