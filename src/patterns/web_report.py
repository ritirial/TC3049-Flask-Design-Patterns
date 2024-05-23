from patterns.csv_utils import Ride
from patterns import strategy_report_data_row

def create_content(rides):
    builder = [_create_headers("Taxi Report"), _create_table_headers()]
    for ride in rides:
        builder.append(_add_ride(ride))
    builder.append(_close_table_headers())

    return "".join(builder)


def create_file(content: str):
    with open("financial-report.html", "w") as file:
        file.write(content)


def _create_headers(title: str):
    return f"<h1>{title}</h1>"


def _create_table_headers():
    return """
    <table>
        <tr>
            <th> TaxiID </th>
            <th> Pickup time </th>
            <th> Dropoff time </th>
            <th> Passenger count </th>
            <th> Trip Distance </th>
            <th> Total amount </th>
        </tr>
    """


def _close_table_headers():
    return "</table>"


def _add_ride(ride):
    row_strategy = strategy_report_data_row.HtmlRow()

    row_strategy = strategy_report_data_row.RowGenerator(row_strategy, ride)

    return row_strategy.run_formatting()