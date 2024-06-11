import openpyxl
import pandas as pd
from openpyxl.comments import Comment
import os

file_excel = "C:\\Users\\braya\\Downloads\\proessa\\NUEVA PLANEACION NUEVAS MODIFICACIONES (1).xlsx"
sheet_name = "INVENTARIO ACTUAL "
NUEVA_PLANEACION_INVENTARIO_ACTUAL = pd.read_excel(
    file_excel,
    sheet_name=sheet_name,
)


VARIABLES_PO = pd.read_excel(
    "C:\\Users\\braya\\Downloads\\proessa\\ExcelVar_Temporal.xlsx", sheet_name="Hoja1"
)


workbook = openpyxl.load_workbook(file_excel)
sheet = workbook[sheet_name]
comment_text = f"PO {VARIABLES_PO['PO'][0]} {VARIABLES_PO['TON'][0]}"
author = "PROESMMA_C3:"


producto_id = VARIABLES_PO["SIZE"][0].lower().strip().replace(" ", "")


producto_fila = None
for index, row in NUEVA_PLANEACION_INVENTARIO_ACTUAL.iterrows():
    if row["MEDIDA "].lower().strip().replace(" ", "") == producto_id:

        producto_fila = index + 2
        break

if producto_fila:
    cell = sheet[f"E{producto_fila}"]
    cellInv = sheet[f"E{producto_fila}"].value
    if cellInv is None:
        cellInv = 0
    sheet[f"E{producto_fila}"] = cellInv + VARIABLES_PO["TON"][0]

    if cell.comment:
        existing_comment = cell.comment.text
        new_comment_text = f"{existing_comment}\n{comment_text}"
        cell.comment = Comment(new_comment_text, author)
    else:
        cell.comment = Comment(comment_text, author)

    print(f"Comentario agregado a la celda E{producto_fila}")
else:
    print(f"Producto con ID {producto_id} no encontrado.")

workbook.save(file_excel)


fileRemovePath = "C:\\Users\\braya\\Downloads\\proessa\\ExcelVar_Temporal.xlsx"


if os.path.exists(fileRemovePath):

    os.remove(fileRemovePath)
    print(f"Archivo {fileRemovePath} eliminado exitosamente.")
else:
    print(f"El archivo {fileRemovePath} no existe.")
