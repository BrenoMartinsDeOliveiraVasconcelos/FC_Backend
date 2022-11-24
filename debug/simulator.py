def simulate():
    st = open("C:\\FC_Backend\\alarm.fc", "r").readlines()

    open("C:\\FC_Backend\\alarm.fc", "a").write(str(int("1" if bool(st[1]) else "0")))


if __name__ == '__main__':
    simulate()
