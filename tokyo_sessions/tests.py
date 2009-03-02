r"""
>>> from django.conf import settings
>>> from tokyo_sessions.tyrant import SessionStore as TokyoSession

>>> tokyo_session = TokyoSession()
>>> tokyo_session.modified
False
>>> tokyo_session.get('cat')
>>> tokyo_session['cat'] = "dog"
>>> tokyo_session.modified
True
>>> tokyo_session.pop('cat')
'dog'
>>> tokyo_session.pop('some key', 'does not exist')
'does not exist'
>>> tokyo_session.save()
>>> tokyo_session.exists(tokyo_session.session_key)
True
>>> tokyo_session.delete(tokyo_session.session_key)
>>> tokyo_session.exists(tokyo_session.session_key)
False

>>> tokyo_session['foo'] = 'bar'
>>> tokyo_session.save()
>>> tokyo_session.exists(tokyo_session.session_key)
True
>>> prev_key = tokyo_session.session_key
>>> tokyo_session.flush()
>>> tokyo_session.exists(prev_key)
False
>>> tokyo_session.session_key == prev_key
False
>>> tokyo_session.modified, tokyo_session.accessed
(True, True)
>>> tokyo_session['a'], tokyo_session['b'] = 'c', 'd'
>>> tokyo_session.save()
>>> prev_key = tokyo_session.session_key
>>> prev_data = tokyo_session.items()
>>> tokyo_session.cycle_key()
>>> tokyo_session.session_key == prev_key
False
>>> tokyo_session.items() == prev_data
True
"""

if __name__ == '__main__':
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    import doctest
    doctest.testmod()
