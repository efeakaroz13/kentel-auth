"Author: Efe Akaröz"
from pydoc import render_doc
import re
from click import password_option
from flask import Flask, render_template,request,redirect
from flask_cors import CORS
import json
import subprocess
import os

#NOTE WEB SERVER OPTION IS STILL IN DEVELOPMENT

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("docs.html")
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        projectname = request.args.get("project")
        username = request.form.get("username")
        password = request.form.get("password")

        if projectname == None or username == None or password == None:
            return {"SCC":False,"err":"MISSING INFORMATION","SOLVE":"Read the README.md","support":"https://github.com/efeakaroz13/kentel-auth"}
        else:
            try:
                checkout = str(subprocess.check_output(f"./auth-module login {username} {password}",shell=True))
                try:
                    checkout.split("200")[1]
                    return {"SCC":True,"err":None,"code":200}
                except:
                    try:
                        checkout.split("403p")[1]
                        return {"SCC":False,"err":"INVALID PASSWORD","code":403}
                    except:
                        try:
                            checkout.split("403e")[1]
                            return {"SCC":False,"err":"USER DOES NOT EXIT","code":404}
                        except:
                            return {"SCC":False,"err":"UNKNOWN ERR","std_out":str(checkout)}



            except Exception as err_internal:
                return {"SCC":False,"err":f"INTERNAL SERVER ERROR \n {str(err_internal)}","code":500}

    projectname = request.args.get("project")
    username = request.args.get("username")
    password = request.args.get("password")
    if projectname == None or username == None or password == None:
        return {"SCC":False,"err":"MISSING INFORMATION","SOLVE":"Read the README.md","support":"https://github.com/efeakaroz13/kentel-auth"}

    else:
        try:
            checkout = str(subprocess.check_output(f"./auth-module login {username} {password}",shell=True))
            try:
                checkout.split("200")[1]
                return {"SCC":True,"err":None,"code":200}
            except:
                try:
                    checkout.split("403p")[1]
                    return {"SCC":False,"err":"INVALID PASSWORD","code":403}
                except:
                    try:
                        checkout.split("403e")[1]
                        return {"SCC":False,"err":"USER DOES NOT EXIT","code":404}
                    except:
                        return {"SCC":False,"err":"UNKNOWN ERR","std_out":str(checkout)}



        except Exception as err_internal:
            return {"SCC":False,"err":f"INTERNAL SERVER ERROR \n {str(err_internal)}","code":500}

@app.route("/register",methods=["POST","GET"])
def register():
    if request.method =="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        project = request.args.get("project")

        projname = request.args.get("project")
        
        fullname = request.form.get("fullname")
        city = request.form.get("city")
        talents = request.form.get("talents")
        birthyear= request.form.get("birthyear")
        if username == None or password == None or project==None:
            return {"SCC":False,"err":"MISSING INFORMATION"}

        try:
            os.listdir("users")
        except:
            os.system("mkdir users")
        try:
            open(f"users/{username}.K7USERFILE","r")

            return {"SCC":False,"err":"USER EXISTS","project":projname}
        except:
            checkout = str(subprocess.check_output(f"./auth-module login {username} {password}",shell=True))
            try:
                checkout.split("200")[1]
                return {"SCC":False,"err":"USER EXISTS","project":projname}

            except:

                userfile = open(f"users/{username}.K7USERFILE","a")
                if fullname == None:
                    fullname = "EMPTY"
                if city == None:
                    city="EMPTY"
                if birthyear ==None:
                    birthyear = "EMPTY"
                if talents == None:
                    talents = "EMPTY"

                userfile.write("PROJECT={};--;\n".format(projname))
                userfile.write("USERNAME={};--;\n".format(username))
                userfile.write("PASSWORD={};--;\n".format(password))
                userfile.write("FULLNAME={};--;\n".format(fullname))
                userfile.write("CITY={};--;\n".format(city))
                userfile.write("BIRTHYEAR={};--;\n".format(birthyear))
                userfile.write("TALENTS={}".format(talents))
                userfile.write(";--;")


                userfile.close()
                theout = str(subprocess.check_output(f"./auth-module register {username} {password}",shell=True))
                try:
                    theout.split("200")[1]
                    return {"SCC":True,"err":"","project":projname}
                except:
                    return {"SCC":False,"err":"C MODULE FAILED!","project":projname}

    if request.method == "GET":
        return {"SCC":False,"err":"GET METHOD NOT SUPPORTED"}

@app.route("/user/<username>",methods=["GET"])
def getuser(username):
    projname = request.args.get("project")
    try:
            profilefile = open(f"users/{username}.K7USERFILE", "r").read()
    except:
        return {"SCC": False, "err": "USER DOES NOT EXIST", "platform": projname}

    information = profilefile.split(";--;")

    talents = str(profilefile.split("TALENTS=")[1]).replace(";--;", "")
    for i in information:
        try:
            i.split("TALENTS=")[1]
            break
        except:
            try:
                projectname = i.split("PROJECT=")[1]
            except:
                try:
                    username = i.split("USERNAME=")[1]
                except:
                    try:
                        password = i.split("PASSWORD=")[1]
                    except:
                        try:
                            fullname = i.split("FULLNAME=")[1]
                        except:
                            try:
                                city = i.split("CITY=")[1]
                            except:
                                try:
                                    birthyear = i.split("BIRTHYEAR=")[1]

                                except:
                                    pass
    return {"projectname": projname, "username": username, "password": password, "fullname": fullname, "city": city, "birthyear": birthyear, "talents": talents}

@app.route("/remove_user")
def removeuser():
    username = request.args.get("username")
    password = request.args.get("password")
    checkout = str(subprocess.check_output(
            f"./auth-module login {username} {password}", shell=True))
    projname = request.args.get("project")
    try:
        checkout.split("200")[1]
        os.system(f"rm users/{username}.K7USERFILE")
        allusers = open("auth.txt", "r")
        allusersdata = allusers.readlines()
        for a in allusersdata:
            if a.split("🇹🇷")[1] == password and a.split("🇹🇷")[0] == username:
                allusersdata[allusersdata.index(a)] = ""
                break

        with open('auth.txt', 'w') as thedata:
            thedata.writelines(allusersdata)

        return {"SCC": True, "err": "", "project": projname}
    except Exception as e:
        # print(e)
        return {"SCC": False, "err": "INVALID EMAIL OR PASSWORD", "project": projname}

if __name__ == "__main__":
    app.run(debug=True,port=1371,host="0.0.0.0")