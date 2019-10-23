from threading import Timer

def run():
    print("hello")
    t = Timer(3,run).start()


if __name__ == "__main__":
    run()