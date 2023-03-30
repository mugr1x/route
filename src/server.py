import asyncio

import requests
import json

import tornado.web

import folium
import polyline


HTML_FORM = """form>
<label>Start</label>
<input type="text" name="start"></input>
<label>Destination</label>
<input type="text" name="dest"></input>
<button type="submit">Submit</button>
</form>
"""


class MainHandler(tornado.web.RequestHandler):

  def get(self):
    start_in = ""
    dest_in = ""
    try:
      start_in = self.get_query_argument('start')
    except:
      pass
    try:
      dest_in = self.get_query_argument('dest')
    except:
      pass
    m = folium.Map(location=[0.0, 0.0], zoom_start=2)

    if start_in != "" and dest_in != "":
      try:
        r_start = requests.get("https://nominatim.openstreetmap.org/search?q={}&format=json".format(start_in))
        start = json.loads(r_start.content)
        if len(start) == 0:
          self.write(m.get_root().render())
          return
      except Exception as e:
        print("Warning: %s" % e)
        return m.get_root().render()
      try:
        r_dest = requests.get("https://nominatim.openstreetmap.org/search?q={}&format=json".format(dest_in))
        dest = json.loads(r_dest.content)
        if len(dest) == 0:
          self.write(m.get_root().render())
          return
      except Exception as e:
        print("Warning: %s" % e)
        return
      m = folium.Map(location=[start[0]['lat'], start[0]['lon']], zoom_stat=5)
      r_url = "https://routing.openstreetmap.de/routed-car/route/v1/driving/{};{}?geometries=polyline&overview=false&alternatives=true&steps=true".format(start[0]['lon'] + "," + start[0]['lat'], dest[0]['lon'] + "," + dest[0]['lat'])
      try:
        r = requests.get(r_url)
      except Exception as e:
        print("Warning: %s" % e)
        return
      try:
        data = json.loads(r.content)
      except Exception as e:
        print("Warning: %s" % e)
        return
      data = data['routes'][0]['legs'][0]['steps']
      trails = []
      for p in data:
        dec = polyline.decode(p['geometry'])
        trails.append(dec)
      folium.PolyLine(trails).add_to(m)

    content = m.get_root().render()
    head, tail = content.split('div', maxsplit=1)
    content = head + HTML_FORM + '<div ' + tail
    self.write(content)


def make_app():
  return tornado.web.Application([
    (r"/", MainHandler)
  ])


async def main():
  app = make_app()
  app.listen(8888)
  await asyncio.Event().wait()


if __name__ == '__main__':
  asyncio.run(main())
