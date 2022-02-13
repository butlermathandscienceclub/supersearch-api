from flask import *
from search import *
app = Flask('app')
p=True
@app.route('/', methods=['GET', 'POST'])
def main():
	d= request.args.get("dark")
	s = request.args.get("search") ;
	r = get_results(s)
	print(s)
	style= """
	text-align:center;
	"""
	s1 = "	<style>:root{color:black}</style>"
	s2 = "	<style>:root{color:white; background-color:black;}</style>"
	z = s2 if d == "2" else s1
	s = f"{z}<div style=\"{style}\"><h1>results</h1><br>"
	print(r)
	for i in r:
		s += (f"<a href=\"{i}\" target=\"_blank\" >{i}</a><br>")
	s+="</div>"
	l = """	<style>:root{color:black}</style><div style="
	text-align:center;
	"><h1>results</h1><br></div>"""
	l2 = """	<style>:root{color:white; background-color:black;}</style><div style="
	text-align:center;
	"><h1>results</h1><br></div>"""

	res = f'{ s if s != l else "<h1>no results</h1>"}'
	if s == l2 :
		res = """<style>:root{color:white; background-color:black;}</style><div style="
	text-align:center;
	"><h1>no results</h1><br></div>"""
	print(res)

	return res

@app.route('/new', methods=['GET', 'POST'])
def r2():
	if not p:
		s = eval(request.args.get("kwdlist")) 
		url = request.args.get("url")
		x=new2(url, *s)
		return f'{x} '

	


app.run(host='0.0.0.0', port=8080)
