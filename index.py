from flask import Flask, render_template
import db

app = Flask(__name__)


@app.route("/")
def welcome():
    return """
            <p> Welcome to the airport database app </p>
            <p> You can view airport information</p>
           """


@app.route("/airports")
def get_airports():
    metadata = db.MetaData(bind=None)
    airport = db.Table("airports", metadata, autoload=True, autoload_with=db.engine)
    select_data = db.select(airport)

    # all datas from the database
    rp = db.connection.execute(select_data)
    result = rp.fetchall()

    # get all columns in this table
    cols = airport.columns
    return render_template("table.html", tables=list(result), title="airport data")


if __name__ == "__index__":
    app.run(debug=True)  # enable debug mode so it listen on port when change is applied
