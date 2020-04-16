import json

from zato.server.service import Service


class Login(Service):

    @property
    def headers(self):
        """Get headers from request."""
        return {x.replace("HTTP_", ""): y for x, y in
                self.request.http._wsgi_environ.items() if
                x.startswith("HTTP_")}

    def handle_POST(self):
        request = json.loads(self.request.payload)

        login = self.outgoing.plain_http.get("Login")
        resp = login.conn.post(self.cid, request)

        message = "Login Successful" if resp.ok else "Login failed"
        translate = self.outgoing.plain_http.get("Translate")
        resp_translate = translate.conn.post(self.cid, {"text": message},
                                             headers=self.headers)

        events = self.outgoing.plain_http.get("Events")
        events.conn.post(self.cid, json.dumps({"event": message}))

        payload = {
            "status": resp_translate.content.decode("utf-8"),
        }
        if resp.ok:
            payload.update(resp.json())

        self.response.status_code = resp.status_code
        self.response.payload = json.dumps(payload)
