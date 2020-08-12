# -*- coding: utf-8 -*-

from random import randint

from factories import CommunicatorFactory, SimpleTCPCommunicatorFactory, SimpleUDPCommunicatorFactory


def get_best_factory() -> CommunicatorFactory:
    available_factories = (SimpleTCPCommunicatorFactory, SimpleUDPCommunicatorFactory)

    return available_factories[randint(0, (len(available_factories) - 1))]


if __name__ == "__main__":
    address = "localhost"
    port = 9999

    factory = get_best_factory()
    receiver = factory.create_receiver(address=address, port=port)
    transmitter = factory.create_transmitter()

    receiver.listen()
    transmitter.send(msg="Hello!", address=address, port=port)
