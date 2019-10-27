import os
from flask import Flask, url_for
from handlers import public

app = Flask(__name__)

# URLs

app.add_url_rule(rule="/", endpoint="main", view_func=public.main, methods=["GET", "POST"])

if __name__ == "__main__":
    if os.getenv('GAE_ENV', '').startswith('standard'):
        app.run()  # production
    else:
        app.run(port=8080, host="localhost", debug=True)  # localhost.run()
