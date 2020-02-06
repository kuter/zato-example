from zato.server.service import Service


class Login(Service):
    def handle(self):
        conn = self.outgoing.plain_http.get("Login").conn
        resp = conn.post(self.cid, self.request.payload)

        self.response.payload = resp.content
