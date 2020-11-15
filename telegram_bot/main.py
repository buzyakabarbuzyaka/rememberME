from threading import Thread
from src import server, bot

if __name__ == '__main__':
    thread = Thread(target=server.start)
    thread.start()

    bot.start()

