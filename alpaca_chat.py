# Filename: alpaca_chat.py

import os
from subprocess import Popen, PIPE

class AlpacaChat:
    def __init__(self, alpaca_dir: str="."):
        """
        Initialize the AlpacaChat object.

        :param alpaca_dir: The path to the Alpaca-7B directory.
        """
        self.alpaca_dir = alpaca_dir
        os.chdir(self.alpaca_dir)
        self.chat = Popen(["chat.exe"], stdin=PIPE, stdout=PIPE, stderr=PIPE)

    def send_message(self, prompt: str) -> str:
        """
        Send a message to chat.exe and receive its response.

        :param prompt: The input message to send to chat.exe.
        :return: The response from chat.exe.
        """
        self.chat.stdin.write(prompt.encode("utf-8") + b"\n")
        self.chat.stdin.flush()

        response = b""
        while not response.startswith(b"> \x1b[1m\x1b[32m\x1b[0m"):
            response = self.chat.stdout.readline()
        response = response[len(b"> \x1b[1m\x1b[32m\x1b[0m"):-len(b"\x1b[0m\r\n")]
        return response.decode("utf-8")

def main():
    alpaca_chat = AlpacaChat()

    while True:
        prompt = input("> ")
        response = alpaca_chat.send_message(prompt)
        print(response)

if __name__ == "__main__":
    main()
