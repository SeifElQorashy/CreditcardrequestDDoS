import requests 

import threading

url = '//اكتب هنا الرابط بتاع الصفحه/ write here the url of the website'

data= { 


}


def do_request():

     while True:

       response = requests.post(url, data = data).txt

       print(response)

threads = []


for i in range (50):
    t = threading.Thread(target=do_request)
    t.daemon=True
    threads.append(t)

for i in range (50):
    thread[i].start()

for i in range (50):
    thread[i].join()
