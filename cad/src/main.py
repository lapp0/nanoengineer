import argparse
import logging
import sys, os


def start_application(verbosity, data_dir, recursion_limit, dev_mode):
    logger = logging.getLogger('NE1_runner')
    logger.setLevel({
        0: logging.ERROR,
        1: logging.WARNING,
        2: logging.DEBUG,
    }[verbosity])

    logger.info('starting NanoEngineer')
    logger.info('using Python: {}'.format(sys.version))
    logger.info('using the data path: {}'.format(data_dir))

    logger.info('Setting recursion limit to {}'.format(recursion_limit))
    sys.setrecursionlimit(recursion_limit)


def run():
    # TODO: handle mmp file here? why can an mmp file be passed?
    # TODO: nosplash

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], default=1,
                        help='set log verbosity (higher is more verbose)')
    parser.add_argument("-d", "--data-dir", type=str, default=os.getcwd(),
                        help='path storing the data')
    parser.add_argument("-r", "--recursion-limit", type=int, default=5000,
                        help='specify the system recursion limit')
    parser.add_argument("-D", "--dev-mode", type=int,
                        help='enable devleoper mode features')
    args = parser.parse_args()
    start_application(args.verbosity, args.data_dir, args.recursion_limit, args.dev_mode)


if __name__ == '__main__':
    run()
