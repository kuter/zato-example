import json

from future.moves.urllib.parse import parse_qs
from simplejson.scanner import JSONDecodeError
from zato.server.service import Service


class GetPhoto(Service):

    @property
    def headers(self):
        """Get headers from request."""
        return {x.replace("HTTP_", ""): y for x, y in
                self.request.http._wsgi_environ.items() if
                x.startswith("HTTP_")}

    def handle(self, _parse_qs=parse_qs):
        params = {"photo_id": self.request.http.params.photo_id}
        photo_conn = self.outgoing.plain_http.get("Photo").conn
        resp = photo_conn.get(self.cid, params, headers=self.headers)

        self.response.status_code = resp.status_code
        self.response.payload = resp.content
