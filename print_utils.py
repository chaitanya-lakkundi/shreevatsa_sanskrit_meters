"""Utils for printing Unicode strings, lists, dicts, etc."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import match_result


def _ToUnicode(x):
  """Convert x to unicode, whatever it is."""
  if isinstance(x, unicode):
    return x
  if isinstance(x, int):
    return unicode(x)
  if isinstance(x, list):
    return _ListToUnicode(x)
  if isinstance(x, dict):
    return _DictToUnicode(x)
  if isinstance(x, match_result.MatchResult):
    return x.Name()
  assert False, (x, type(x))


def _ListToUnicode(li):
  assert isinstance(li, list)
  ret = ('[' + ', '.join(_ToUnicode(i) for i in li) + ']')
  assert isinstance(ret, unicode)
  return ret


def _DictToUnicode(d):
  assert isinstance(d, dict)
  ret = '{'.encode('utf-8')
  for (key, value) in sorted(d.items(), key=lambda x: x[1], reverse=True):
    ret += ('\n  ' + key + ': ' + _ToUnicode(value)).encode('utf-8')
  ret += '\n}'.encode('utf-8')
  assert isinstance(ret, str)
  ret = ret.decode('utf-8')
  assert isinstance(ret, unicode)
  return ret


def Print(u):
  u = _ToUnicode(u)
  assert isinstance(u, unicode), (u, type(u))
  print(u.encode('utf8'))
