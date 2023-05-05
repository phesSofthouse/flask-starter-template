import os
import yaml
import logging

from flask import Flask, jsonify, make_response, request

logger = logging.getLogger(__name__)


def create_app(test_config_path=None):
    app = Flask(__name__)

    root_folder = os.path.dirname(app.root_path)
    config_path = os.path.join(root_folder, 'config/config.yaml')
    if test_config_path:
        config_path = test_config_path
    app.config.from_file(config_path, load=yaml.safe_load)

    @app.errorhandler(Exception)
    def handle_exception(e):
        logger.error(f"Error raised: {e}")
        data = jsonify({
            "code": e.code,
            "message": e.message,
        })
        response = make_response(data, e.code)
        response.headers["Content-Type"] = "application/json"
        return response

    @app.errorhandler(404)
    def page_not_found(e):
        logger.error(f"404 error: {request.url} not found")
        return jsonify({"code": 404, "message": "Page not found"}), 404

    @app.route("/")
    def status():
        return jsonify({"code": 200, "message": "Application is running"}), 200

    return app


if __name__ == "__main__":
    _flask = create_app()
    _flask.run(
        debug=_flask.config.get("DEBUG", False),
        port=_flask.config.get("PORT", 8080)
    )
