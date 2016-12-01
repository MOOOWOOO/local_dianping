# coding: utf-8

__author__ = 'Jux.Liu'

INSTALLED_MODULES = [
    ('apis', 'api', '/api'),
    ('routes', 'main', '/'),
    ('routes', 'store', '/')
]


def register_blueprint(app):
    from importlib import import_module
    for module, bp, prefix in INSTALLED_MODULES:
        m = import_module(module)
        print(m)
        if hasattr(m, bp):
            bp = getattr(m, bp)
            if prefix.strip() == '/':
                # no prefix
                app.register_blueprint(bp)
            else:
                app.register_blueprint(bp, url_prefix=prefix)
