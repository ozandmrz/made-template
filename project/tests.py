import sqlite3
import pandas as pd

def check_table_columns(table_name, expected_columns):
    con = sqlite3.connect("./data/data.sqlite")

    query = f"PRAGMA table_info({table_name});"
    table_info = pd.read_sql_query(query, con)

    unexpected_columns = set(table_info['name']) - set(expected_columns)
    missing_columns = set(expected_columns) - set(table_info['name'])

    error_message = ""
    if unexpected_columns or missing_columns:
        error_message += f"Columns mismatch in '{table_name}':\n"
        if unexpected_columns:
            error_message += f"Unexpected columns: {', '.join(unexpected_columns)}.\n"
        if missing_columns:
            error_message += f"Missing columns: {', '.join(missing_columns)}.\n"

    if error_message:
        raise AssertionError(error_message)

    con.close()


def test_table_data(table_name, primary_key_column):
    con = sqlite3.connect("./data/data.sqlite")

    query = f"SELECT * FROM {table_name} LIMIT 5;"
    table_data = pd.read_sql_query(query, con)

    assert not table_data.empty, f"{table_name} data is empty."
    assert primary_key_column in table_data.columns, f"{primary_key_column} column not found in {table_name} data."

    con.close()

try:
    # Public Transport Type 1
    check_table_columns('public_transport_type_1', ['DATE_TIME', 'transport_type_id', 'number_of_passage'])
    test_table_data('public_transport_type_1', 'DATE_TIME')

    # Public Transport Type 2
    check_table_columns('public_transport_type_2', ['DATE_TIME', 'transport_type_id', 'number_of_passage'])
    test_table_data('public_transport_type_2', 'DATE_TIME')

    # Public Transport Type 3
    check_table_columns('public_transport_type_3', ['DATE_TIME', 'transport_type_id', 'number_of_passage'])
    test_table_data('public_transport_type_3', 'DATE_TIME')

    # Traffic Density
    check_table_columns('traffic_density', ['DATE_TIME', 'AVERAGE_SPEED', 'NUMBER_OF_VEHICLES'])
    test_table_data('traffic_density', 'DATE_TIME')

    # Weather
    check_table_columns('weather', ['time', 'temperature_2m (°C)', 'relativehumidity_2m (%)', 'dewpoint_2m (°C)', 'apparent_temperature (°C)', 'precipitation (mm)', 'rain (mm)', 'snowfall (cm)', 'snow_depth (m)', 'windspeed_10m (km/h)', 'windspeed_100m (km/h)'])
    test_table_data('weather', 'time')

    print("All tests passed successfully.")
    
except AssertionError as e:
    print(f"Test failed: {e}")
    raise IOError("Test failed.") from e
