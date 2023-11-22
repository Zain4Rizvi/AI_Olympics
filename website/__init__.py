from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ksjfldksjflksdjf'

    from .views import views

    # specifies a prefix that we have to put before any of the blueprint paths
    app.register_blueprint(views, url_prefix='/')

    return app
