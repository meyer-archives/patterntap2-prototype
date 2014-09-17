import mimetypes, sys
from os import curdir, sep
from os.path import splitext
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
try:
	from jinja2 import Template
except ImportError:
	print "Jinja template engine is not installed. Fix this with `pip install jinja2`"
	exit(1)

server_port = 8080

class JinjaHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			f = open(curdir + sep + self.path)
			self.send_response(200)

			mimetype = mimetypes.guess_type(self.path)[0]
			self.send_header('Content-type', mimetype)
			self.end_headers()

			filename = splitext( self.path )

			if( self.path.endswith('.html') ):
				template = Template( f.read() ).render()
				self.wfile.write( template )
				r = open( curdir + filename[0] + "-compiled" + filename[1], 'w' )
				r.write(template)
				r.close()
			else:
				self.wfile.write(f.read())

			f.close()

			return
		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		try:
			sys.argv[1] = int( sys.argv[1] )
		except:
			print "Invalid port number:", sys.argv[1]
			exit(1)
		server_port = sys.argv[1]

	try:
		httpd = HTTPServer(('',server_port), JinjaHandler)
		print 'Server started on port %d, press Ctrl-C to stop' % server_port
		httpd.serve_forever()
	except KeyboardInterrupt:
		print "\nShutting down..."
		httpd.socket.close()