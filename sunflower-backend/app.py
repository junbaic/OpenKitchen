from main import *
from main.table.mytable import *
from main.api import blueprint
from main.table.insertdata import insert_data
from flask_cors import *


app = create_app()
app.register_blueprint(blueprint)


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        insert_data()
        app.run(
            host='0.0.0.0',
            debug=True, 
            port=8000 # port number
        )
