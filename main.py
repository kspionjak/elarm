import cherrypy

class Elarm(object):
    @cherrypy.expose
    def index(self):
        return "Hello Elarm!"

if __name__ == "__main__":
    cherrypy.config.update({'server.socket_host': '192.168.64.17'})
    cherrypy.quickstart(Elarm())

