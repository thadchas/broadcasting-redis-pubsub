import logging
import sys

from redis import Redis


class ServerMaster:
    def __init__(self):
        """ SeverMaster class for Broadcasting messages to all server
        """

        self.redis = Redis(host='localhost', port=6379, db=0)
        self.pubsub = self.redis.pubsub()

    def subscribe(self, channels: list):
        """Create subscription of channels
        :param channels:
        :return ret_vals
        """
        self.pubsub.subscribe(*channels)
        logging.info(f'#### Start subscribe to {channels} ####')
        for message in self.pubsub.listen():
            if message['type'] == 'message':
                self.publish('children', message['data'])

    def publish(self, channel, message):
        """Publish messages to channel
        :param channel: destination topic for children
        :param message: original message
        :return: status
        """

        logging.info(f'#### Published {message} to {channel} channel')
        return self.redis.publish(channel, message)


def main():
    s = ServerMaster()
    logging.info('### Master Server Start ####')
    s.subscribe(['parent_children'])


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    sys.exit(main())
