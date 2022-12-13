from typing import Dict

from entity.abstract_srorage import AbstractStorage

class Request:
    def __init__(self, request_str: str, storages: Dict[str, AbstractStorage]):
        split_request = request_str.lower().split(' ')
        if len(split_request) != 7:
    # TODO: Ощибка

        self.amount = int(split_request[1])
        self.product = split_request[2]
        self.destination = split_request[4]
        self.departure = split_request[6]

        if self.destination not in storages or self.departure not in storages:
    # TODO: Ощибка