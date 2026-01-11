from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["UPLOAD_FOLDER"] = "app/static/uploads"
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

    from app.routes import main
    app.register_blueprint(main)

    return app