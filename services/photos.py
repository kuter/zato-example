import json

from future.moves.urllib.parse import parse_qs
from simplejson.scanner import JSONDecodeError
from zato.server.service import Service


class GetPhoto(Service):
    def handle(self, _parse_qs=parse_qs):
        headers = {}

        login_conn = self.outgoing.plain_http.get("Login").conn
        resp = login_conn.post(self.cid, json.loads(self.request.payload))

        try:
            token = resp.json()["token"]
        except JSONDecodeError:
            pass
        else:
            headers.update({"X-Token": token})

        params = {"photo_id": self.request.http.params.photo_id}
        photo_conn = self.outgoing.plain_http.get("Photo").conn
        resp = photo_conn.get(self.cid, params, headers=headers)

        self.response.payload = resp.content
