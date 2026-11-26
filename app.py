from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def home(_):
    return render_template('index.html\')
 @app.route('/')
def name():
   name=request.form['student_name']
   cgpa=request.form['student_cgpa']
   remarks=request.form['student_remarks']
   return F"regestration successfull!welcome"                         
                           if __name__='__main__':
                           app.run(debug=True)