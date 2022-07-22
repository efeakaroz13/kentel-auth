async function login(){
    username=prompt("username")
    password = prompt("password")
    project="yourprojectname"
    const response = await fetch("http://192.168.1.39:1371/login?project="+project+"&username="+username+"&password="+password);
    const out = await response.json();

    //works with http 
    //for using with https, create an https server
    return out
}
