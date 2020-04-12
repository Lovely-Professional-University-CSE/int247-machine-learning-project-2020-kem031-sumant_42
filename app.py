#importing the necessary modules
from flask import Flask,render_template

import work#this file consist of function returnig data regarding our model
content=work.context
ins=work.insp
app=Flask(__name__)#we know that __name__ =__main__ which triggers flask to run on main

#get data from the work on rape cases
d_rape_col=work.get_col_rape()
d_rape_head=work.get_dataR_head()


@app.route('/')
def start_main():
    return render_template('data_desc.html',data=content,ins=ins)

#This is responsible for showing the description about our data
@app.route('/data_desc')
def data_desc():
    return render_template('data_desc.html',data=content,ins=ins)

#This is responsible for taking data and showing to our webpage (It is dynamic process)
@app.route('/data_see')
def data_see():
    return render_template('data_see.html',data=d_rape_col,content=d_rape_head)


#this helps us to visualize our data to the web page
@app.route('/data_vis')
def data_vis():
    return render_template('data_vis.html')


#this is implementation of our jupyter notebook on webpage
@app.route('/notebook')
def notebook():
    return render_template('p1.html')

#this helps to debug our flask webpage in case or error
if __name__=='__main__':
    app.run(debug=True,port=5000)
