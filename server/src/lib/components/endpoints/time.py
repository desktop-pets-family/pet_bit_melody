#!/usr/bin/env python3
"""_summary_
    This file contains functions for the alarm endpoint
"""

from fastapi import FastAPI, Request
from ..http_codes import HCI
import json
import time
import winsound

class Time_endpoints:
    """_summary_
    """

    def __init__(self, url = "https://timeapi.io/api/time/current/zone?timeZone=Europe/Paris") -> None:
        """_summary_

        Args:
            debug (bool, optional): _description_. Defaults to False.
        """
        self.url = url

    async def get_time(self, request: Request):
        title = "get_time"
        try:
            response = request.get(self.url)
            response.raise_for_status()
            data = response.json()
            print(json.dumps(data, indent=4))
        except request.exceptions.RequestException as e:
            print(f"An error occured: {e}")
        return HCI.success({"msg": time})

    # async def set_alarm(time):
    #     time.sleep(time)
