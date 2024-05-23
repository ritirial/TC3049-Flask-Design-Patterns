# Facade Structural pattern
# Se enmascara la operación de exportación del string de reporte, el codigo principal
# no conoce que el reporte html usa una función .create_file(),
# mientras que el reporte en texto usa un metodo print()

from patterns import web_report
from patterns import print_reporter

class Facade:

    def export_reports_operation(web_object, print_object):
        web_report_operations(web_object)
        print_report_operations(print_object)


def web_report_operations(web_object):
    html_content = web_report.create_content(web_object.rides)
    web_report.create_file(html_content)


def print_report_operations(print_object):
    text_content = print_reporter.create_content(print_object.rides)
    print(text_content)