def merge(*objs):
    """Recursively merges objects together."""
    def _merge(a, b):
        if a is None:
            a = {}
        elif not isinstance(a, dict):
            return a
        else:
            a = dict(a)
        for key, value in b.items():
            if isinstance(value, dict):
                value = _merge(a.get(key) or {}, value)
            a[key] = value
        return a

    rv = None
    for obj in objs:
        if obj is not None:
            rv = _merge(rv, obj)
    return rv or {}
