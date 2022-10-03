import logging
import sys

from server_master import ServerMaster


class ServerA(ServerMaster):
    def __init__(self):
        super().__init__()

    def subscribe(self, channels: list):
        """Create subscription of channels
        :param channels:
        :return ret_vals
        """
        self.pubsub.subscribe(*channels)
        logging.info(f'#### Start subscribe to {channels} ####')
        for q in self.pubsub.listen():
            if q['type'] == 'message':
                logging.info(f"#### Got a new message {q['data']} ####")


def main():
    s = ServerA()
    logging.info('### Server A Start ####')
    s.subscribe(['children'])


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    sys.exit(main())
