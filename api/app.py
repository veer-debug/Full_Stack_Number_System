from flask import Flask ,request,render_template
import requests
from Full_Stack_Number_System.api.convert import Number_system

app=Flask(__name__)

sol=Number_system()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/takenumber',methods= ['GET','POST'])
def priduction():
    if request.method=="POST":
        try:
            if request.form:
                number=request.form['number']
                base1=request.form['base1']
                base2=request.form['base2']
                result=sol.solv(number,base1,base2)
                return render_template('index.html',number=result)

        except Exception as e:
            print (e)
            error={'error':e}
            return render_template('index.html')
    
    else:
        return "Error ....."


if __name__ =="__main__":
    #start_server(main,debug=True)
    #run the app and enable debugging
    app.run(debug=False)
