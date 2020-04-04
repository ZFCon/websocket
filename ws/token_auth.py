from channels.auth import AuthMiddlewareStack
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from urllib.parse import parse_qs


class TokenAuthMiddleware:
    """
    Token authorization middleware for Django Channels 2
    """

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        try:
            token_key = parse_qs(scope["query_string"].decode("utf8"))["token"][0]
            token = Token.objects.get(key=token_key)
            scope['user'] = token.user
            close_old_connections()
        except:
            scope['user'] = AnonymousUser()
        return self.inner(scope)

TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))
