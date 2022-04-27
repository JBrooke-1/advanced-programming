from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import io
import db


def draw_small_airport_freq():
    sql = """
        SELECT frequency_mhz, airport_ref FROM db.`airport-frequencies`
        JOIN db.airports ON db.airports.id=db.`airport-frequencies`.airport_ref
        AND db.airports.type='small_airport';
        """
    sql_text = db.text(sql)
    # all datas from the database
    rp = db.connection.execute(sql_text)
    results = rp.fetchall()

    # create a bin size that reflects the width
    # get the max frequency value from DB
    sql_max = """
             SELECT MAX(frequency_mhz), airport_ref, db.airports.name FROM db.`airport-frequencies`
            JOIN db.airports ON db.airports.id=db.`airport-frequencies`.airport_ref
            AND db.airports.type='small_airport';
            """
    max =db.connection.execute(db.text(sql_max))
    max_val = max.fetchall()[0][0]

    # get the min frequency value from db
    sql_min = """
            SELECT MIN(frequency_mhz), airport_ref, db.airports.name FROM db.`airport-frequencies`
            JOIN db.airports ON db.airports.id=db.`airport-frequencies`.airport_ref
            AND db.airports.type='small_airport';
            """
    max =db.connection.execute(db.text(sql_min))
    min_val = max.fetchall()[0][0]

    # total width and allocate binsize
    bin_width = 15 # create a set number of bins
    total_width = max_val - min_val
    print('total_width:', total_width)
    bins = int(total_width) // bin_width

    # average freqluency
    sql_avg = """
        SELECT AVG(frequency_mhz), airport_ref, db.airports.name FROM db.`airport-frequencies`
        JOIN db.airports ON db.airports.id=db.`airport-frequencies`.airport_ref
        AND db.airports.type='small_airport';"""
    avg =db.connection.execute(db.text(sql_avg))
    avg_val = avg.fetchall()[0][0]

    # added visualization for historgram
    counts, edges, bars = plt.hist(x=[result[0] for result in results], bins=400, edgecolor="yellow", color="green")
    plt.xlim(100, avg_val + bin_width)
    plt.bar_label(bars)
    plt.title("communication frequencies used by small_airports")
    plt.xlabel('Frequencies (mhz)')
    plt.ylabel('Numbers of counts')
    plt.show()


draw_small_airport_freq()
