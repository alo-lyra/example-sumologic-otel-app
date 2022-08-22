import logging
import os

from flask import Flask

if not 'PYTHONPATH' in os.environ:
        os.environ['PYTHONPATH'] = ''
import opentelemetry.instrumentation.auto_instrumentation.sitecustomize

# Set debug logging globally
root = logging.getLogger()
root.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
root.addHandler(handler)


def create_app():
    app = Flask(__name__)

    from .routes import bp
    app.register_blueprint(bp)

    return app


if __name__ == '__main__':
    create_app().run(host="0.0.0.0", port=5020)
