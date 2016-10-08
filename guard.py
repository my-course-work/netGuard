import sys
import time
from socketserver import ThreadingUDPServer
from threading import Thread

import config.guardconfig as cfg
from dns_request_handler import DNSRequestHandler
from service.configservice import ConfigService


class Guard(object):
    def __init__(self):

        configService = ConfigService()
        configService.configure()

    @staticmethod
    def run():
        # start the monitor
        print('Start monitoring DNS queries')
        s = ThreadingUDPServer(('', cfg.guardConfig['GUARD_PORT']), DNSRequestHandler)
        thread = Thread(target=s.serve_forever)
        thread.daemon = True
        thread.start()

        # initialize LogManager
        try:
            while True:
                time.sleep(1)
                sys.stderr.flush()
                sys.stdout.flush()

        except KeyboardInterrupt:
            pass
        finally:
            s.shutdown()
