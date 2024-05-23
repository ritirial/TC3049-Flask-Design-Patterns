from patterns import csv_utils
from patterns import simple_factory_report_type
from patterns import facade_report_export

CSV_FILE = "taxi-data.csv"


def main():
    rides = csv_utils.parse_file(CSV_FILE)

    #creational pattern - simple factory
    web_report = simple_factory_report_type.get_report("web", rides)
    print_report = simple_factory_report_type.get_report("print", rides)

    #structural pattern - facade
    facade_report_export.Facade.export_reports_operation(web_report, print_report)

if __name__ == '__main__':
    main()
