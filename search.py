import json
import time as t
def print_list(lst):
  if len(lst) == 0:
    print("search not found")
  else:
    for x  in lst:
      print(x)
  return 0  
#search = input("search: ").lower()
start = t.perf_counter()
with open('json.json', 'r') as file:
  list1 = json.load(file)
	
def get_results(s):
  results = [ ]
  for dicts in list1:
    if len(results) > 5:
      return results
    urls = dicts['kwd']
    for i in urls:
      if i == s:
        results.append(dicts['url'])
        results.append("<br>")
        break
  return "".join(results  )
"""        
res = get_results(search)

end = t.perf_counter()
print(f"{len(res)} results in {end-start} seconds")     
stat = print_list(res)
  """

def new():
	with open('json.json', 'r') as file:
  	 j = json.load(file)
	t = input("num of kwds: ")	
	kwds = []
	for i in range(0,int(t)):
		kwds.append (input(f"kwd number {i+1}: "))
	url = input("url: ")
	while not url.startswith("https://") and not url.startswith("http://"):
		print('please enter a valad url')	
		url = input("url: ")

	
	print(j)
def new2(url, *kwds2):
	kwds=[ i for i in kwds2]	 
	return {"kwd":kwds,"url":url }
	


		
	
#if input("new entry? ") == "yes"	 : new()


