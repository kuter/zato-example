import json

from future.moves.urllib.parse import parse_qs
from zato.server.service import Service


class GetPhoto(Service):
    def handle(self, _parse_qs=parse_qs):
        # get photo_id from url
        photo_id = self.request.http.params.photo_id

        params = {'photo_id': photo_id}

        conn = self.outgoing.plain_http.get("Photo").conn
        resp = conn.get(self.cid, params)

        self.response.payload = resp.content
