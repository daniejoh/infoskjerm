#!/usr/bin/python
from http.server import BaseHTTPRequestHandler,HTTPServer
import requests
from bs4 import BeautifulSoup
import re



PORT_NUMBER = 8484

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		# self.send_header('Content-type','text/html')
		self.send_header('Access-Control-Allow-Origin', '*')
		self.end_headers()
		# Send the html message
		message = self.getDagens()
		self.wfile.write(bytes(message, 'utf8'))
		return

	def getDagens(self):
		url = "https://www.sio.no/mat-og-drikke/spisesteder-og-kaffebarer"
		header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
		request = requests.get(url,headers=header)
		soup = BeautifulSoup(request.text, 'html.parser')    
		text = soup.find('div',id="jump284")
		# print(text)
		regex = 'h4>Dagens</h4><ul class=\"dinner\"><li>(.*?)</li>'
		m = re.findall(regex, str(text))
		# print(m)
		return m[0]


try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print( 'Started httpserver on port ' , PORT_NUMBER)
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print ('^C received, shutting down the web server')
	server.socket.close()