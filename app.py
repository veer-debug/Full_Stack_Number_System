from flask import Flask ,request,render_template
import requests
from convert import Number_system

app=Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/takenumber',methods= ['GET','POST'])
def priduction():
    if request.method=="POST":
        try:
            if request.form:
                number=request.form['number']
                base=request.form['base']
                print(number) 
                print(base)
                status=True
                
                return render_template('index.html',number=number,base=base)

        except Exception as e:
            error={'error':e}
            print(e)
            return render_template('index.html')
    
    else:
        return "Error ....."




app.run(debug=True)