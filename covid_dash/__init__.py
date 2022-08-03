from flask import Flask

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_obejct('config.Config')

    with app.app_context():
        from . import routes
        
        from plotlydash import create_dashboard
        return app 

