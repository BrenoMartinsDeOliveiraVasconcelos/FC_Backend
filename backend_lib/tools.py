import datetime
import csv


# Função para registrado para ativação e desativação
def reg(mode, dontregister):
    # 0 é alarme desativado, 1 é alarme ativado

    if dontregister == 0:
        with open("C:\\FC_Backend\\registro.csv", "a", encoding="utf-8", newline='') as regist:
            file = csv.writer(regist, delimiter=";", quoting=csv.QUOTE_NONE, escapechar=' ')
            row = [f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}']
            rows = []

            if mode == "-2":
                row.append("PROGRAMA INICIADO")
            elif mode == "-1":
                row.append("PROGRAMA FECHADO")
            elif mode == "0":
                row.append("ALARME DESATIVADO")
            elif mode == "1":
                row.append("ALARME ATIVADO")
            else:
                pass

            with open("C:\\FC_Backend\\registro.csv", "r", encoding="utf-8", newline='') as rd:
                fl = csv.reader(rd, delimiter=";", quoting=csv.QUOTE_NONE, escapechar=' ')

                for r in fl:
                    rows.append(r)
            try:
                if rows[-1][1] != row[1]:
                    file.writerow(row)
            except IndexError:
                file.writerow(row)
