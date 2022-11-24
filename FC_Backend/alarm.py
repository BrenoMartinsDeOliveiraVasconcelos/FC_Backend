import os
import multiprocessing
from backend_lib import tools, functions


def alarmsystem():
    alarm_sound = multiprocessing.Process(target=functions.play, args=())
    alarm_sound.start()
    while True:
        # Pra fechar a thread através do programa principal
        close_thread = open("C:\\FC_Backend\\pid\\alarm_thread", "r+")
        if close_thread.readline().strip("\n") == "1":
            close_thread.write("0")
            alarm_sound.terminate()

            close_thread.close()
            exit(0)

        close_thread.close()

        file = open("C:\\FC_Backend\\alarm.fc", "r")
        content = file.readline().split("\n")
        index = -1
        error = 0

        # Andando pelo arquivo
        for text in content:
            index += 1

            # Checa a ativação do alarme
            if index == 0:
                if text == "1":
                    error = 0
                elif text == "0":
                    error = 1
                tools.reg(text, error)
        file.close()


if __name__ == '__main__':
    alarmsystem()