from flask import Flask, render_template,request,jsonify

print("Starting Flask app...")  # Debug print

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_operation():
    if (request.method == 'POST'):
        operation = request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        
        if (operation=='add'):
            r = num1+num2
            result = ' sum of '+str(num1)+ 'and'+ str(num2) + 'is' +str(r)
        
        if (operation=='substract'):
            r = num1 - num2
            result = ' Difference of '+str(num1)+ 'and'+ str(num2) + 'is' +str(r)

        if (operation=='multiply'):
            r = num1*num2
            result = ' Multiply of '+str(num1)+ 'and'+ str(num2) + 'is' +str(r)  

        if (operation=='division'):
            r = num1 / num2
            result = ' division of '+str(num1)+ 'and'+ str(num2) + 'is' +str(r)  

        return render_template('results.html',result = result)
if __name__ == '__main__':
    print("Running the app...")  # Debug print
    app.run(debug=True)
