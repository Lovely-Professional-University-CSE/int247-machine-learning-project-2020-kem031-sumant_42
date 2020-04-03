#importing the necessary modules
from flask import Flask,render_template
from tkinter import *
import work

K_ys=work.d_keys()
feature=work.d_columns()
d_desc=work.d_desc()

app=Flask(__name__)#we know that __name__ =__main__
root=Tk() #creating the tkinter object

@app.route('/')#showing relative path
def hello():
    
    return render_template('index.html')

@app.route('/data_desc')
def data_desc():
    return render_template('data_desc.html',d_desc=d_desc,data=K_ys)
@app.route('/data_see')
def data_see():
    return render_template('data_see.html')
@app.route('/data_modif')
def data_modif():
    return render_template('data_modif.html')
@app.route('/data_vis')
def data_vis():
    return render_template('data_vis.html')
@app.route('/data_imp')
def data_imp():
    return render_template('data_imp.html')
@app.route('/data_models')
def data_models():
    return render_template('data_models.html')


if __name__=='__main__':
    app.run(debug=True,port=5000)
