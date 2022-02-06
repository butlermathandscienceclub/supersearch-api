from flask import *
from search import *
from time import perf_counter
app = Flask('app')
@app.route('/', methods=['GET', 'POST'])
def main():
	s = request.args.get("search") ;
	start = perf_counter()
	r = get_results(s)
	end = perf_counter()
	result_time = str(end-start)
	s = "found results in {} seconds <br>".format(result_time)
	for i in r:
		s += (f"<a href=\"{i}\" target=\"_blank\" >{i}</a><br>")
		
	return f'{s if r !="" else f"no results for your search " }'
@app.route('/new', methods=['GET', 'POST'])
def r2():
	s = eval(request.args.get("kwdlist")) 
	url = request.args.get("url")
	x=new2(url, *s)
	return f'{x} '


app.run(host='0.0.0.0', port=8080)
