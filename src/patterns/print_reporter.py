from patterns import strategy_report_data_row

#funcion principal, llama a funciones especializadas para construir todo el documento
def create_content(rides):
    #encabezado
    builder = [_create_headers("Taxi Report"), _create_table_headers()]
    #filas
    for ride in rides:
        builder.append(_add_ride(ride))
    #final del reporte
    builder.append(_close_table_headers())

    #return html as string
    return "".join(builder)


def _create_headers(title: str):
    return f"{title}\n"

#encabezados
def _create_table_headers():
    return "TaxiID\tPickup time\t\tDropoff time\t\tPassenger count\tTrip Distance\tTotal amount\n"

#termina reporte
def _close_table_headers():
    return "\n"

#genera string de fila
def _add_ride(ride):
    row_strategy = strategy_report_data_row.TextRow()

    row_strategy = strategy_report_data_row.RowGenerator(row_strategy, ride)

    return row_strategy.run_formatting()
