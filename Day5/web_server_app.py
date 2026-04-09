import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return {"message": "Hello World!"}

cherrypy.quickstart(HelloWorld())