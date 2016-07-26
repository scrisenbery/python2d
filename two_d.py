from __future__ import print_function
import json
import webapp2

class Mainer(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    headers = dict(self.request.headers)
    s = json.dumps(headers, sort_keys=True, indent=4)
    self.response.write(s + '\n')
    table_data = [
        ['Last name',   'First name',   'Age'],
        ['Smith',       'John',         30],
        ['Carpenter',   'Jack',         47],
        ['Johnson',     'Paul',         62],
    ]
    self.response.write(table_data)
    self.response.write('\n\n\n\n')
    for row in table_data:
        for column in row:
            self.response.write(column)
        self.response.write('\n')
    self.response.write('\n\n\n\n')
    self.response.write(json.dumps(table_data))

app = webapp2.WSGIApplication([
  ('/', Mainer),
], debug=True)
