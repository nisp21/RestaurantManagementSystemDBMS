# from curses import flash
from flask import  *
import mysql.connector
app=Flask(__name__)
app.secret_key='Nisarg'

@app.route('/')
def homepage():
    return render_template("index.htm")

@app.route('/login',methods=['POST','GET'])
def loginpage():
    if(request.method=='POST'):
        username=str(request.form.get("username"))
        password=str(request.form.get("password"))

        if(username=='Nisarg' and password=='1234567890'):
            conn=mysql.connector.connect(host='localhost',user='root',database='Restaurant2')
            cur=conn.cursor()

            q="select * from Employees"
            cur.execute(q)
            records=cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            return render_template("displayemp.html",data=records)
        
        else: 
            return render_template("login.html",error='Invalid Input!!!')
    return render_template("login.html",error="")

@app.route('/emp',methods=['GET','POST'])
def emppage():
    if(request.method=='POST'):
        name=request.form.get("name")
        surname=request.form.get("surname")
        phone=request.form.get("phone")
        city=request.form.get("city")

        conn=mysql.connector.connect(host='localhost',user='root',database='Restaurant2')
        cur=conn.cursor()
        q = f"insert into Employees(Name,Surname,Phone_no,City) values('{name}','{surname}','{phone}','{city}')"
        cur.execute(q)

        conn.commit()
        cur.close()
        conn.close()
        return render_template("emp.html",message="Successfully added")
    return render_template("emp.html",message="")

# @app.route('/dispemp')
# def displayemp():
    

if __name__=='__main__':
    app.run(debug=True)

