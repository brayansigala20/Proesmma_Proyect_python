import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Leer los archivos Excel con pandas
SKU_COMPRAS = pd.read_excel(
    "C:\\Users\\braya\\Downloads\\proessa\\Proesmma_Email\\CONTROL DE ALMACEN - NUEVO.xlsm",
    sheet_name="SKU - COMPRAS",
    header=0,
)

# Leer el archivo Excel donde se harán las modificaciones
file_excel = "C:\\Users\\braya\\Downloads\\proessa\\Proesmma_Email\\NUEVA PLANEACION NUEVAS MODIFICACIONES.xlsx"
sheet_name = "INVENTARIO ACTUAL "
NUEVA_PLANEACION_INVENTARIO_ACTUAL = pd.read_excel(
    file_excel,
    sheet_name=sheet_name,
)


# Función para parsear el inventario
def parse_inventary():
    sku_inventary = SKU_COMPRAS[["SKU", "INVENTARIO (TON)"]]
    sku_inventary.loc[:, "INVENTARIO (TON)"] = sku_inventary["INVENTARIO (TON)"].astype(
        int
    )
    return sku_inventary


# Función para unir los Excel y actualizar los datos
def join_excel(excel1, excel2):
    mapeo_inventario = excel2.set_index("SKU")["INVENTARIO (TON)"].to_dict()
    excel1["INVENTARIO FISICO "] = (
        excel1["ID PRODUCTO "]
        .map(mapeo_inventario)
        .fillna(excel1["INVENTARIO FISICO "])
    )
    return excel1


update_excel = join_excel(NUEVA_PLANEACION_INVENTARIO_ACTUAL, parse_inventary())


wb = load_workbook(file_excel)
ws = wb[sheet_name]


comments = {}
for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
    for cell in row:
        if cell.comment:
            comments[cell.coordinate] = cell.comment


ws.delete_rows(2, ws.max_row)

for r_idx, row in enumerate(
    dataframe_to_rows(update_excel, index=False, header=True), 1
):
    for c_idx, value in enumerate(row, 1):
        cell = ws.cell(row=r_idx, column=c_idx, value=value)
        coord = cell.coordinate
        if coord in comments:
            cell.comment = comments[coord]


wb.save(file_excel)

print(NUEVA_PLANEACION_INVENTARIO_ACTUAL["INVENTARIO FISICO "])
