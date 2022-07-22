from black import err
from flask import Flask,request,redirect
from flask_cors import CORS
import json
import subprocess

#NOTE WEB SERVER OPTION IS STILL IN DEVELOPMENT

app = Flask(__name__)
CORS(app)

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        projectname = request.args.get("projectname")
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

