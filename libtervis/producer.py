import time
import json
import logging
import functools

from confluent_kafka import Producer as KafkaProducer

from libtervis.utils import merge


class Producer(object):

    def __init__(self, config, logger=None):
        if logger is None:
            logger = logging.getLogger(__name__)
        self._producer = KafkaProducer(
            merge(config.get('common') or {},
                  config.get('producer') or {}))
        self.event_count = 0

    def flush(self):
        return self._producer.flush()

    def produce_event(self, project, event, timestamp=None):
        produce = functools.partial(
            self._producer.produce, 'events',
            json.dumps([project, event]).encode('utf-8'),
            key=str(project).encode('utf-8'))

        try:
            produce()
        except BufferError as e:
            self.logger.info(
                'Caught %r, waiting for %s events to be produced',
                e,
                len(self.producer),
            )
            self.producer.flush()  # wait for buffer to empty
            self.logger.info('Done waiting, continue to generate events')
            produce()

        self.event_count += 1

        i = self.event_count
        if i % 1000 == 0:
            if timestamp is None:
                timestamp = time.time()
            self.logger.info('%s events produced, current timestamp is %s',
                             i, timestamp)
