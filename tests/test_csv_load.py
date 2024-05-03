import pytest
import patterns.csv_utils as csv_utils

#datos a usar en el unit test
@pytest.fixture
def test_rides():
    return csv_utils.parse_file('taxi-data.csv')


#test de carga de archivo
def test_read_file(test_rides):
    #comprueba que parse_file si generó una lista
    assert test_rides is not None

    #comprueba que hay datos en la lista
    assert len(test_rides) > 0
