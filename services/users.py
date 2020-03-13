import json

from zato.server.service import Service


class Login(Service):

    @property
    def headers(self):
        """Get headers from request."""
        return {x.replace("HTTP_", ""): y for x, y in
                self.request.http._wsgi_environ.items() if
                x.startswith("HTTP_")}

    def handle(self):

        request = json.loads(self.request.payload)

        login = self.outgoing.plain_http.get("Login")
        resp = login.conn.post(self.cid, request)

        if resp.ok:
            message = "Login Successful"
        else:
            message = "Login failed"
            # translate mesage
            translate = self.outgoing.plain_http.get("Translate")
            resp = translate.conn.post(self.cid, {"text": message},
                                       headers=self.headers)

        # send event
        events = self.outgoing.plain_http.get("Events")
        events.conn.post(self.cid, json.dumps({"event": message}))

        self.response.payload = resp.content
