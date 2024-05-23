# Simple Factory Creational pattern
# Usado para generar una clase especializada para cada tipo de reporteque se pueda utilizar

class Web:

    def __init__(self, rides):
        self.rides = rides


class Print:

    def __init__(self, rides):
        self.rides = rides


def get_report(report_type: str, rides):
    if report_type == "web":
        return Web(rides)
    elif report_type == "print":
        return Print(rides)
    else:
        raise Exception(f"Formato \"{report_type}\" no reconocido")