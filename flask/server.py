import logging
import connexion

from flask_socketio import SocketIO
from flask_cors import CORS

LOG = logging.getLogger(__name__)

options = {"swagger_ui": False}
app = connexion.App(__name__, specification_dir='./openapi/', options=options)
# app.app.json_encoder = en
app.add_api('flask_server.yml',
            arguments={'title': 'flask server'},
            pythonic_params=True)

socketio = SocketIO(app.app, async_mode='eventlet')
CORS(app.app, resources={r'/*': {'origins': '*'}})

socketio.init_app(app.app)
socketio.run(app.app, 'localhost', 8989, use_reloader=True, log=LOG)
