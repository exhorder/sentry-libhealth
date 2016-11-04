import sys


PY2 = sys.version_info[0] == 2


if PY2:
    def implements_to_string(cls):
        cls.__unicode__ = cls.__str__
        cls.__str__ = lambda x: x.__unicode__().encode('utf-8')
        return cls
else:
    implements_to_string = lambda x: x
