from flask import Blueprint, send_from_directory
import os

DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def build_static_blueprint(*args, **kwargs):
    bp = Blueprint(*args, **kwargs)

    @bp.route('/wikimedia-ui-static/<path:fn>')
    def wikimediaui_static(fn):
        return send_from_directory(os.path.join(DIRECTORY, "static"), fn)

    @bp.route('/MW/<path:fn>')
    def wikimediaui_mw_static(fn):
        return send_from_directory(os.path.join(DIRECTORY, "static", "MW"), fn)

    return bp
