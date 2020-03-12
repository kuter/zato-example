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

        if not resp.ok:
            translate = self.outgoing.plain_http.get("Translate")
            resp = translate.conn.post(self.cid, {"text": "Login failed"},
                                       headers=self.headers)

        self.response.payload = resp.content
