##
# EPITECH PROJECT, 2023
# Desktop_pet
# File description:
# http_codes.py
##

import json
from typing import Mapping, Union, Dict, Any
from fastapi import Response


class HttpCodes:
    """_summary_
    A class containing all the known http codes that can be used to reply to websites.
    These codes are:
    * The 1xx: Continue
    * The 2xx: Success
    * The 3xx: Redirection
    * The 4xx: Client error
    * The 5xx: Server error
    """

    def __init__(self) -> None:
        self.authorised_statuses = [
            100, 101, 102, 103, 110,
            200, 201, 202, 203, 204, 205,
            206, 207, 208, 226,
            300, 301, 302, 303, 304, 305,
            306, 307, 308,
            400, 401, 402, 403, 404, 405,
            406, 407, 408, 409, 410, 411,
            412, 413, 414, 415, 416, 417,
            418, 419, 420, 421, 422, 423,
            424, 425, 426, 428, 429, 430,
            431, 451, 498,
            500, 501, 502, 503, 504, 505,
            506, 507, 508, 509, 510, 511
        ]
        self.data_types = {
            'json': 'application/json',
            'html': 'text/html',
            'text': 'text/plain',
            'xml': 'application/xml',
            'css': 'text/css',
            'javascript': 'application/javascript',
            'js': 'application/javascript',
            'form': 'application/x-www-form-urlencoded',
            'form-data': 'multipart/form-data',
            'jpeg': 'image/jpeg',
            'jpg': 'image/jpeg',
            'png': 'image/png',
            'gif': 'image/gif',
            'bmp': 'image/bmp',
            'tiff': 'image/tiff',
            'webp': 'image/webp',
            'pdf': 'application/pdf',
            'zip': 'application/zip',
            'gzip': 'application/gzip',
            'octet-stream': 'application/octet-stream',
            'csv': 'text/csv',
            'plain': 'text/plain',
            'mp3': 'audio/mpeg',
            'mp4': 'video/mp4',
            'mpeg': 'video/mpeg',
            'avi': 'video/x-msvideo',
            'webm': 'video/webm',
            'ogg': 'application/ogg',
            'jsonld': 'application/ld+json',
            'markdown': 'text/markdown',
            'md': 'text/markdown',
            'rtf': 'application/rtf',
            'wav': 'audio/wav',
            'flac': 'audio/flac',
            'aac': 'audio/aac',
            'ogg-audio': 'audio/ogg',
            'opus': 'audio/opus',
            '3gp': 'video/3gpp',
            '3gpp': 'video/3gpp',
            '3g2': 'video/3gpp2',
            '3gpp2': 'video/3gpp2',
            'tar': 'application/x-tar',
            'ico': 'image/vnd.microsoft.icon',
            'svg': 'image/svg+xml',
            'txt': 'text/plain',
            'doc': 'application/msword',
            'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'xls': 'application/vnd.ms-excel',
            'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'ppt': 'application/vnd.ms-powerpoint',
            'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
            'eot': 'application/vnd.ms-fontobject',
            'otf': 'font/otf',
            'ttf': 'font/ttf',
            'woff': 'font/woff',
            'woff2': 'font/woff2'
        }

    # """ General basic success message that speaks on channel 200 by default """

    def _check_data_type(self, data_type: Union[str, None] = None) -> str:
        """_summary_
        Function in charge of checking the type provided by the user is one that can be used to send data.

        Args:
            data_type (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_: Returns the correct known version of the sent data.
        """
        if data_type is None:
            return "text/plain"

        data_type = data_type.lower()

        if data_type in self.data_types:
            return self.data_types[data_type]
        elif data_type in self.data_types.values():
            return data_type
        else:
            raise TypeError(f"Invalid data type: {data_type}")

    def _check_header(self, header: Union[Mapping[str, str], None] = None) -> Any:
        """_summary_
        Function in charge of checking the headers provided by the user.
        Args:
            header (Mapping[str, str], optional): _description_. Defaults to None.
        Returns:
            Any: _description_: Returns the correct known version of the sent headers.
        """
        if header is None:
            return {}
        elif isinstance(header, Dict):
            return header
        else:
            msg = "Invalid header format, the format you provided is: "
            msg += f"{type(header)}"
            raise TypeError(msg)

    def _process_data_content(self, data: Any, data_type: str) -> Any:
        """_summary_
        Function in charge of processing the data content to be sent.

        Args:
            data (Any): _description_: The data to be sent.
            data_type (str): _description_: The type of the data to be sent.

        Returns:
            Any: _description_: The processed data.
        """
        if data is None:
            return ""
        if data_type == self.data_types['json'] and isinstance(data, Dict):
            return json.dumps(data)
        return str(data)

    def send_message_on_status(self, status: int = 200, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """
        A generic function in charge of sending a message with a status.

        Args:
            status (int, optional): HTTP status code. Defaults to 200.
            content (Any, optional): The content to send. Defaults to None.
            content_type (str, optional): The type of the content. Defaults to "JSON".
            headers (Mapping[str, str], optional): The headers. Defaults to None.

        Returns:
            Response: FastAPI response object.
        """
        data_type = self._check_data_type(content_type)
        data_header = self._check_header(headers)
        data = self._process_data_content(content, data_type)

        if isinstance(status, str) and status.isnumeric():
            status = int(status)

        if status not in self.authorised_statuses:
            raise ValueError(
                f"Invalid status code, the code you entered is: {status}"
            )

        return Response(status_code=status, content=data, media_type=data_type, headers=data_header)

    # """ 1xx informational response"""

    def send_continue(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ send_continue: 100 """
        return self.send_message_on_status(status=100, content=content, content_type=content_type, headers=headers)

    def switching_protocols(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ switching_protocols: 101 """
        return self.send_message_on_status(status=101, content=content, content_type=content_type, headers=headers)

    def processing(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ processing: 102 """
        return self.send_message_on_status(status=102, content=content, content_type=content_type, headers=headers)

    def early_hints(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ early_hints: 103 """
        return self.send_message_on_status(status=103, content=content, content_type=content_type, headers=headers)

    def response_is_stale(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ response_is_stale: 110 """
        return self.send_message_on_status(status=110, content=content, content_type=content_type, headers=headers)

    # """success: 200"""

    def success(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ success: 200 """
        return self.send_message_on_status(status=200, content=content, content_type=content_type, headers=headers)

    def created(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ created: 201 """
        return self.send_message_on_status(status=201, content=content, content_type=content_type, headers=headers)

    def accepted(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ accepted: 202 """
        return self.send_message_on_status(status=202, content=content, content_type=content_type, headers=headers)

    def non_authoritative_information(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ non_authoritative_information: 203 """
        return self.send_message_on_status(status=203, content=content, content_type=content_type, headers=headers)

    def no_content(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ no_content: 204 """
        return self.send_message_on_status(status=204, content=content, content_type=content_type, headers=headers)

    def reset_content(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ reset_content: 205 """
        return self.send_message_on_status(status=205, content=content, content_type=content_type, headers=headers)

    def partial_content(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ partial_content: 206 """
        return self.send_message_on_status(status=206, content=content, content_type=content_type, headers=headers)

    def multi_status(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ multi_status: 207 """
        return self.send_message_on_status(status=207, content=content, content_type=content_type, headers=headers)

    def already_reported(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ already_reported: 208 """
        return self.send_message_on_status(status=208, content=content, content_type=content_type, headers=headers)

    def im_used(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ im_used: 226 """
        return self.send_message_on_status(status=226, content=content, content_type=content_type, headers=headers)

    """ 3xx redirection """

    def multiple_choices(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ multiple_choices: 300 """
        return self.send_message_on_status(status=300, content=content, content_type=content_type, headers=headers)

    def moved_permanently(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ moved_permanently: 301 """
        return self.send_message_on_status(status=301, content=content, content_type=content_type, headers=headers)

    def found(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ found: 302 """
        return self.send_message_on_status(status=302, content=content, content_type=content_type, headers=headers)

    def see_other(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ see_other: 303 """
        return self.send_message_on_status(status=303, content=content, content_type=content_type, headers=headers)

    def not_modified(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ not_modified: 304 """
        return self.send_message_on_status(status=304, content=content, content_type=content_type, headers=headers)

    def use_proxy(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ use_proxy: 305 """
        return self.send_message_on_status(status=305, content=content, content_type=content_type, headers=headers)

    def switch_proxy(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ switch_proxy: 306 """
        return self.send_message_on_status(status=306, content=content, content_type=content_type, headers=headers)

    def temporary_redirect(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ temporary_redirect: 307 """
        return self.send_message_on_status(status=307, content=content, content_type=content_type, headers=headers)

    def permanent_redirect(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ permanent_redirect: 308 """
        return self.send_message_on_status(status=308, content=content, content_type=content_type, headers=headers)

    """ 4xx client error """

    def bad_request(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ bad_request: 400 """
        return self.send_message_on_status(status=400, content=content, content_type=content_type, headers=headers)

    def unauthorized(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ unauthorized: 401 """
        return self.send_message_on_status(status=401, content=content, content_type=content_type, headers=headers)

    def payment_required(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ payment_required: 402 """
        return self.send_message_on_status(status=402, content=content, content_type=content_type, headers=headers)

    def forbidden(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ forbidden: 403 """
        return self.send_message_on_status(status=403, content=content, content_type=content_type, headers=headers)

    def not_found(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ not_found: 404 """
        return self.send_message_on_status(status=404, content=content, content_type=content_type, headers=headers)

    def method_not_allowed(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ method_not_allowed: 405 """
        return self.send_message_on_status(status=405, content=content, content_type=content_type, headers=headers)

    def not_acceptable(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ not_acceptable: 406 """
        return self.send_message_on_status(status=406, content=content, content_type=content_type, headers=headers)

    def proxy_authentication_required(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ proxy_authentication_required: 407 """
        return self.send_message_on_status(status=407, content=content, content_type=content_type, headers=headers)

    def request_timeout(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ request_timeout: 408 """
        return self.send_message_on_status(status=408, content=content, content_type=content_type, headers=headers)

    def conflict(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ conflict: 409 """
        return self.send_message_on_status(status=409, content=content, content_type=content_type, headers=headers)

    def gone(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ gone: 410 """
        return self.send_message_on_status(status=410, content=content, content_type=content_type, headers=headers)

    def length_required(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ length_required: 411 """
        return self.send_message_on_status(status=411, content=content, content_type=content_type, headers=headers)

    def precondition_failed(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ precondition_failed: 412 """
        return self.send_message_on_status(status=412, content=content, content_type=content_type, headers=headers)

    def payload_too_large(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ payload_too_large: 413 """
        return self.send_message_on_status(status=413, content=content, content_type=content_type, headers=headers)

    def uri_too_long(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ uri_too_long: 414 """
        return self.send_message_on_status(status=414, content=content, content_type=content_type, headers=headers)

    def unsupported_media_type(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ unsupported_media_type: 415 """
        return self.send_message_on_status(status=415, content=content, content_type=content_type, headers=headers)

    def range_not_satisfiable(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ range_not_satisfiable: 416 """
        return self.send_message_on_status(status=416, content=content, content_type=content_type, headers=headers)

    def expectation_failed(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ expectation_failed: 417 """
        return self.send_message_on_status(status=417, content=content, content_type=content_type, headers=headers)

    def im_a_teapot(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ im_a_teapot: 418 """
        return self.send_message_on_status(status=418, content=content, content_type=content_type, headers=headers)

    def page_expired(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ page_expired: 419 """
        return self.send_message_on_status(status=419, content=content, content_type=content_type, headers=headers)

    def enhance_your_calm(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ enhance_your_calm: 420 """
        return self.send_message_on_status(status=420, content=content, content_type=content_type, headers=headers)

    def misdirected_request(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ misdirected_request: 421 """
        return self.send_message_on_status(status=421, content=content, content_type=content_type, headers=headers)

    def unprocessable_entity(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ unprocessable_entity: 422 """
        return self.send_message_on_status(status=422, content=content, content_type=content_type, headers=headers)

    def locked(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ locked: 423 """
        return self.send_message_on_status(status=423, content=content, content_type=content_type, headers=headers)

    def failed_dependency(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ failed_dependency: 424 """
        return self.send_message_on_status(status=424, content=content, content_type=content_type, headers=headers)

    def too_early(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ too_early: 425 """
        return self.send_message_on_status(status=425, content=content, content_type=content_type, headers=headers)

    def upgrade_required(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ upgrade_required: 426 """
        return self.send_message_on_status(status=426, content=content, content_type=content_type, headers=headers)

    def precondition_required(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ precondition_required: 428 """
        return self.send_message_on_status(status=428, content=content, content_type=content_type, headers=headers)

    def too_many_requests(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ too_many_requests: 429 """
        return self.send_message_on_status(status=429, content=content, content_type=content_type, headers=headers)

    def request_header_fields_too_large(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ request_header_fields_too_large: 431 """
        return self.send_message_on_status(status=431, content=content, content_type=content_type, headers=headers)

    def unavailable_for_legal_reasons(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ unavailable_for_legal_reasons: 451 """
        return self.send_message_on_status(status=451, content=content, content_type=content_type, headers=headers)

    def invalid_token(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ invalid_token: 498 """
        return self.send_message_on_status(status=498, content=content, content_type=content_type, headers=headers)

    """ 5xx server error"""

    def internal_server_error(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ internal_server_error: 500 """
        return self.send_message_on_status(status=500, content=content, content_type=content_type, headers=headers)

    def not_implemented(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ not_implemented: 501 """
        return self.send_message_on_status(status=501, content=content, content_type=content_type, headers=headers)

    def bad_gateway(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ bad_gateway: 502 """
        return self.send_message_on_status(status=502, content=content, content_type=content_type, headers=headers)

    def service_unavailable(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ service_unavailable: 503 """
        return self.send_message_on_status(status=503, content=content, content_type=content_type, headers=headers)

    def gateway_timeout(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ gateway_timeout: 504 """
        return self.send_message_on_status(status=504, content=content, content_type=content_type, headers=headers)

    def http_version_not_supported(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ http_version_not_supported: 505 """
        return self.send_message_on_status(status=505, content=content, content_type=content_type, headers=headers)

    def variant_also_negotiates(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ variant_also_negotiates: 506 """
        return self.send_message_on_status(status=506, content=content, content_type=content_type, headers=headers)

    def insufficient_storage(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ insufficient_storage: 507 """
        return self.send_message_on_status(status=507, content=content, content_type=content_type, headers=headers)

    def loop_detected(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ loop_detected: 508 """
        return self.send_message_on_status(status=508, content=content, content_type=content_type, headers=headers)

    def bandwidth_limit_exceeded(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ bandwidth_limit_exceeded: 509 """
        return self.send_message_on_status(status=509, content=content, content_type=content_type, headers=headers)

    def not_extended(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ not_extended: 510 """
        return self.send_message_on_status(status=510, content=content, content_type=content_type, headers=headers)

    def network_authentication_required(self, content: Any = {'msg': 'message'}, content_type: str = "JSON", headers: Mapping[str, str] = None) -> Response:
        """ network_authentication_required: 511 """
        return self.send_message_on_status(status=511, content=content, content_type=content_type, headers=headers)


HCI = HttpCodes()
