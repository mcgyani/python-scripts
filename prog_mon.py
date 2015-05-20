import datetime
def index():
    return """
<html><head>
<link rel="shortcut icon" href="/mon.png" type="image/png">
<title>Program Monitorizare</title>
<meta charset="utf-8">
<link rel="stylesheet" href="//code.jquery.com/ui/1.11.2/themes/smoothness/jquery-ui.css">
<script src="//code.jquery.com/jquery-1.10.2.js"></script>
<script src="//code.jquery.com/ui/1.11.2/jquery-ui.js"></script>
<link rel="stylesheet" href="/resources/demos/style.css">
<script>
$(function() {
$( "#datepicker" ).datepicker();
});
</script>
</head>
<style>
img {
    width: 90;		
    margin: 0 auto;
    padding-top: 30px;
    padding-left: 45px;		 
}
body {
    width:250px;
    margin: 0 auto;
}
.checkbox-day-night {
    padding-left : 45px;
}
.butons {
    padding-left : 45px;
}
iframe {
    margin: 0px;
    padding: 0px;
    border: 0px;
    display: block;
}
</style>
<body>
<img src="http://s1emagst.akamaized.net/layout/ro/images/logo//2/2821.png">
<br>
<form onreset="reset_all()" value="form" action="index.py/get_prog" method="POST" target="receiver"> 
<p>
    <label for="datepicker">Data: </label>
    <input type="text" name="datepicker" id="datepicker" placeholder = "alege data... "><br>
    <p></p>
<div class="checkbox-day-night">
     <label><input type="checkbox" name="day_shift" value="day" >Tura Zi<br></label>
     <label><input type="checkbox" name="night_shift" value="night" >Tura Noapte<br></label> 
</div>     
<p></p>
<div class="butons">
    <input type="submit" value="Calculeaza"> 
    <input type="reset" value="Reseteaza">
</div>
<p></p>
<iframe name="receiver" id="receiver"></iframe>
<script>
function reset_all() {
document.getElementById('receiver').src = "";
document.form.reset();
}
</script>
</form>
</body>
</html>
"""

def get_prog(req):
	info = req.form
	custom_date = info['datepicker']
        if custom_date == "":
            custom_date = datetime.datetime.now().strftime("%m/%d/%Y")
	if not (info.has_key("day_shift") or info.has_key("night_shift")):
		return '''
<html>
<style>
body {
    width:200px;
    padding-left: 45px;
    
}
</style>
<body>
<font color="red">Nu ati selectat tura!</font>
<body>
</html>'''
	else:
		while True:
			try:
				str_custom_date = datetime.datetime.strptime(custom_date, "%m/%d/%Y").date()
				break
			except ValueError:
				return '''
<html>
<style>
body {
    width:200px;
    margin: 0 auto; 
}
</style>
<body>
<font color="red">Ooops! Nu ati introdus data corect! (ll/zz/aaaa)</font>
<body>
</html>'''

        	day_1 = "09/18/2014"
		str_day_1 = datetime.datetime.strptime(day_1, "%m/%d/%Y").date()
        	days_diff = (str_custom_date - str_day_1).days
        	day_of_21 = days_diff % 21
        	shifts = [20, 30, 21, 13, 30, 10, 20, 30, 10, 32, 21, 10, 20, 30, 10, 20, 13, 32, 20, 30, 10]
        	n = shifts[day_of_21]
		on_shift = []
		on_shift.append(str(n)[1:])
                on_shift.append(str(n)[:1])
		for i in range(len(on_shift)):
			if on_shift[i] == '0':
				on_shift[i] = 'Alexandru Iepurasi'
			elif on_shift[i] == '1':
				on_shift[i] = 'Eusebiu Petu'
			elif on_shift[i] == '2':
				on_shift[i] = 'Catalin Maican'
			else:	
				on_shift[i] = 'Cristinel Catana'
 
		if (info.has_key("day_shift") and info.has_key("night_shift")):
			return """
<html>
<style>
body {
    width:200px;
    margin: 0 auto;
}
</style>
<body>
Pe tura de zi:<br>
<font color="blue"> %s</font><br>
<p></p>
Pe tura de noapte:<br>
<font color="blue"> %s</font>
</body>
</html>
"""%(on_shift[0],on_shift[1])

		elif info.has_key('day_shift'):
			return '''
<html>
<style>
body {
    width:200px;
    margin: 0 auto;
}
</style>
<body>
Pe tura de zi:<br>
<font color="blue">%s</font>
</body>
</html>
'''%(on_shift[0])
		elif info.has_key('night_shift'):
                        return '''
<html>
<style>
body {
    width:200px;
    margin: 0 auto;
}
</style>
<body>
Pe tura de noapte:<br>
<font color="blue">%s</font>
</body>
</html>
'''%(on_shift[1])
			
