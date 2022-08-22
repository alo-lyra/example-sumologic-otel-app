from flask import Blueprint
from opentelemetry.metrics import get_meter

bp = Blueprint('', __name__)


@bp.route("/")
def hello_world():
    meter = get_meter("test_meter")
    counter = meter.create_counter("test_counter")
    counter.add(1)
    return "<p>Hello, World!</p>"
