import hydrogram as pyrogram  # alias hydrogram -> pyrogram supaya sisa kode tetap kompatibel

from .client import Client
from ..utils import patch_into, should_patch


@patch_into(pyrogram.types.user_and_chats.user.User)
class User:
    _client: Client

    @should_patch()
    def listen(self, *args, **kwargs):
        return self._client.listen(*args, user_id=getattr(self, "id", None), **kwargs)

    @should_patch()
    def ask(self, text, *args, **kwargs):
        return self._client.ask(
            getattr(self, "id", None), text, *args, user_id=getattr(self, "id", None), **kwargs
        )

    @should_patch()
    def stop_listening(self, *args, **kwargs):
        return self._client.stop_listening(*args, user_id=getattr(self, "id", None), **kwargs)
