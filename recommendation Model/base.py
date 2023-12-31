import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask, render_template, request, redirect, url_for
import pickle
from new import cus_dit, loc_dit
from new import df

# Loading the Model
model = pickle.load(open('model_pred.pkl', 'rb'))
app = Flask(__name__)

def get_prediction(Cusine1, Price, Location):
    Cusine1_encode = cus_dit.get(Cusine1, -1)
    Location_encode = loc_dit.get(Location, -1)
    
    if Cusine1_encode == -1 or Location_encode == -1:
        return None  # Invalid input, return None
    
    arr = np.array([[Cusine1_encode, Location_encode]])
    predict = model.predict(arr)
    
    # Include your logic to calculate other predictions here
    # ...
    
    return predict[0]

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        Cusine1 = request.form['cusine']
        Price = float(request.form['price'])
        Location = request.form['loc']
        
        prediction = get_prediction(Cusine1, Price, Location)
        
        if prediction is not None:
            return render_template('web.html', predict=prediction, predict_1="...", predict_2="...", predict_3="...", predict_4="...", predict_5="...", predict_6="...", prediction_error=False)
        else:
            return render_template('web.html', prediction_error=True)
    
    return render_template('web.html', predict="", predict_1="", predict_2="", predict_3="", predict_4="", predict_5="", predict_6="", prediction_error=False)

@app.route('/predict', methods=['POST', 'GET'])
def web():
    if request.method == 'POST':
        # Include your prediction logic here
        Cusine1 = request.form['cusine']
        Price = float(request.form['price'])
        Location = request.form['loc']
        Cusine1_encode = cus_dit.get(Cusine1, -1)
        Location_encode = loc_dit.get(Location, -1)
        
        if Cusine1_encode == -1 or Location_encode == -1:
            return render_template('web.html', predict="", predict_1="", predict_2="", predict_3="", predict_4="", predict_5="", predict_6="", prediction_error=True)
        
        arr = np.array([[Cusine1_encode, Location_encode]])
        predict = model.predict(arr)
        
        # Include your logic to calculate other predictions here
        # ...
        Cusine1=request.form['cusine']
        Price=float(request.form['price'])
        Location=request.form['loc']
        Cusine1_encode=cus_dit.get(Cusine1,-1)
        Location_encode=loc_dit.get(Location,-1)
        arr=np.array([[Cusine1_encode,Location_encode]])
        predict=model.predict(arr)
        pop_cousine=df[df['location']==Location]['cusines'].value_counts().idxmax()
        pop_loc=df[(df['cusines']==Cusine1) & (df['price']<=Price)]['location'].value_counts().idxmax()
        pop_res=df[df['cusines']==Cusine1]['res_name'].value_counts().idxmax()
        most_pop_res = df[df['location']==Location]['res_name'].value_counts().idxmax()
        pop_serves = df[df['location']==Location]['cusines'].value_counts().idxmax()
        rec_predict=df[df['location']==Location]['price_for_one'].value_counts().idxmax()
        
        return render_template('web.html', predict=round(predict[0]), predict_1=pop_cousine, predict_2=pop_loc, predict_3=pop_serves, predict_4=pop_res, predict_5=most_pop_res, predict_6=rec_predict, prediction_error=False)
    
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)
