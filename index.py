# nombres = """brayan sigala, jose martinez, pablo montero, luis torres"""

# NOMBRES_1 = nombres[0:13]
# NOMBRES_2 = nombres[15:]

# print(f"{NOMBRES_1} y  {NOMBRES_2}")

# calculadora

# num1 = input('Ingresa el primer numero ')
# num2 = input('Ingresa el segun numero ')

# edad = 56

# if edad > 65:
#    print("tienes un super descuento")

# elif edad > 55:
#    print("tienes un descuento")

# elif edad > 18:
#    print("puedes entrar")
# else:
#    print("no puedes entrar")

# condicionales ternarios
# EDAD = 20
# MENSAJE = "Es mayor" if EDAD >= 18 else "Es menor"
# print(MENSAJE)

# operadores logicos and not or

# AGE = 18
# DRIVE_CARD = False
# DRIVE_COURSE = True

# if AGE >= 18 and DRIVE_CARD and DRIVE_COURSE:
#     print("puede conducir sin problema")

# if AGE >= 18 and not (DRIVE_CARD and DRIVE_COURSE):
#     print("puede conducir pero no cuenta con la total aprobacion")

# if AGE < 18 and not (DRIVE_CARD and DRIVE_COURSE):
#     print("no puede")


# Cadena de comparacion

# import pandas as pd
# AGE = 25

# Simplify chained comparison between the operands (esto es un error de slint y dice que se puede simplificar)
# if AGE >= 18 and AGE <= 60:
#     print("puede pasar")

# # aqui la manera simplificada ya que solo ocupa una variable
# if 18 <= AGE <= 60:
#     print("puede pasar")

# lista = ['pepe', 'jose', 'lalo', 'pedro']

# for index in lista:
#     print(index)

# # Funcion con xArgument paramentro iterable

# def new_function(*numbers):
#     res = 0
#     for number in numbers:
#         res = number * 2
#     return res


# print(new_function(5, 4, 5))

# # Funcion con kwArgument paramentro

# def new_function(**numbers):
#     print(numbers["n1"])


# new_function(n1=5, n2=4, n3=5)


# Palindromo

# def is_palindromo(string):
#     string_formated = string.lower().replace(" ", "")

#     if string_formated == "".join(reversed(string_formated)):
#         return "es Palindromo"
#     return "no es palindromo"


# print(is_palindromo("ana ana"))

# mascotas = ["perro", "gato", "camaleon", "serpiente"]

# for indice, mascota in enumerate(mascotas):
#     print(indice, mascota)

# import re

# # HTML provisto en una variable (supongamos que esto es lo que obtienes en Power Automate)
# html_body = """
# <html>
# <head>
# <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
# </head>
# <body>
# <div dir="ltr">
# <div class="gmail_quote">
# <div dir="ltr">
# <div class="gmail_quote">
# <div dir="ltr">
# <div dir="ltr">
# <div class="gmail_quote">
# <blockquote class="gmail_quote" style="margin:0px 0px 0px 0.8ex;border-left:1px solid rgb(204,204,204);padding-left:1ex">
# <div dir="ltr">
# <div class="gmail_quote">
# <div dir="ltr" class="gmail_attr"><br>
# </div>
# <div>
# <div lang="ES-MX">
# <div>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">Hello</span><span lang="EN-US">
# <span style="color:black">Cindy,<u></u><u></u></span></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">&nbsp;<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">Hope you are well.<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">&nbsp;<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">Please find attached PO
# </span><b><span lang="EN-US">2382</span></b><span lang="EN-US" style="color:black">
# </span><span lang="EN-US">m<span style="color:black">ake sure to use a DOUBLE SUPER BAG 3 LAYERS 2 TON WRAPPED IN PLASTIC WITH UV RESISTANCE since we don’t want to break it at port. Kindly advise ETD for this material, we need them to be shipped</span> as shown:<span style="color:black"><u></u><u></u></span></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US"><u></u>&nbsp;<u></u></span></p>
# <table border="0" cellspacing="0" cellpadding="0" width="595" style="width:446.5pt;margin-left:0.1pt;border-collapse:collapse">
# <tbody>
# <tr style="height:15.75pt">
# <td width="80" nowrap="" style="width:60pt;border:1pt solid windowtext;padding:0cm 3.5pt;height:15.75pt">
# <p class="MsoNormal" align="center" style="text-align:center"><b><span style="color:black">PO
# <u></u><u></u></span></b></p>
# </td>
# <td width="80" nowrap="" style="width:60pt;border-top:1pt solid windowtext;border-right:1pt solid windowtext;border-bottom:1pt solid windowtext;border-left:none;padding:0cm 3.5pt;height:15.75pt">
# <p class="MsoNormal" align="center" style="text-align:center"><b><span style="color:black">TONS<u></u><u></u></span></b></p>
# </td>
# <td width="89" nowrap="" style="width:67.1pt;border-top:1pt solid windowtext;border-right:1pt solid windowtext;border-bottom:1pt solid windowtext;border-left:none;padding:0cm 3.5pt;height:15.75pt">
# <p class="MsoNormal" align="center" style="text-align:center"><b><span style="color:black">SIZE
# <u></u><u></u></span></b></p>
# </td>
# <td width="80" nowrap="" style="width:60.2pt;border-top:1pt solid windowtext;border-right:1pt solid windowtext;border-bottom:1pt solid windowtext;border-left:none;padding:0cm 3.5pt;height:15.75pt">
# <p class="MsoNormal" align="center" style="text-align:center"><b><span style="color:black">ETD<u></u><u></u></span></b></p>
# </td>
# <td width="80" nowrap="" style="width:60.2pt;border-top:1pt solid windowtext;border-right:1pt solid windowtext;border-bottom:1pt solid windowtext;border-left:none;padding:0cm 3.5pt;height:15.75pt">
# <p class="MsoNormal" align="center" style="text-align:center"><b><span style="color:black">ETA
# <u></u><u></u></span></b></p>
# </td>
# <td width="105" nowrap="" style="width:79pt;border-top:1pt solid windowtext;border-right:1pt solid windowtext;border-bottom:1pt solid windowtext;border-left:none;padding:0cm 3.5pt;height:15.75pt">
# <p class="MsoNormal" align="center" style="text-align:center"><b><span style="color:black">INCOTERM
# <u></u><u></u></span></b></p>
# </td>
# <td width="80" nowrap="" style="width:60pt;border-top:1pt solid windowtext;border-right:1pt solid windowtext;border-bottom:1pt solid windowtext;border-left:none;padding:0cm 3.5pt;height:15.75pt">
# <p class="MsoNormal" align="center" style="text-align:center"><b><span style="color:black">PACKING
# <u></u><u></u></span></b></p>
# </td>
# </tr>
# <tr style="height:45.75pt">
# <td width="80" style="width:60pt;border-right:1pt solid windowtext;border-bottom:1pt solid windowtext;border-left:1pt solid windowtext;border-top:none;padding:0cm 3.5pt;height:45.75pt">
# <p class="MsoNormal" align="center" style="text-align:center"><span style="color:black">2382<u></u><u></u></span></p>
# </td>
# <td width="80" nowrap="" style="width:60pt;border-top:none;border-left:none;border-bottom:1pt solid windowtext;border-right:1pt solid windowtext;padding:0cm 3.5pt;height:45.75pt">
# <p class="MsoNormal" align="center" style="text-align:center"><span style="color:black">52<u></u><u></u></span></p>
# </td>
# <td width="89" style="width:67.1pt;border-top:none;border-left:none;border-bottom:1pt solid windowtext;border-right:1pt solid windowtext;padding:0cm 3.5pt;height:45.75pt">
# <p class="MsoNormal" align="center" style="text-align:center"><span style="color:black">40MM 2-3%<u></u><u></u></span></p>
# </td>
# <td width="80" style="width:60.2pt;border-top:none;border-left:none;border-bottom:1pt solid windowtext;border-right:1pt solid windowtext;padding:0cm 3.5pt;height:45.75pt">
# <p class="MsoNormal" align="center" style="text-align:center"><span style="color:black">29/01/2024<u></u><u></u></span></p>
# </td>
# <td width="80" nowrap="" style="width:60.2pt;border-top:none;border-left:none;border-bottom:1pt solid windowtext;border-right:1pt solid windowtext;padding:0cm 3.5pt;height:45.75pt">
# <p class="MsoNormal" align="center" style="text-align:center"><span style="color:black">18/02/2024<u></u><u></u></span></p>
# </td>
# <td width="105" style="width:79pt;border-top:none;border-left:none;border-bottom:1pt solid windowtext;border-right:1pt solid windowtext;padding:0cm 3.5pt;height:45.75pt">
# <p class="MsoNormal" align="center" style="text-align:center"><span style="color:black">CIF MANZANILLO
# <u></u><u></u></span></p>
# </td>
# <td width="80" style="width:60pt;border-top:none;border-left:none;border-bottom:1pt solid windowtext;border-right:1pt solid windowtext;padding:0cm 3.5pt;height:45.75pt">
# <p class="MsoNormal" align="center" style="text-align:center"><span style="color:black">SUPERBAG 2 TONS
# <u></u><u></u></span></p>
# </td>
# </tr>
# </tbody>
# </table>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US"><u></u>&nbsp;<u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">Please work with your quality team and emphasize the importance of this. As Eric, has talked to you about our quality policy, if ball does not comply with the quality standards, we will
#  make a penalty.</span><span lang="EN-US"><u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">&nbsp;<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">Hello </span>
# <span lang="es-419"><a href="mailto:eric@proesmma.com" target="_blank"><span lang="EN-US">@Eric</span></a><span style="color:black">
# </span></span><span lang="EN-US" style="color:black">Can you coordinate with </span>
# <span lang="EN-US">Cindy<span style="color:black">, in order to check material please?</span><u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">&nbsp;<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">Regarding the quality requests, we are also going to implement a new way to track all our product so from now on we need you to<b> print</b> PROESMMA LOGO, batch number and number of
#  packages in each super bag, <b>remember to use two double super bags</b>.<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">&nbsp;<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">Batch Number:<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">Will include initial always will be T (T it is from TAIHONG), production date (YY-MM-DD), size( in two digits 10, 20, 25), material (always will use A= chrome, and for hcr% is the following:<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">&nbsp;<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US">&nbsp;<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US"><img border="0" width="147" height="223" id="m_-2896664144497463781m_-8396470470194898662m_7620337922913835834m_1704852504993871125m_2176170468362344995Imagen_x0020_2" src="cid:ii_18f2dbe498d4ce8e91"></span><span lang="es-419"><u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US">&nbsp;<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US">&nbsp;<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">&nbsp;Example:
# <b>T22040440AG</b></span><span lang="EN-US"><u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><b><span lang="EN-US" style="color:black">T: TAIHONG</span></b><span lang="EN-US" style="color:black"><u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><b><span lang="EN-US" style="color:black">220404-
# </span></b><span lang="EN-US" style="color:black">production date 2022 April 04 (example)<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><b><span lang="EN-US" style="color:black">Size-
# </span></b><span lang="EN-US" style="color:black">40 means 40 mm”<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">A: Chrome<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><b><span lang="EN-US" style="color:black">% Chrome:&nbsp;
# </span></b><span lang="EN-US" style="color:black">G means 18-20%<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">&nbsp;<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">Please let me know if you have any questions about this batch number .<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><b><span lang="EN-US" style="color:black"><u></u>&nbsp;<u></u></span></b></p>
# <p style="margin:0cm 0cm 0.0001pt"><b><span lang="EN-US" style="color:black;background:yellow">IMPORTANT:
# </span></b><b><span lang="EN-US" style="color:black"><u></u><u></u></span></b></p>
# <p style="margin:0cm 0cm 0.0001pt"><b><span lang="EN-US"><u></u>&nbsp;<u></u></span></b></p>
# <p class="MsoNormal" style="margin-left:36pt"><u></u><span lang="EN-US"><span>1-<span style="font:7pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# </span></span></span><u></u><span lang="EN-US">INCLUDE BATCH NUMBER ON PACKING LIST
# <u></u><u></u></span></p>
# <p class="MsoNormal" style="margin-left:36pt"><u></u><span lang="EN-US"><span>2-<span style="font:7pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# </span></span></span><u></u><span lang="EN-US">SEND PICTURES OF CONTAINERS LOADING<u></u><u></u></span></p>
# <p class="MsoNormal" style="margin-left:36pt"><u></u><span lang="EN-US"><span>3-<span style="font:7pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# </span></span></span><u></u><span lang="EN-US">APPLY FOR 21 DAYS FREE OF DEMURRAGE IN DESTINATION<u></u><u></u></span></p>
# <p class="MsoNormal" style="margin-left:36pt"><u></u><span lang="EN-US" style="background:yellow"><span>4-<span style="font:7pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# </span></span></span><u></u><span lang="EN-US" style="background:yellow">DESCRIPTION OF SIZES AND TONS MUST BE SHOWN ON PACKING LIST
# <u></u><u></u></span></p>
# <p class="MsoNormal" style="margin-left:36pt"><u></u><span lang="EN-US" style="background:yellow"><span>5-<span style="font:7pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# </span></span></span><u></u><span lang="EN-US" style="background:yellow">COMERCIAL INVOICE MUST SHOWN: STEEL BALLS OBTAINED THROUGH&nbsp;STEEL&nbsp;CASTING<u></u><u></u></span></p>
# <p class="MsoNormal"><span lang="EN-US"><u></u>&nbsp;<u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">&nbsp;<u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US" style="color:black">If you have any questions about something, please let me know.</span><span lang="EN-US"><u></u><u></u></span></p>
# <p style="margin:0cm 0cm 0.0001pt"><span lang="EN-US"><u></u>&nbsp;<u></u></span></p>
# <div>
# <p class="MsoNormal"><span lang="EN-US">Saludos,<u></u><u></u></span></p>
# <p class="MsoNormal"><span lang="EN-US">Kind Regards.<u></u><u></u></span></p>
# <p class="MsoNormal"><span><img border="0" width="1240" height="260" id="m_-2896664144497463781m_-8396470470194898662m_7620337922913835834m_1704852504993871125m_2176170468362344995Imagen_x0020_1" src="cid:ii_18f2dbe498d692e332"></span><span lang="EN-US"><u></u><u></u></span></p>
# </div>
# <p class="MsoNormal"><u></u>&nbsp;<u></u></p>
# <p class="MsoNormal"><span><u></u>&nbsp;<u></u></span></p>
# <p class="MsoNormal"><span lang="EN-US"><u></u>&nbsp;<u></u></span></p>
# </div>
# <div id="m_-2896664144497463781m_-8396470470194898662m_7620337922913835834m_1704852504993871125m_2176170468362344995DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2">
# <br>
# <table style="border-top:1px solid rgb(211,212,222)">
# <tbody>
# <tr>
# <td style="width:55px;padding-top:13px"><a href="https://www.avast.com/sig-email?utm_medium=email&amp;utm_source=link&amp;utm_campaign=sig-email&amp;utm_content=emailclient" target="_blank"><img src="https://s-install.avcdn.net/ipm/preview/icons/icon-envelope-tick-round-orange-animated-no-repeat-v1.gif" alt="" width="46" height="29" style="width:46px;height:29px"></a></td>
# <td style="width:470px;padding-top:12px;color:rgb(65,66,78);font-size:13px;font-family:Arial,Helvetica,sans-serif;line-height:18px">
# Libre de virus.<a href="https://www.avast.com/sig-email?utm_medium=email&amp;utm_source=link&amp;utm_campaign=sig-email&amp;utm_content=emailclient" style="color:rgb(68,83,234)" target="_blank">www.avast.com</a></td>
# </tr>
# </tbody>
# </table>
# <a href="#m_-2896664144497463781_m_-8396470470194898662_m_7620337922913835834_m_1704852504993871125_m_2176170468362344995_DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2" width="1" height="1"></a></div>
# </div>
# </div>
# </div>
# </div>
# </blockquote>
# </div>
# </div>
# </div>
# </div>
# </div>
# </div>
# </div>
# </body>
# </html>

# """

# # Encontrar la tabla dentro del cuerpo del correo electrónico
# start_index = html_body.find("<table")
# end_index = html_body.find("</table>", start_index)
# if start_index != -1 and end_index != -1:
#     table_html = html_body[start_index : end_index + len("</table>")]

#     # Expresión regular para encontrar las filas de la tabla
#     row_regex = re.compile(r"<tr[^>]*>(.*?)</tr>", re.DOTALL)
#     # Expresión regular para encontrar las celdas de la fila
#     cell_regex = re.compile(r"<t[dh][^>]*>(.*?)</t[dh]>", re.DOTALL)

#     # Inicializar listas para cada columna de la tabla
#     column1_data = ""
#     column2_data = ""
#     column3_data = ""
#     column4_data = ""
#     column5_data = ""
#     column6_data = ""
#     column7_data = ""

#     # Buscar filas en la tabla
#     for row_match in row_regex.finditer(table_html):
#         row_html = row_match.group(1)
#         # Buscar celdas en la fila
#         cells = cell_regex.findall(row_html)
#         # Si hay suficientes celdas (al menos 7 para cada columna)
#         if len(cells) >= 7:
#             # Obtener el texto de cada celda y agregarlo a la lista de datos de la columna correspondiente
#             column1_data = re.sub(r"<.*?>", "", cells[0])  # Eliminar etiquetas HTML
#             column2_data = re.sub(r"<.*?>", "", cells[1])  # Eliminar etiquetas HTML
#             column3_data = re.sub(r"<.*?>", "", cells[2])  # Eliminar etiquetas HTML
#             column4_data = re.sub(r"<.*?>", "", cells[3])  # Eliminar etiquetas HTML
#             column5_data = re.sub(r"<.*?>", "", cells[4])  # Eliminar etiquetas HTML
#             column6_data = re.sub(r"<.*?>", "", cells[5])  # Eliminar etiquetas HTML
#             column7_data = re.sub(r"<.*?>", "", cells[6])  # Eliminar etiquetas HTML
# print(
#     f"""{column1_data},{column2_data},{column3_data},{column4_data},{column5_data},{column6_data},{column7_data}"""
# )

# date = "5/13/2024 12:00:00 AM"
# split = date.split(" ", maxsplit=1)[0].split("/")
# montBefore = int(split[0]) - 1

# print(montBefore)
# import json

# string = {
#     0: "COMPAÑÍA INDUSTRIAL HANKA SA DE CV",
#     1: "COMPAÑÍA INDUSTRIAL HANKA SA DE CV",
#     2: "COMPAÑÍA INDUSTRIAL HANKA SA DE CV",
#     3: "COMPAÑÍA INDUSTRIAL HANKA SA DE CV",
#     4: "COMPAÑÍA INDUSTRIAL HANKA SA DE CV",
#     5: "COMPAÑÍA INDUSTRIAL HANKA SA DE CV",
#     6: "COMPAÑÍA INDUSTRIAL HANKA SA DE CV",
#     7: "COMPAÑÍA INDUSTRIAL HANKA SA DE CV",
#     8: "COMPAÑÍA INDUSTRIAL HANKA SA DE CV",
#     9: "DEMSA, DESISTE DE SERVICIO",
#     10: "MAZATLAN ELECTRO MAR",
#     11: "SOLUCIONES ESPECIALIZADAS",
#     12: "MINERA ADULARIA EXPLORACION",
#     13: "JOY GLOBAL MEXICO",
#     14: "LOS GATOS",
#     15: "LAS PALAPAS RESTAURANTE",
#     16: " COMUNICACIÓN VERSATIL",
#     17: "JOY GLOBAL MEXICO",
#     18: "JOY GLOBAL MEXICO",
#     19: "AGNICO SONORA",
#     20: "MSI 2000",
#     21: "MSI 2000",
#     22: "LAYNE DE MEXICO SA DE CV",
#     23: "COMUNICACIÓN VERSATIL",
#     24: "COMUNICACIÓN VERSATIL",
#     25: "COMUNICACIÓN VERSATIL",
#     26: "COMUNICACIÓN VERSATIL",
#     27: "COMUNICACIÓN VERSATIL",
#     28: "COMUNICACIÓN VERSATIL",
#     29: "COMUNICACIÓN VERSATIL",
#     30: "COMUNICACIÓN VERSATIL",
#     31: "COMUNICACIÓN VERSATIL",
#     32: "COMUNICACIÓN VERSATIL",
#     33: "COMUNICACIÓN VERSATIL",
#     34: "COMUNICACIÓN VERSATIL",
#     35: "COMUNICACIÓN VERSATIL",
#     36: "COMUNICACIÓN VERSATIL",
#     37: "COMUNICACIÓN VERSATIL",
#     38: "COMUNICACIÓN VERSATIL",
#     39: "COMUNICACIÓN VERSATIL",
#     40: "MAZATLAN ELECTRO MAR",
#     41: "COMUNICACIÓN VERSATIL",
#     42: "COMUNICACIÓN VERSATIL",
#     43: "MINA LA CANTERA",
#     44: "MINA LA CANTERA",
#     45: "MINA LA CANTERA",
#     46: "MINA LA CANTERA",
#     47: "MINA LA CANTERA",
#     48: "MINA LA CANTERA",
#     49: "MINA LA CANTERA",
#     50: "MINA LA CANTERA",
#     51: "RAMIRO REGAL",
#     52: "AGNICO EAGLE MEXICO",
#     53: "AGNICO EAGLE MEXICO",
#     54: "AGNICO SONORA",
#     55: "AGNICO SONORA",
#     56: "AGNICO EAGLE MEXICO",
#     57: "LUIS F",
#     58: "BERNARDO CASTRO",
#     59: "DR. VAGON",
#     60: "BERNARDO CASTRO",
#     61: "JUAN RODRIGUEZ",
#     62: "RADIOCOMUNICACIONES AVANZADA DE ACAPULCO",
#     63: "RADIOCOMUNICACIONES AVANZADA DE ACAPULCO",
#     64: "ANTENA MOVIL BERNARDO REASIGNADA A JAVIER TORRES",
#     65: "MARISOL ALONSO, JESUS SOTO",
#     66: "COMUNICACIÓN VERSATIL",
#     67: "JOY GLOBAL MEXICO(empezar a factura 1 mayo 2024)",
#     68: "MAZATLAN ELECTRO MAR",
#     69: "SOLENSA",
#     70: "COMER INTER",
#     71: "COMER INTER",
#     72: "COMER INTER",
#     73: "COMER INTER",
#     74: "TECSER ENERGIA Y TELECOMUNICACIONES",
#     75: "COMUNICACIÓN VERSATIL",
#     76: "LUIS F",
#     77: "COMUNICACIÓN VERSATIL",
#     78: "COMUNICACIÓN VERSATIL",
#     79: "JOY GLOBAL MEXICO",
#     80: "TECSER ENERGIA Y TELECOMUNICACIONES",
#     81: "MEXICANA DE COBRE S.A. DE C.V.",
#     82: "ARTURO GRAJEDA",
#     83: "ARTURO GRAJEDA",
#     84: "COMUNICACIÓN VERSATIL",
#     85: "COMUNICACIÓN VERSATIL",
#     86: "MINA LA CANTERA",
#     87: "VALDEZ & WOODWARD SC",
#     88: "LIBRE",
#     89: "SOLENSA",
#     90: "GARANTIA ENVIADA A STARLINK",
#     91: "DR. VAGON",
#     92: "LOS GATOS",
#     93: "AL INSTANTE COMUNICACIONES",
#     94: "MINA LA CANTERA",
#     95: "MINA LA CANTERA",
#     96: "VALDEZ & WOODWARD SC",
#     97: "ARTURO GRAJEDA ",
#     98: "TECSER ENERGIA Y TELECOMUNICACIONES",
#     99: "LUIS F",
#     100: "FLAVIO ROBLES",
#     101: "MARISOL ALONSO, JESUS SOTO",
#     102: "COMUNICACIÓN VERSATIL",
#     103: "COMUNICACIÓN VERSATIL",
#     104: "TECSER ENERGIA Y TELECOMUNICACIONES",
#     105: "DR. VAGON",
#     106: "DR. VAGON",
#     107: "TUFESA",
#     108: "ARNOGOLD",
#     109: "HEXAGON",
#     110: "LIBRE",
#     111: "GRUPO MEXICO",
# }


# # Leer el archivo JSON y convertirlo a un diccionario
# # Convertir el diccionario a una cadena JSON
# json_string = json.dumps(string, ensure_ascii=False, indent=4)

# # Mostrar la cadena JSON
# print(json_string)
