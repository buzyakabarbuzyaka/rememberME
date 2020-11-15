from threading import Thread
import bot
import server

if __name__ == '__main__':
    thread = Thread(target=server.start)
    thread.start()

    bot.start()

