# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Receiver(metaclass=ABCMeta):

    def __init__(self, address: str, port: int) -> None:
        self.address = address
        self.port = port

    @abstractmethod
    def listen(self) -> str:
        raise NotImplementedError()


class SimpleTCPReceiver(Receiver):

    def listen(self) -> str:
        print("Listening for TCP messages...")


class SimpleUDPReceiver(Receiver):

    def listen(self) -> str:
        print("Listening for UDP messages...")
