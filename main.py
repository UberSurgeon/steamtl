import argparse
import game_overlay_sdk
import game_overlay_sdk.injector
import threading
import logging
import trackertest
import shutdown_game
import regex
import time
import pyuac


logging.basicConfig(filename='test.log', level=logging.WARNING)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
overlay_log_handler = game_overlay_sdk.injector.OvelrayLogHandler()
formatter = logging.Formatter('%(levelname)s:%(message)s')
overlay_log_handler.setFormatter(formatter)
logger.addHandler(overlay_log_handler)


class MessageThread (threading.Thread):

    def __init__(self, game_task_name):
        super(MessageThread, self).__init__()
        self.need_quit = False
        self.game_task_name = game_task_name

    def run(self):
        while not self.need_quit:
            try:
                # logger.info(self.game_task_name)
                logger.info(trackertest.start_tracking())
            except Exception as e:
                logger.error(e)
                logger.warning("LEAVING IN 5 min")
                time.sleep(300)
                shutdown_game.shutdown_game(self.game_task_name)
                exit(0)


def clean_path(path):
    pattern = regex.compile(r'([^\\]+)(?=\.exe$)')
    return pattern.search(path).group(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--exe_path', type=str, help='exe path', required=True)
    parser.add_argument('--exe_args', type=str, help='exe args', default='')
    parser.add_argument('--steam_app_id', type=int,
                        help='for steam games please provide app_id',
                        required=False)
    args = parser.parse_args()
    print(args)

    game_overlay_sdk.injector.enable_monitor_logger()
    game_overlay_sdk.injector.run_process(
        args.exe_path, args.exe_args, args.steam_app_id)

    # start sending messages to overlay
    thread = MessageThread(clean_path(args.exe_path))
    thread.start()
    input("Press Enter to stop...")
    thread.need_quit = True
    thread.join()

    game_overlay_sdk.injector.release_resources()


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching with admin privileges...")
        pyuac.runAsAdmin()
    else:
        main()
