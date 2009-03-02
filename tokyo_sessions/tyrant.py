import pytyrant
import time

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.encoding import force_unicode
from django.contrib.sessions.backends.base import SessionBase, CreateError

try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

TT_HOST = getattr(settings, 'TT_HOST', None)
TT_PORT = getattr(settings, 'TT_PORT', None)

if TT_HOST is None or TT_PORT is None:
    raise ImproperlyConfigured(u'To use django-tokyo-sessions, you must ' + 
        'first set the TT_HOST and TT_PORT settings in your settings.py')
else:
    SERVER_LOCAL = local()
    def get_server():
        try:
            server = SERVER_LOCAL.server
        except AttributeError:
            server = pytyrant.PyTyrant.open(TT_HOST, TT_PORT)
            SERVER_LOCAL.server = server
        return server
        

class SessionStore(SessionBase):
    """
    A Tokyo Cabinet-based session store.
    """
    def load(self):
        session_data = get_server().get(self.session_key)
        if session_data is not None:
            expiry, data = int(session_data[:15]), session_data[15:]
            if expiry < time.time():
                return {}
            else:
                return self.decode(force_unicode(data))
        self.create()
        return {}
    
    def create(self):
        while True:
            self.session_key = self._get_new_session_key()
            try:
                self.save(must_create=True)
            except CreateError:
                continue
            self.modified = True
            return
    
    def save(self, must_create=False):
        if must_create and self.exists(self.session_key):
            raise CreateError
        data = self.encode(self._get_session(no_load=must_create))
        encoded = '%15d%s' % (int(time.time()) + self.get_expiry_age(), data)
        get_server()[self.session_key] = encoded
    
    def exists(self, session_key):
        retrieved = get_server().get(session_key)
        if retrieved is None:
            return False
        expiry, data = int(retrieved[:15]), retrieved[15:]
        if expiry < time.time():
            return False
        return True
    
    def delete(self, session_key=None):
        if session_key is None:
            if self._session_key is None:
                return
            session_key = self._session_key
        del get_server()[session_key]