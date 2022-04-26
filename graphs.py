from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import io
import db

figure = plt.figure()
axes = figure.add_subplot(1, 1, 1)
axes.bar([1, 2, 3, 4], [3, 4, 5, 25], tick_label=["a", "b", "c", "d"])


def draw_airport():
    metadata = db.MetaData(bind=None)
    airport = db.Table("airports", metadata, autoload=True, autoload_with=db.engine)
    select_data = db.select(airport)

    sql = """
        SELECT frequency_mhz, airport_ref FROM db.`airport-frequencies`
        JOIN db.airports ON db.airports.id=db.`airport-frequencies`.airport_ref
        AND db.airports.type='small_airport';
        """
    # all datas from the database
    rp = db.connection.execute(select_data)
    result = rp.fetchall()

    # get the result as list
    print(type(result[10]))


draw_airport()
plt.show()
