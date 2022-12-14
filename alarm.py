import multiprocessing
from backend_lib import tools, functions


def alarmsystem():
    alarm_sound = multiprocessing.Process(target=functions.play, args=())
    alarm_sound.start()
    run = 0
    while True:
        run += 1
        # Pra fechar a thread através do programa principal
        close_thread = open("C:\\FC_Backend\\pid\\alarm_thread", "r")
        if close_thread.readline().strip("\n") == "1":
            close_thread.close()

            closew = open("C:\\FC_Backend\\pid\\alarm_thread", "w")
            closew.write("0")
            alarm_sound.terminate()

            tools.reg("-1", 0)
            exit(0)

        file = open("C:\\FC_Backend\\alarm.fc", "r")
        content = file.readline().split("\n")
        index = -1

        # Andando pelo arquivo
        for mode in content:
            index += 1

            # Checa a ativação do alarme
            if index == 0:
                tools.reg(mode, 0)
        file.close()


if __name__ == '__main__':
    tools.reg("-2", 0)
    alarmsystem()
