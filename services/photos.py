import json

from zato.server.service import Service


class GetPhoto(Service):
    def handle(self):
        login = self.outgoing.plain_http.get("Login")
        resp = login.conn.post(self.cid, json.loads(self.request.payload))

        is_authenticated = False if resp.status_code == 401 else True

        photo = self.outgoing.plain_http.get("Photo")
        self.logger.info(dir(self.request))
        resp = photo.conn.get(self.cid, {"is_authenticated": is_authenticated})

        self.response.payload = json.dumps(resp)
