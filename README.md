## Note
  This is a cheap clone of the OSRM [demo server](https://map.project-osrm.org).
  You would want to use this one instead.



## Setup

pip3 install --user requests folium tornado polyline

                ------------------------------------------------------                     
                |                                                    |                     
                |              Navi application                      |                     
                |                                                    |                     
                |                                                    |                     
                |     Input current location and destination:        |                     
                |                                                    |                     
                |     <o> Call Nominatim API                         |                     
                |                                                    |                     
                |     <o> Show current location in the browser       |                     
                |                                                    |
                |     <o> Call OSRM API                              |                     
                |                                                    |                     
                |     <o> Display route in the browser               |                     
                |                                                    |                     
                ------------------------------------------------------                     
                +--------------+ +----------------+ +----------------+                     
                |  Route API   | |  Resolver API  | |   Frontend     |                     
                |              | |                | |                |                     
                |    OSRM      | |   Nominatim    | |   tornado +    |                     
                |              | |                | |   HTML form    |                     
                |              | |                | |                |                     
                |              | |                | |                |                     
                +--------------+ +----------------+ +----------------+  
## License


Copyright (c) 2023 github.com/mugr1x

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
