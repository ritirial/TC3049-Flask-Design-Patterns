# Strategy Behavioral pattern
# Usado para separar en nuevas clases las funciones de formateo de filas
# para los diferentes tipos de reportes

import abc

class Strategy(abc.ABC):

    def run_formatting(self, ride):
        raise Exception("I am an interface")


class HtmlRow:

    def run_formatting(self, ride):
        return "".join([
        "<tr>",
        f"<td>{ride.taxi_id}</td>",
        f"<td>{ride.pick_up_time.isoformat()}</td>",
        f"<td>{ride.drop_of_time.isoformat()}</td>",
        f"<td>{ride.passenger_count}</td>",
        f"<td>{ride.trip_distance}</td>",
        f"<td>{f"<span style='color:red'>{ride.tolls_amount}</span>" if ride.tolls_amount < 0 else ride.tolls_amount}</td>",
        "</tr>"
    ])


class TextRow:

    def run_formatting(self, ride):
        return "\t".join([
        f"{ride.taxi_id}",
        f"{ride.pick_up_time.isoformat()}",
        f"{ride.drop_of_time.isoformat()}",
        f"{ride.passenger_count}\t",
        f"{ride.trip_distance}\t",
        f"{f"({ride.tolls_amount})" if ride.tolls_amount < 0 else ride.tolls_amount}\t",
        f"\n"
    ])


class RowGenerator:

    def __init__(self, strategy, ride):
        self.strategy = strategy
        self.ride = ride

    def run_formatting(self):
        return self.strategy.run_formatting(self.ride)
