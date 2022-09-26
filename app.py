from flask import Flask, render_template, request,redirect
import pickle
import numpy as np

model = pickle.load(open('iri.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/predict', methods=['POST'])
def home():
    if request.method=='POST':
        data1 = request.form['a']
        data2 = request.form['b']
        data3 = request.form['c']
        data4 = request.form['d']
        arr = np.array([[data1, data2, data3, data4]])
        pred = model.predict(arr)
        return render_template('after.html', data=pred)
    else:
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
    















