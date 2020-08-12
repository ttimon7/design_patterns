# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from receivers import Receiver, SimpleTCPReceiver, SimpleUDPReceiver
from transmitters import Transmitter, SimpleTCPTransmitter, SimpleUDPTransmitter


class CommunicatorFactory(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def create_receiver(cls, address: str, port: int) -> Receiver:
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def create_transmitter(cls) -> Transmitter:
        raise NotImplementedError()


class SimpleTCPCommunicatorFactory(CommunicatorFactory):

    @classmethod
    def create_receiver(cls, address: str, port: int) -> Receiver:
        return SimpleTCPReceiver(address=address, port=port)

    @classmethod
    def create_transmitter(cls) -> Transmitter:
        return SimpleTCPTransmitter()


class SimpleUDPCommunicatorFactory(CommunicatorFactory):

    @classmethod
    def create_receiver(cls, address: str, port: int) -> Receiver:
        return SimpleUDPReceiver(address=address, port=port)

    @classmethod
    def create_transmitter(cls) -> Transmitter:
        return SimpleUDPTransmitter()
