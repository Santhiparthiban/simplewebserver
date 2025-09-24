from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
     <title>table</title>
     <body>
          <h1 align="centre">Device specification(Santhi)</h1>
          <table border="4" cellpadding="6" cellspacing="10">
          <tr>
             <th bgcolor="cyan">S.No</th>
             <th bgcolor="cyan">Device specification</th>
             <th bgcolor="cyan">Type</th>
          </tr>
          <tr bgcolor="pink">
              <td>1</td>
              <td>Device name</td>
              <td>TMP215-75-G2</td>
          </tr>
          <tr bgcolor="light blue">
              <td>2</td>
              <td>Processor</td>
              <td>Intel(R)Core(TM)ultra 5125H</td>
              </tr>
          <tr bgcolor="yellow">
              <td>3</td>
              <td>Installed RAM</td>
              <td>16.0 GB</td>
          </tr>
          <tr bgcolor="orange">
              <td>4</td>
              <td>system type</td>
              <td>64 bit operating system</td>
          </tr>
          <tr bgcolor="purple">
              <td>5</td>
              <td>pen and touch</td>
              <td>no pen and touch available</td>
          </tr>
          </table>
      </body>
</html>    
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()