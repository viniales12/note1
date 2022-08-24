from flask import Flask
from flask_migrate import Migrate

from notes_api.models.note import db
from notes_api.routes.notes import notes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///note.db"
db.init_app(app)
with app.app_context():
    db.create_all()
migrate = Migrate(app, db)

app.register_blueprint(notes)

if __name__ == "__main__":
    app.run(
        debug=False,
        host='0.0.0.0',
        port=5000,
        use_reloader=False
    )
