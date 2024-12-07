"""_summary_
File in charge of containing the boilerplate functions for checking if a given status corresponds to the expected response.
"""

from requests import Response


class QueryStatus:
    """_summary_
        This is the class in charge of checking if a response corresponds to a given status.
    """

    def __init__(self) -> None:
        pass

    def _get_status(self, response: Response) -> int:
        """_summary_
            This function is in charge of getting the status code from the response.
        Args:
            response (Response): _description_: The response from the server.
        Returns:
            int: _description_: The status code from the response.
        """
        return response.status_code

    # """ 1xx informational response"""

    def send_continue(self, response: Response) -> bool:
        """ send_continue: 100 """
        status = self._get_status(response)
        return status == 100

    def switching_protocols(self, response: Response) -> bool:
        """ switching_protocols: 101 """
        status = self._get_status(response)
        return status == 101

    def processing(self, response: Response) -> bool:
        """ processing: 102 """
        status = self._get_status(response)
        return status == 102

    def early_hints(self, response: Response) -> bool:
        """ early_hints: 103 """
        status = self._get_status(response)
        return status == 103

    def response_is_stale(self, response: Response) -> bool:
        """ response_is_stale: 110 """
        status = self._get_status(response)
        return status == 110

    # """success: 200"""

    def success(self, response: Response) -> bool:
        """ success: 200 """
        status = self._get_status(response)
        return status == 200

    def created(self, response: Response) -> bool:
        """ created: 201 """
        status = self._get_status(response)
        return status == 201

    def accepted(self, response: Response) -> bool:
        """ accepted: 202 """
        status = self._get_status(response)
        return status == 202

    def non_authoritative_information(self, response: Response) -> bool:
        """ non_authoritative_information: 203 """
        status = self._get_status(response)
        return status == 203

    def no_content(self, response: Response) -> bool:
        """ no_content: 204 """
        status = self._get_status(response)
        return status == 204

    def reset_content(self, response: Response) -> bool:
        """ reset_content: 205 """
        status = self._get_status(response)
        return status == 205

    def partial_content(self, response: Response) -> bool:
        """ partial_content: 206 """
        status = self._get_status(response)
        return status == 206

    def multi_status(self, response: Response) -> bool:
        """ multi_status: 207 """
        status = self._get_status(response)
        return status == 207

    def already_reported(self, response: Response) -> bool:
        """ already_reported: 208 """
        status = self._get_status(response)
        return status == 208

    def im_used(self, response: Response) -> bool:
        """ im_used: 226 """
        status = self._get_status(response)
        return status == 226

    """ 3xx redirection """

    def multiple_choices(self, response: Response) -> bool:
        """ multiple_choices: 300 """
        status = self._get_status(response)
        return status == 300

    def moved_permanently(self, response: Response) -> bool:
        """ moved_permanently: 301 """
        status = self._get_status(response)
        return status == 301

    def found(self, response: Response) -> bool:
        """ found: 302 """
        status = self._get_status(response)
        return status == 302

    def see_other(self, response: Response) -> bool:
        """ see_other: 303 """
        status = self._get_status(response)
        return status == 303

    def not_modified(self, response: Response) -> bool:
        """ not_modified: 304 """
        status = self._get_status(response)
        return status == 304

    def use_proxy(self, response: Response) -> bool:
        """ use_proxy: 305 """
        status = self._get_status(response)
        return status == 305

    def switch_proxy(self, response: Response) -> bool:
        """ switch_proxy: 306 """
        status = self._get_status(response)
        return status == 306

    def temporary_redirect(self, response: Response) -> bool:
        """ temporary_redirect: 307 """
        status = self._get_status(response)
        return status == 307

    def permanent_redirect(self, response: Response) -> bool:
        """ permanent_redirect: 308 """
        status = self._get_status(response)
        return status == 308

    """ 4xx client error """

    def bad_request(self, response: Response) -> bool:
        """ bad_request: 400 """
        status = self._get_status(response)
        return status == 400

    def unauthorized(self, response: Response) -> bool:
        """ unauthorized: 401 """
        status = self._get_status(response)
        return status == 401

    def payment_required(self, response: Response) -> bool:
        """ payment_required: 402 """
        status = self._get_status(response)
        return status == 402

    def forbidden(self, response: Response) -> bool:
        """ forbidden: 403 """
        status = self._get_status(response)
        return status == 403

    def not_found(self, response: Response) -> bool:
        """ not_found: 404 """
        status = self._get_status(response)
        return status == 404

    def method_not_allowed(self, response: Response) -> bool:
        """ method_not_allowed: 405 """
        status = self._get_status(response)
        return status == 405

    def not_acceptable(self, response: Response) -> bool:
        """ not_acceptable: 406 """
        status = self._get_status(response)
        return status == 406

    def proxy_authentication_required(self, response: Response) -> bool:
        """ proxy_authentication_required: 407 """
        status = self._get_status(response)
        return status == 407

    def request_timeout(self, response: Response) -> bool:
        """ request_timeout: 408 """
        status = self._get_status(response)
        return status == 408

    def conflict(self, response: Response) -> bool:
        """ conflict: 409 """
        status = self._get_status(response)
        return status == 409

    def gone(self, response: Response) -> bool:
        """ gone: 410 """
        status = self._get_status(response)
        return status == 410

    def length_required(self, response: Response) -> bool:
        """ length_required: 411 """
        status = self._get_status(response)
        return status == 411

    def precondition_failed(self, response: Response) -> bool:
        """ precondition_failed: 412 """
        status = self._get_status(response)
        return status == 412

    def payload_too_large(self, response: Response) -> bool:
        """ payload_too_large: 413 """
        status = self._get_status(response)
        return status == 413

    def uri_too_long(self, response: Response) -> bool:
        """ uri_too_long: 414 """
        status = self._get_status(response)
        return status == 414

    def unsupported_media_type(self, response: Response) -> bool:
        """ unsupported_media_type: 415 """
        status = self._get_status(response)
        return status == 415

    def range_not_satisfiable(self, response: Response) -> bool:
        """ range_not_satisfiable: 416 """
        status = self._get_status(response)
        return status == 416

    def expectation_failed(self, response: Response) -> bool:
        """ expectation_failed: 417 """
        status = self._get_status(response)
        return status == 417

    def im_a_teapot(self, response: Response) -> bool:
        """ im_a_teapot: 418 """
        status = self._get_status(response)
        return status == 418

    def page_expired(self, response: Response) -> bool:
        """ page_expired: 419 """
        status = self._get_status(response)
        return status == 419

    def enhance_your_calm(self, response: Response) -> bool:
        """ enhance_your_calm: 420 """
        status = self._get_status(response)
        return status == 420

    def misdirected_request(self, response: Response) -> bool:
        """ misdirected_request: 421 """
        status = self._get_status(response)
        return status == 421

    def unprocessable_entity(self, response: Response) -> bool:
        """ unprocessable_entity: 422 """
        status = self._get_status(response)
        return status == 422

    def locked(self, response: Response) -> bool:
        """ locked: 423 """
        status = self._get_status(response)
        return status == 423

    def failed_dependency(self, response: Response) -> bool:
        """ failed_dependency: 424 """
        status = self._get_status(response)
        return status == 424

    def too_early(self, response: Response) -> bool:
        """ too_early: 425 """
        status = self._get_status(response)
        return status == 425

    def upgrade_required(self, response: Response) -> bool:
        """ upgrade_required: 426 """
        status = self._get_status(response)
        return status == 426

    def precondition_required(self, response: Response) -> bool:
        """ precondition_required: 428 """
        status = self._get_status(response)
        return status == 428

    def too_many_requests(self, response: Response) -> bool:
        """ too_many_requests: 429 """
        status = self._get_status(response)
        return status == 429

    def request_header_fields_too_large(self, response: Response) -> bool:
        """ request_header_fields_too_large: 431 """
        status = self._get_status(response)
        return status == 431

    def unavailable_for_legal_reasons(self, response: Response) -> bool:
        """ unavailable_for_legal_reasons: 451 """
        status = self._get_status(response)
        return status == 451

    def invalid_token(self, response: Response) -> bool:
        """ invalid_token: 498 """
        status = self._get_status(response)
        return status == 498

    """ 5xx server error"""

    def internal_server_error(self, response: Response) -> bool:
        """ internal_server_error: 500 """
        status = self._get_status(response)
        return status == 500

    def not_implemented(self, response: Response) -> bool:
        """ not_implemented: 501 """
        status = self._get_status(response)
        return status == 501

    def bad_gateway(self, response: Response) -> bool:
        """ bad_gateway: 502 """
        status = self._get_status(response)
        return status == 502

    def service_unavailable(self, response: Response) -> bool:
        """ service_unavailable: 503 """
        status = self._get_status(response)
        return status == 503

    def gateway_timeout(self, response: Response) -> bool:
        """ gateway_timeout: 504 """
        status = self._get_status(response)
        return status == 504

    def http_version_not_supported(self, response: Response) -> bool:
        """ http_version_not_supported: 505 """
        status = self._get_status(response)
        return status == 505

    def variant_also_negotiates(self, response: Response) -> bool:
        """ variant_also_negotiates: 506 """
        status = self._get_status(response)
        return status == 506

    def insufficient_storage(self, response: Response) -> bool:
        """ insufficient_storage: 507 """
        status = self._get_status(response)
        return status == 507

    def loop_detected(self, response: Response) -> bool:
        """ loop_detected: 508 """
        status = self._get_status(response)
        return status == 508

    def bandwidth_limit_exceeded(self, response: Response) -> bool:
        """ bandwidth_limit_exceeded: 509 """
        status = self._get_status(response)
        return status == 509

    def not_extended(self, response: Response) -> bool:
        """ not_extended: 510 """
        status = self._get_status(response)
        return status == 510

    def network_authentication_required(self, response: Response) -> bool:
        """ network_authentication_required: 511 """
        status = self._get_status(response)
        return status == 511
