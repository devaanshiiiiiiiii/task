from flask import Flask ,render_template,request,redirect,url_for
from flask_mysqldb import MySQL



app=Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = "devanshi_19"
app.config['MYSQL_DB'] = 'project'

mysql=MySQL(app)

@app.route("/") # this is the address of the function which we define below , it simply works of fcfs
def home():
    return render_template('index.html')

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form["e_mail"]
        password=request.form["_password_"]

        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM register WHERE e_mail =  %s AND password_= %s", (email,password,))
        existing_user = cursor.fetchone()
        cursor.connection.commit()
        cursor.close()
        if existing_user:
            return render_template("main.html")
        
    return render_template("login.html")

@app.route("/login1")
def login1():
    return render_template("login1.html")

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form['u_name']
        email=request.form["email"]
        password=request.form["password"]
        cursor=mysql.connection.cursor()

        cursor.execute("SELECT * FROM register WHERE e_mail = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            return render_template('login1.html', message="You are already registered. Please login.")
        else:
            cursor.execute(''' insert into register (user_name,e_mail,password_) values(%s,%s,%s)''',(name,email,password))
            cursor.connection.commit()
            cursor.close()
            return redirect(url_for("login"))
        
    return render_template("register.html")
@app.route("/main")
def main():
    return render_template("main.html")
@app.route("/subs",methods=["GET","POST"])
def subs():
    if request.method=="POST":
        title=request.form["plans"]
        desc=request.form["desc"]
        cursor=mysql.connection.cursor()
        cursor.execute(''' insert into subscribers (title,description_) values(%s,%s)''',(title,desc))
        cursor.connection.commit()
        cursor.close()
    return render_template("subscribe.html")

if __name__=="__main__":
    app.run(debug=True,host="127.0.0.1") 