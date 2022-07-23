import requests
import json
#Register
page1_register = requests.post("http://192.168.1.50:1371/register?project=yourprojectname",data={"username":"testuser","password":"testpassword","fullname":"John Doe"})
#Example out: {'SCC': True, 'err': '', 'project': 'yourprojectname'}

#Login
#Using POST
page2_login = requests.post("http://192.168.1.50:1371/login?project=yourprojectname",data={"username":"testuser","password":"testpassword"})
#Example out {'SCC': True, 'err': null, 'project': 'yourprojectname'}

#Using get
page3_login_get = requests.get("http://192.168.1.50:1371/login?project=yourprojectname&username=testuser&password=testpassword")
#Example out {'SCC': True, 'err': null, 'project': 'yourprojectname'}

#Change password 
page4_change_password= requests.get("http://192.168.1.50:1371/change_password?project=yourprojectname&username=testuser&oldpassword=testpassword&newpassword=checkoutmynewpassword")
