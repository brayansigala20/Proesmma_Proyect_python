import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.worksheet.table import Table, TableStyleInfo

# Excel INVENTARIOS ALMACENES CHIH Y ALMAN
ALMACENES_CHIH_Y_ALMAN_SKU = pd.read_excel(
    "C:\\Users\\braya\\Downloads\\proessa\\INVENTARIOS ALMACENES CHIH Y ALMAN.xlsx",
    sheet_name="SKU - COMPRAS",
    header=2,
)

ALMACENES_CHIH_Y_ALMAN_SKU.columns = [
    "SKU",
    "MEDIDA DE BOLA Y DESCRIPCION",
    "INVENTARIO",
    "PROGRAMADO PARA ENTREGA",
    "ENTRADAS DE IMPO",
    "SALIDAS A CLIENTES",
    "INVENTARIO REAL DISPONIBLE",
]


# Excel NUEVA PLANEACION NUEVAS MODIFICACIONES
file_excel = (
    "C:\\Users\\braya\\Downloads\\proessa\\NUEVA PLANEACION NUEVAS MODIFICACIONES.xlsx"
)
sheet_name = "INVENTARIO ACTUAL "
NUEVA_PLANEACION_INVENTARIO_ACTUAL = pd.read_excel(
    file_excel,
    sheet_name=sheet_name,
)


# Conjuncion excel inventarios
def parse_inventary():
    sku_inventary = ALMACENES_CHIH_Y_ALMAN_SKU[["SKU", "INVENTARIO"]]

    for index, row in sku_inventary.iterrows():
        sku_inventary.at[index, "INVENTARIO"] *= 1000

        return sku_inventary


def join_excel(excel1, excel2):
    mapeo_inventario = excel2.set_index("SKU")["INVENTARIO"].to_dict()

    excel1["INVENTARIO FISICO "] = (
        excel1["ID PRODUCTO "]
        .map(mapeo_inventario)
        .fillna(excel1["INVENTARIO FISICO "])
    )

    return excel1


update_excel = join_excel(NUEVA_PLANEACION_INVENTARIO_ACTUAL, parse_inventary())


wb = load_workbook(file_excel)

ws = wb[sheet_name]


ws.delete_rows(2, ws.max_row)
df = pd.DataFrame(update_excel)

for row in dataframe_to_rows(df, index=False, header=True):
    ws.append(row)


ws.delete_rows(2)

wb.save(file_excel)
