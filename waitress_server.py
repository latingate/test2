from waitress import serve
import update_db

serve(update_db.app, host='0.0.0.0', port=5000)

# in order to use waitress server:
# in the main app (ie update_db.app) replace this line:
# app.run(host='0.0.0.0', port=5000)
# with this line:
# app = Flask(__name__)