import json
import logging
import logging.config

import jsoncfg.jsoncfg as jsoncfg


CONFIG_FILES = {
    'CONFIG_A':'data/config.json',
    'LOGCONF1': 'data/logging1.json',
    'LOGCONF2': 'data/logging2.json'
}

logConf = CONFIG_FILES['LOGCONF1']


def main():
    pass

if __name__ == '__main__':
    logger = logging.getLogger()
    logger = logging.basicConfig(level="INFO")

    jsoncfg.dumpdata(logConf)
    with open(logConf, 'r', encoding="utf-8") as fd:
        logging.config.dictConfig(json.load(fd))

    main()