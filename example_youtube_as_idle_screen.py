"""
Example code to show how you can start a YouTube movie
whenever the idle screen is shown.
"""
from __future__ import print_function
import time

import pychromecast

if __name__ == "__main__":
    cast = pychromecast.get_chromecast(strict=False)

    print(u"Monitoring {}".format(cast.device.friendly_name))

    while True:
        cast.refresh()

        if cast.app_id == pychromecast.APP_ID['HOME']:
            print("Hey, we are on the home screen :( Starting YouTube..")
            pychromecast.play_youtube_video("kxopViU98Xo", cast=cast)

        time.sleep(10)
