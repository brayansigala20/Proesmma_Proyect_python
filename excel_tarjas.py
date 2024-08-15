import pandas as pd
import json

with open("tarjetas.json", "r", encoding="utf-8") as file:
    tarj_Json = json.load(file)


almacenes_tablas = {}

for almacen, table in tarj_Json.items():
    tablas_almacen = {}
    for product, details in table.items():
        tabla = pd.read_excel(
            "C:\\Users\\braya\\Downloads\\proessa\\INVENTARIOS ALMACENES CHIH Y ALMAN.xlsx",
            sheet_name=almacen,
            skiprows=details["fromRow"] - 1,
            nrows=details["toRow"],
            usecols=f'{details["fromColumn"]}:{details["toColumn"]}',
        )

        tabla.columns = [col.split(".")[0].strip() for col in tabla.columns]
        tablas_almacen[product] = tabla
    almacenes_tablas[almacen] = tablas_almacen


# Ahora puedes acceder a las tablas por almacén y por producto

print(almacenes_tablas["CHIH. TARJETA ALMACEN"]["Bola 1.0"])
# print(almacenes_tablas["CHIH. TARJETA ALMACEN"]["Bola 3/4"])
# print(almacenes_tablas["CHIH. TARJETA ALMACEN"]["BOLA 40 MM 18-20%"]["FECHA"])
# print(almacenes_tablas["FORJACHISA"]["Bola 2.0"]["FECHA"])
# print(almacenes_tablas["FORJACHISA"]["Bola 2.5"])
