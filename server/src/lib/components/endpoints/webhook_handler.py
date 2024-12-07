#!/usr/bin/env python3
"""_summary_
    File containing boilerplate functions that could be used by the server in it's endpoints_initialised for checking incoming data.
"""

from fastapi import FastAPI, Request
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME
import httpx
import logging
from .. import constants as CONST
from ..runtime_data import RuntimeData
from ..http_codes import HCI

app = FastAPI()

class Webhook:
    def __init__(self, runtime_data: RuntimeData) -> None:
        """_summary_

        Args:
            runtime_data (RuntimeData): _description_
        """
        data = []
        self.runtime_data_initialised: RuntimeData = runtime_data
        self.disp: Disp = Disp(
            TOML_CONF,
            SAVE_TO_FILE,
            FILE_NAME,
            FILE_DESCRIPTOR,
            debug=self.debug,
            logger=self.__class__.__name__
        )

    logging.basicConfig(level=logging.INFO)

    @app.post("/webhook") # put this in endpoints routes
    async def receive_webhook(self, request: Request):
        title = "get_applet"

        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request)
        self.disp.log_debug(f"Token = {token}", title)
        if token is None:
            return HCI.unauthorized({"error": "Authorisation required."})

        services_data = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_SERVICES)
        if services_data is None:
            return HCI.not_found({"error": "Services not found."}, content_type=CONST.CONTENT_TYPE, headers=self.runtime_data_initialised.json_header)

        payload = await request.json()

        logging.info(f"Received webhook data: {payload}")
        if not isinstance(payload, list):
            return {"error": "Expected an array of API requests"}

        print(f"payload: {payload}")

        async with httpx.AsyncClient(self) as client:
            for api_info in payload:
                try:
                    method = api_info.get("method", "GET").upper()
                    url = api_info.get("url")
                    data = api_info.get("data", {})

                    logging.info(f"Calling {method} {url} with data: {data}")

                    if method == "POST":
                        response = await client.post(url, json=data)
                    elif method == "PUT":
                        response = await client.put(url, json=data)
                    else:
                        response = await client.get(url)

                    self.data.append({
                        "url": url,
                        "status_code": response.status_code,
                        "response": response.json() if response.headers.get('content-type') == 'application/json' else response.text
                    })

                except Exception as e:
                    logging.error(f"Error calling API {api_info}: {e}")
                    self.data.append({
                        "url": api_info.get("url"),
                        "error": str(e)
                    })

        return {"message": "Webhook received", "data": payload}

    @app.get("/")
    async def test():
        return "test"

# test
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
