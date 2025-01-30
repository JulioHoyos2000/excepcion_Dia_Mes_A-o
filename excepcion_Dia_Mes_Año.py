from datetime import datetime


class DiaInvalidoException(Exception):
    pass


class MesInvalidoException(Exception):
    pass


class AnioInvalidoException(Exception):
    pass


def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def obtener_fecha():
    while True:
        try:
            fecha_str = input("Ingrese una fecha en formato DD/MM/AAAA: ")
            dia, mes, anio = map(int, fecha_str.split('/'))

            if anio != 2025:
                raise AnioInvalidoException("Solo se permiten fechas del año 2025.")

            dias_por_mes = {
                1: 31, 2: 29 if es_bisiesto(anio) else 28, 3: 31, 4: 30,
                5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
            }

            if mes < 1 or mes > 12:
                raise MesInvalidoException("Mes inválido. Debe estar entre 1 y 12.")

            if dia < 1 or dia > dias_por_mes[mes]:
                raise DiaInvalidoException(
                    f"Día inválido. Para el mes {mes}, debe estar entre 1 y {dias_por_mes[mes]}.")

            fecha = datetime(anio, mes, dia)
            return fecha
        except ValueError:
            print("Error: Formato de fecha incorrecto. Intente nuevamente.")
        except DiaInvalidoException as e:
            print(f"Error: {e}")
        except MesInvalidoException as e:
            print(f"Error: {e}")
        except AnioInvalidoException as e:
            print(f"Error: {e}")


def main():
    fecha = obtener_fecha()
    print(f"Fecha válida ingresada: {fecha.strftime('%d/%m/%Y')}")


if __name__ == "__main__":
    main()
