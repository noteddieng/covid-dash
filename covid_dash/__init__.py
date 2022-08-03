from flask import Flask


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config_frompyfile('config.py')
    app.config.from_object('config.ProdConfig')


    with app.app_context():
        from . import routes
        
        from plotlydash.app import create_dashboard
        app =create_dashboard(app)
        
        return app 

