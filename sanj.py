
d = open("sanjana.html","w")
a = """<!doctype html>
<html>
 <head>
<title>RESUME</title>
<style type="text/css">
    table {
        font-size: 18px;
    }
    #heading{
        font-size: 20px;
        }
</style>
</head>
<center><h1><u><b> RESUME</u></b></h1></center></div>
<body style="padding-top:10px ; padding-left: 40px; padding-right:40px; " >
    <div class="col-xs-6" >

<div  >
	<div class="jumbotron">
    
<h3 style="font-size: 28px;">sanjana chaudhari</h3>
<p style="font-size: 25px;">pihuchaudhary2002@gmail.com</p>
<p  style="font-size: 25px;">DOB: 24-1-2001</p>
<p  style="font-size: 25px;">Adress : Narayan Nagar Bhopal </p>
<p  style="font-size: 25px;">Contact No.:  8305163181</p>
<p  style="font-size: 25px;">Nationality : Indian</p>

 
  <h3><u><b>CAREER OBJECTIVE</u></b></h3>
  <p  style="font-size: 25px;">To solve problems in effective and creative in a challanging  position. </p>
            <h3><u>EDUCATION </u></h3>
            <table border="" >
                <tr >
                    <th>Qualification</th>
                    <th>Institute</th>
                    <th>Percentage / Grades</th>
                    <th>Year</th>
                </tr>
                <tr>
                    <td>10th</td>
                    <td>Govt.Girls higher secondary school rampur baghelan dist.satna (m.p)</td>
                    <td>52.9%</td>
                    <td>2016</td>
                </tr>
                <tr>
                    <td>Deploma (CSE)</td>
                    <td>Govt. Polytechnic College Satna  </td>
                    <td>71.4%</td>
                    <td>2019</td>
                </tr>
                
            </table>

        </div>
          <h3 style="text-transform: uppercase;"><u>Key Skills</u></h3>
     <ol  style="font-size: 25px;">
      <li> C++</h3>
	 <li> C</li>
	 <li> HTML</li>
	 <li> CSS</li>
     <li>PHP</li>
	</ol>
      <h3><u><b style="text-transform: uppercase;">Persnol Profile ID</b></u></h3>
    <ol style="font-size: 25px;">
        <li>Github :  Sanjana387</a></li>
        <li>Linkdin :   sanju Chaudhary</a></li>
       <li>HackerRank : pihuchaudhary2002@gmail.com</a></li>
       <li>Canvas :  pihuchaudhary2002@gmail.com</a></li> 
       <li>Intershala : pihuchaudhary2002@gmail.com</a></li></ol>

         <h3><u>HOBBIES</u></h3>
        <ol style="font-size: 25px;"><li>Reading Story</li>
        <li>Singing</li>
        </ol>
    <h3><u style="text-transform: uppercase;">Langauges</u></h3>
    <ol style="font-size: 25px;">
        <li> English</li>
        <li>Hindi</li>
    </ol>
        <h3><u>WORK  EXPERIENCE</u></h3>
        <p style="font-size: 25px;">Fresher</p>
</div></body>
</html>"""
d.write(a)
d.close()