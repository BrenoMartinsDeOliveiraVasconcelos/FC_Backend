import datetime
import csv


# Função para registrado para ativação e desativação
def reg(mode, dontregister):
    # 0 é alarme desativado, 1 é alarme ativado

    if dontregister == 0:
        with open("C:\\FC_Backend\\registro.csv", "a", encoding="utf-8", newline='') as regist:
            file = csv.writer(regist, delimiter=";")
            lines = []
            row = [datetime.datetime.now().strftime("%d/%m/%Y %H:%M")]
                        # Gambiarra pra eliminar duplicações desnecessárias
            with open("C:\\FC_Backend\\registro.csv", "r", newline='', encoding="utf-8") as reg_r:
                filer = csv.reader(reg_r, delimiter=";")

                for r in filer:
                    lines.append(r)

            if mode == "0":
                row.append("DESATIVADO")
            elif mode == "1":
                row.append("ATIVADO")
            else:
                pass

            if lines[-1][1] != row[1]:
                file.writerow(row)
