# coding: utf-8

__author__ = 'Jux.Liu'

INSTALLED_MODULES = [
    ('routes', 'main', '/'),
    ('api', 'api', '/api'),
    ('routes', 'store', '/')
]


def register_blueprint(app):
    from importlib import import_module
    for folder, module, prefix in INSTALLED_MODULES:
        m = import_module(folder)
        print(m)
        print(module)
        if hasattr(m, module):
            bp = getattr(m, module)
            if prefix.strip() == '/':
                # no prefix
                app.register_blueprint(bp)
            else:
                app.register_blueprint(bp, url_prefix=prefix)
