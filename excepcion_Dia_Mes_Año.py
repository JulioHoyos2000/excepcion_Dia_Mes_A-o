from datetime import datetime

class DiaInvalidoException(Exception):
    pass


class MesInvalidoException(Exception):
    pass


class AñoInvalidoException(Exception):
    pass


def obtener_fecha():
    while True:
        try:
            fecha_str = input("Ingrese una fecha en formato DD/MM/AAAA: ")
            dia, mes, año = map(int, fecha_str.split('/'))

            if dia < 1 or dia > 31:
                raise DiaInvalidoException("Día inválido. Debe estar entre 1 y 31.")
            if mes < 1 or mes > 12:
                raise MesInvalidoException("Mes inválido. Debe estar entre 1 y 12.")
            if año < 1:
                raise AñoInvalidoException("Año inválido. Debe ser mayor que 0.")

            fecha = datetime(año, mes, dia)
            return fecha
        except ValueError:
            print("Error: Formato de fecha incorrecto. Intente nuevamente.")
        except DiaInvalidoException as e:
            print(f"Error: {e}")
        except MesInvalidoException as e:
            print(f"Error: {e}")
        except AñoInvalidoException as e:
            print(f"Error: {e}")


def main():
    fecha = obtener_fecha()
    print(f"Fecha válida ingresada: {fecha.strftime('%d/%m/%Y')}")


if __name__ == "__main__":
    main()