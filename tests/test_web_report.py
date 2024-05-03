import pytest
import os.path
from datetime import datetime
from patterns.csv_utils import Ride
import patterns.web_report as web_report

#datos a usar en el unit test
@pytest.fixture
def test_rides_list():
    return [
        Ride(
            error= '',
            taxi_id= 1,
            pick_up_time= datetime.strptime('2018-01-01 00:30:26', '%Y-%m-%d %H:%M:%S'),
            drop_of_time= datetime.strptime('2018-01-01 00:46:42', '%Y-%m-%d %H:%M:%S'),
            passenger_count= 2,
            trip_distance= 3.5,
            tolls_amount= 15.8
        ),
        Ride(
            error= '',
            taxi_id= 2,
            pick_up_time= datetime.strptime('2018-02-10 15:10:30', '%Y-%m-%d %H:%M:%S'),
            drop_of_time= datetime.strptime('2018-02-10 15:22:11', '%Y-%m-%d %H:%M:%S'),
            passenger_count= 1,
            trip_distance= 4.1,
            tolls_amount= 20.99
        )
    ]

#comprueba que se genera un archivo html
def test_generate_report(test_rides_list):

    #si el archivo ya existia por prueba anterior, borra
    if os.path.exists('./financial-report.html'):
        os.remove('./financial-report.html')

    #genera el string de etiquetas html
    test_report = web_report.create_content(test_rides_list)

    #comprueba que el string de html no está vacío
    assert test_report is not None and test_report != ''

    #exporta string a archivo .html
    web_report.create_file(test_report)

    #comprueba que el archivo existe en directorio
    assert os.path.exists('./financial-report.html') is True