from browser import document, ajax, bind
from browser.widgets.dialog import InfoDialog


# bdfb5671e56189cb2073ef6a0b99a523 106.67417764663696, 11.063078488967657
# api.openweathermap.org/data/2.5/weather?lat=11.063078488967657&lon=106.67417764663696&appid=bdfb5671e56189cb2073ef6a0b99a523
lat = ""
lng = ""
api = "bdfb5671e56189cb2073ef6a0b99a523"
url = "http://api.openweathermap.org/data/2.5/weather"

def on_complete(req):
   if req.status == 200 or req.status == 0:
       InfoDialog("Hello", req.text) 
       document['lat'] <= "blah "
       
   else:
       InfoDialog("Error", req.text) 

def test():
    InfoDialog("Error", "asdasd") 

       


def getData(aa):
    url = document['url'].value
    req = ajax.Ajax()
    req.bind('complete', on_complete)
    # send a POST request to the url
    req.open('GET', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    # send data as a dictionary
    req.send({'x': 0, 'y': 1})

document["map"].bind("click", getData)
