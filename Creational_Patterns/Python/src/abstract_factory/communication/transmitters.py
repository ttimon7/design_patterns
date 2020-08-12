# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Transmitter(metaclass=ABCMeta):

    @abstractmethod
    def send(self, msg: str, address: str, port: int) -> None:
        raise NotImplementedError()


class SimpleTCPTransmitter(Transmitter):

    def send(self, msg: str, address: str, port: int) -> None:
        print("Sending TCP message...")


class SimpleUDPTransmitter(Transmitter):

    def send(self, msg: str, address: str, port: int) -> None:
        print("Sending UDP message...")
