import logging

logging.basicConfig(filename='example_2.log',
                    level=logging.DEBUG)


def log():

    logging.debug('Example Debug')
    logging.info('Example Info')
    logging.warning('Example Warning')
    logging.error('Example Error')
    logging.critical('Example Critical or Fatal')


if __name__ == '__main__':
    log()
