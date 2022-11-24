import playsound
import multiprocessing
import os
import subprocess


def playsd(path):
    while True:
        playsound.playsound(path, block=True)


def play():
    running = False

    while True:
        if open("C:\\FC_Backend\\alarm.fc", "r").readline().strip("\n") == "1":
            tg = multiprocessing.Process(target=playsd, args=("C:\\FC_Backend\\alarm.mp3",))
            if not running:
                running = True
                tg.start()
                open("C:\\FC_Backend\\pid\\pid", "w+").write(str(tg.pid))
        else:
            try:
                with open(os.devnull, 'wb') as dn:
                    subprocess.run(args=["taskkill", "/F", "/PID",
                                         f"{open('C:/FC_Backend/pid/pid', 'r').readlines()[0]}"], stdout=dn,
                                   stderr=subprocess.STDOUT)
            except subprocess.SubprocessError:
                pass
            running = False
