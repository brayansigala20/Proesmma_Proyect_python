import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from dotenv import load_dotenv
import os as OS

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

    @property
    def process(self):
        nueva_planeacion = self.excelNuevaPlaneacion
        parsed_inventory = self.parse_inventory()
        updated_excel = self.join_excel(nueva_planeacion, parsed_inventory)
        self.save_updated_excel(updated_excel)
        return updated_excel


if __name__ == "__main__":
    nueva_planeacion_path = OS.getenv("NUEVA_PLANEACION_PATH")
    control_almacen_path = OS.getenv("CONTROL_ALMACEN_PATH")
    print(nueva_planeacion_path)

    inventory = ExcelInventory(
        {"path": nueva_planeacion_path, "sheet": "INVENTARIO ACTUAL "},
        {"path": control_almacen_path, "sheet": "SKU - COMPRAS"},
    )
    update_excel = inventory.process
    print(update_excel["INVENTARIO FISICO "])
