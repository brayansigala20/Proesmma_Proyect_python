import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from dotenv import load_dotenv
import os as OS
from openpyxl.comments import Comment

load_dotenv()


class ExcelInventory:
    def __init__(self, file_excel_nuevaplaneacion, file_excel_controlalmacen) -> None:
        self.file_excel_nuevaplaneacion = file_excel_nuevaplaneacion
        self.file_excel_controlalmacen = file_excel_controlalmacen

    @property
    def excelNuevaPlaneacion(self):
        return pd.read_excel(
            self.file_excel_nuevaplaneacion["path"],
            sheet_name=self.file_excel_nuevaplaneacion["sheet"],
        )

    @property
    def excelControlAlmacen(self):
        return pd.read_excel(
            self.file_excel_controlalmacen["path"],
            sheet_name=self.file_excel_controlalmacen["sheet"],
            header=0,
        )

    @property
    def toExcelEntradas(self):
        return pd.read_excel(
            self.file_excel_controlalmacen["path"],
            sheet_name="ENTRADAS",
        )

    def toExcelSalidas(self):
        return pd.read_excel(
            self.file_excel_controlalmacen["path"],
            sheet_name="SALIDAS",
        )

    def parse_inventory(self):
        sku_inventary = self.excelControlAlmacen[["SKU", "INVENTARIO (TON)"]]

        sku_inventary.loc[:, "INVENTARIO (TON)"] = sku_inventary[
            "INVENTARIO (TON)"
        ].astype(int)

        return sku_inventary

    def join_excel(self, excel1, excel2):
        mapeo_inventario = excel2.set_index("SKU")["INVENTARIO (TON)"].to_dict()

        excel1["INVENTARIO FISICO "] = (
            excel1["ID PRODUCTO "]
            .map(mapeo_inventario)
            .fillna(excel1["INVENTARIO FISICO "])
        )
        return excel1

    def save_updated_excel(self, updated_excel):
        wb = load_workbook(self.file_excel_nuevaplaneacion["path"])
        ws = wb[self.file_excel_nuevaplaneacion["sheet"]]

        comments = {
            cell.coordinate: cell.comment
            for row in ws.iter_rows(min_row=2, max_row=ws.max_row)
            for cell in row
            if cell.comment
        }

        ws.delete_rows(2, ws.max_row)

        for r_idx, row in enumerate(
            dataframe_to_rows(updated_excel, index=False, header=True), 1
        ):
            for c_idx, value in enumerate(row, 1):
                cell = ws.cell(row=r_idx, column=c_idx, value=value)
                if cell.coordinate in comments:
                    cell.comment = comments[cell.coordinate]

        wb.save(self.file_excel_nuevaplaneacion["path"])

    def bl_excel(self):
        last_entries = self.toExcelEntradas[
            self.toExcelEntradas["FECHA DE REGISTRO"] == "2024-06-25"
        ]
        dataframe_excelNuevaPlaneacion = self.excelNuevaPlaneacion
        inventory_last = last_entries.set_index("SKU")["CANTIDAD"].to_dict()

        inventtory_map = dataframe_excelNuevaPlaneacion["ID PRODUCTO "].map(
            inventory_last
        )

        dataframe_excelNuevaPlaneacion["INVENTARIO EN TRANSITO "] = (
            dataframe_excelNuevaPlaneacion["INVENTARIO EN TRANSITO "]
            - inventtory_map.fillna(0)
        )
        workbook = load_workbook(self.file_excel_nuevaplaneacion["path"])
        sheet = workbook["INVENTARIO ACTUAL "]

        comments = {
            cell.coordinate: cell.comment
            for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row)
            for cell in row
            if cell.comment
        }

        sheet.delete_rows(2, sheet.max_row)

        for r_idx, row in enumerate(
            dataframe_to_rows(dataframe_excelNuevaPlaneacion, index=False, header=True),
            1,
        ):
            for c_idx, value in enumerate(row, 1):
                cell = sheet.cell(row=r_idx, column=c_idx, value=value)
                if cell.coordinate in comments:
                    cell.comment = comments[cell.coordinate]

        workbook.save(self.file_excel_nuevaplaneacion["path"])

        bl = last_entries.set_index("SKU")["OC / BL"].to_dict()

        producto_fila = None
        for producto_id, comment_to_remove in bl.items():
            producto_id = producto_id.lower().strip().replace(" ", "")
            for index, row in dataframe_excelNuevaPlaneacion.iterrows():
                if (
                    row["ID PRODUCTO "].lower().strip().replace(" ", "")
                    == producto_id.lower()
                ):

                    producto_fila = index + 2
                    break

            if producto_fila:
                cell = sheet[f"D{producto_fila}"]

                if cell.comment:
                    existing_comment = cell.comment.text
                    if comment_to_remove in existing_comment:
                        new_comment_text = existing_comment.replace(
                            comment_to_remove, ""
                        ).strip()
                        if new_comment_text:
                            cell.comment = Comment(
                                new_comment_text, cell.comment.author
                            )
                        else:
                            cell.comment = None
                        print(
                            f"Comentario '{comment_to_remove}' eliminado de la celda D{producto_fila}"
                        )
                    else:
                        print(
                            f"El comentario '{comment_to_remove}' no se encontró en la celda E{producto_fila}"
                        )
                else:
                    print(f"No hay comentario existente en la celda E{producto_fila}")
            else:
                print(f"Producto con ID {producto_id} no encontrado.")

        workbook.save(self.file_excel_nuevaplaneacion["path"])
        column_index = dataframe_excelNuevaPlaneacion.columns.get_loc(
            "ORDENES COLOCADAS "
        )
        return dataframe_excelNuevaPlaneacion.iloc[:, : column_index + 1]

    @property
    def process(self):
        nueva_planeacion = self.excelNuevaPlaneacion
        parsed_inventory = self.parse_inventory()
        updated_excel = self.join_excel(nueva_planeacion, parsed_inventory)
        self.save_updated_excel(updated_excel)
        update_finalexcel = self.bl_excel()
        return update_finalexcel


if __name__ == "__main__":
    nueva_planeacion_path = OS.getenv("NUEVA_PLANEACION_PATH")
    control_almacen_path = OS.getenv("CONTROL_ALMACEN_PATH")
    print(nueva_planeacion_path)

    inventory = ExcelInventory(
        {"path": nueva_planeacion_path, "sheet": "INVENTARIO ACTUAL "},
        {"path": control_almacen_path, "sheet": "SKU - COMPRAS"},
    )
    update_excel = inventory.process

    print(update_excel)
