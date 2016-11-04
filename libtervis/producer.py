from confluent_kafka import Producer

from libtervis.utils import merge


def make_producer(config):
    return Producer(merge(config.get('common') or {},
                          config.get('producer') or {}))
