from flask import *
from DBM import addEmp,selectAllEmp,deleteEmp,selectEmpById,updateEmp,LoginCheck
app = Flask(__name__)

#HOME PAGE
@app.route("/")
def home():
    return render_template("mainpage.html")

#ADMIN LOGIN
@app.route("/admin")
def admin():
    return render_template("adminlogin.html")

@app.route("/adminLoginpage",methods=["POST"])
def adminlogin():
    name=request.form["name"]
    passw=request.form["passw"]
    if(name=="admin" and passw=="jai@123"):
        return redirect("/adminpage")
    else:
        return redirect("/admin")

@app.route("/adminpage")
def adminpage():
    return render_template("admin.html")


#USER LOGIN
@app.route("/login")
def log():
    return render_template("loginpage.html")

@app.route("/LoginCheck",methods=["POST"])
def login():
    name=request.form["name"]
    passw=request.form["passw"]
    d=LoginCheck()
    if((name,passw) in d):
        return redirect("/")
    else:
        return redirect("/login")
        
@app.route("/reg")
def register():
    return render_template("register.html")

#Show Emp
@app.route("/emplist")
def empList():
    d=selectAllEmp()
    return render_template("records.html",elist=d)

#ADD EMP
@app.route("/addEmp" , methods=["POST"])
def add_emp():
    ids=request.form["ids"]
    name=request.form["name"]
    contact=request.form["contact"]
    email=request.form["email"]
    passw=request.form["passw"]


    t=(ids,name,contact,email,passw)
    addEmp(t)

    return redirect("/")

#DEL EMP
@app.route("/delemp")
def dele():
    return render_template("deletemp.html")

@app.route("/deleteEmp" ,methods=["POST"])
def del_emp():
    ids=request.form["id"]
    t=(ids)
    deleteEmp(t)
    return redirect("/emplist")



#UPDATE EMP
@app.route("/updemp")
def upemp():
    return render_template("singlemp.html")

#singleEmp
@app.route("/selectEmpById",methods=["POST"])
def emp():
    ids=request.form["id"]
    t=(ids)
    d=selectEmpById(t)
    return render_template("updatemp.html",elist=d)

@app.route("/updateEmp",methods=["POST"])
def updatemp():
    
    name=request.form["name"]
    contact=request.form["contact"]
    email=request.form["email"]
    passw=request.form["passw"]
    ids=request.form["id"]
  
    t=(name,contact,email,passw,ids)
    updateEmp(t)
    return redirect("/emplist")


if(__name__=="__main__"):
    app.run(debug=True)
