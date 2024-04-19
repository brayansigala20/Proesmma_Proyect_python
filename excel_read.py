import pandas as pd

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
NUEVA_PLANEACION_INVENTARIO_ACTUAL = pd.read_excel(
    "C:\\Users\\braya\\Downloads\\proessa\\NUEVA PLANEACION NUEVAS MODIFICACIONES (1).xlsx",
    sheet_name="INVENTARIO ACTUAL ",
)


# Conjuncion excel inventarios
sku_inventary = ALMACENES_CHIH_Y_ALMAN_SKU[["SKU", "INVENTARIO"]]

for index, row in sku_inventary.iterrows():
    sku_inventary.at[index, "INVENTARIO"] *= 1000


def join_excel(excel1, excel2):
    mapeo_inventario = excel2.set_index("SKU")["INVENTARIO"].to_dict()

    excel1["INVENTARIO FISICO "] = (
        excel1["ID PRODUCTO "]
        .map(mapeo_inventario)
        .fillna(excel1["INVENTARIO FISICO "])
    )

    return excel1


print(join_excel(NUEVA_PLANEACION_INVENTARIO_ACTUAL, sku_inventary))
