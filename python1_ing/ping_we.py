import multiprocessing
import re
import subprocess
import pprint
import logging
import time

fmt = "%(asctime)-15s %(levelname)s	%(module)s %(lineno)d %(message)s"
logging.basicConfig(format=fmt)
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

LOGGER.info(pprint.pformat(["start programu", "inny parametr"]))


def debug_print(*args, **kwargs):
    if __debug__:
        print(*args, ** kwargs)

    def pingHost(hostname):
        # time.sleep(10)
        try:
            assert bool(re.search("^[a-zA-Z._0-9-]+$", hostname))
        except AssertionError as e:
            print("asercja: %s %s" % (hostname, e))
            raise

        v = b''
        try:
            v = subprocess.check_output('ping.exe -n 1 {0}'.format(hostname), shell=True)

        except subprocess.CalledProcessError as e:
            import traceback
            import sys
            blad = sys.exc_info()
            debug_print(blad)
            LOGGER.debug("%s" % e)

            if LOGGER.isEnabledFor(logging.DEBUG):
                print("blad", e)
            # pprint.pprint(traceback.format_exception(*blad))
            return "fail - ping could not reach host %s" % hostname

        except BaseException as e:
            print("inny blad")
            print(locals())
        a = [x for x in v.decode(errors='ignore').splitlines()]
        a = hostname + ':' + '\n'.join([x.strip() for x in a if re.search('straty', x)])
        print(a)
        return a

    def run():
        hosty = ['localhot%', ''] + ['10.111.34.{0}'.format(i) for i in range(30, 42)]
        print(hosty)
        # wersja wieloprocesowa
        # p=multiprocessing.Pool(16)
        # v=p.map(pingHost,hosty)
        
        # wersja jednoprocesowa
        v = map(pingHost, hosty)
        print('output')
        print('\n'.join(v))

    if __name__ == '__main__':
        print("tryb debugowy?", __debug__)
        run()
