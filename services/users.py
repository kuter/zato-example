import json

from zato.server.service import Service


class Login(Service):

    @property
    def headers(self):
        return {x.replace("HTTP_", ""): y for x, y in
                self.request.http._wsgi_environ.items() if
                x.startswith("HTTP_")}

    def handle(self):
        conn = self.outgoing.plain_http.get("Login").conn
        resp = conn.post(self.cid, json.loads(self.request.payload))

        if not resp.ok:
            lang_conn = self.outgoing.plain_http.get("Photo").conn
            lang_resp = lang_conn.post(self.cid, {"text": "Login failed"},
                                       headers=self.headers)

        self.response.payload = resp.content
