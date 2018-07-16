
from flask import Flask


app = Flask(__name__)
from models import user_views
if __name__ == '__main__':
    app.run(debug=True)

