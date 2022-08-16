import re
import json

from tabulate import tabulate
from logfilemake import logmaker
class mate2:
    
    def bab5():
        
       
        

        
        with open('regularlog.txt','r+')as logfile:
            with open ('regularlog2.txt','w') as resultfile:
                f=logfile.readlines()
                resultfile.write('''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  background: #555;
  background-image: url('https://upload.wikimedia.org/wikipedia/commons/0/08/Cisco_logo_blue_2016.svg');

}

.content {
  max-width: 1500px;
  margin: auto;
  background: white;
  padding: 10px;
  
}
p.ex2 {
    text-align: center; 
    font-size: 50px;
    color: green;

}
#boxbutton{
        align-self: center;

     width: 227px;
    height: 50px;
    border-radius: 5px;
    color: green;
}
#testcase{
    color:
}
</style>
</head>
<body>

<div class="content">''')
                resultfile.write('''<script>
function myFunction() {
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}
</script>''')
                resultfile.write('''<p class="ex2">TESTCASE LOG</p>''')
                resultfile.write(''''<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for names.." title="Type in a name">''')
                resultfile.write('''<body style="background-color:lightblue;"''')
                resultfile.write('''<form>
 <input type="button" id="boxbutton"value="Go back!" onclick="history.go(0)">
</form>''')
                resultfile.write('''<ul id="myUL">''')
                for line in f:
                    if 'Starting testcase' in line:
                        resultfile.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        resultfile.write("\n")
                    if 'result of testcase' in line:
                        resultfile.write("<b>")
                        resultfile.write(line)
                        resultfile.write("</b>")
                        resultfile.write("-XASEWASDASDFASDFASDFASDKLFASDKFLASDFASDLFKADSFDSAFKDSFASDKFASDFKASDFASDKFASD--XASEWASDASDFASDFASDFASDKLFASDKFLASDFASDLFKADSFDSAFKDSFASDKFASDFKASDFASDKFASD-")
                        resultfile.write("\n")
                        resultfile.write("\n")
                    if '+------------------------------------------------------------------------------+' in line:
                        pass
                    else:
                        resultfile.write('''<li><a href="#">''')
                        resultfile.write(line)
                        resultfile.write("</a></li>")

            
        nope=open('regularlog2.txt','r')
        zz=nope.read()
        kaka=zz.split("-XASEWASDASDFASDFASDFASDKLFASDKFLASDFASDLFKADSFDSAFKDSFASDKFASDFKASDFASDKFASD--XASEWASDASDFASDFASDFASDKLFASDKFLASDFASDLFKADSFDSAFKDSFASDKFASDFKASDFASDKFASD-")

        return kaka
