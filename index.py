from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return """
            <p> Welcome to the airport database app </p>
            <p> You can view airport information</p>
           """


@app.route("/airports")
def get_airports():
    
    return """
            <p>This page has airport information </p>
           """


if __name__ == "__index__":
    app.run(debug=True)  # enable debug mode so it listen on port when change is applied
