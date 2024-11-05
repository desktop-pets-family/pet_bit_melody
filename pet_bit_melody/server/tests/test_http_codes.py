"""_summary_
    File in charge of testing the http response codes.
"""
import os
import sys
from fastapi import Response

sys.path.append(os.getcwd())
try:
    from src import HCI
except ImportError as e:
    raise ImportError("Failed to import the src module") from e


def _get_status(data: Response) -> int:
    """_summary_
        Get the generated status from the boilerplate.

    Args:
        data (Response): _description_

    Returns:
        int: _description_
    """
    return data.status_code


def test_send_continue() -> None:
    """ send_continue: 100 """
    status = _get_status(HCI.send_continue())
    assert status == 100


def test_switching_protocols() -> None:
    """ switching_protocols: 101 """
    status = _get_status(HCI.switching_protocols())
    assert status == 101


def test_processing() -> None:
    """ processing: 102 """
    status = _get_status(HCI.processing())
    assert status == 102


def test_early_hints() -> None:
    """ early_hints: 103 """
    status = _get_status(HCI.early_hints())
    assert status == 103


def test_response_is_stale() -> None:
    """ response_is_stale: 110 """
    status = _get_status(HCI.response_is_stale())
    assert status == 110


def test_success() -> None:
    """ success: 200 """
    status = _get_status(HCI.success())
    assert status == 200


def test_created() -> None:
    """ created: 201 """
    status = _get_status(HCI.created())
    assert status == 201


def test_accepted() -> None:
    """ accepted: 202 """
    status = _get_status(HCI.accepted())
    assert status == 202


def test_non_authoritative_information() -> None:
    """ non_authoritative_information: 203 """
    status = _get_status(HCI.non_authoritative_information())
    assert status == 203


def test_no_content() -> None:
    """ no_content: 204 """
    status = _get_status(HCI.no_content())
    assert status == 204


def test_reset_content() -> None:
    """ reset_content: 205 """
    status = _get_status(HCI.reset_content())
    assert status == 205


def test_partial_content() -> None:
    """ partial_content: 206 """
    status = _get_status(HCI.partial_content())
    assert status == 206


def test_multi_status() -> None:
    """ multi_status: 207 """
    status = _get_status(HCI.multi_status())
    assert status == 207


def test_already_reported() -> None:
    """ already_reported: 208 """
    status = _get_status(HCI.already_reported())
    assert status == 208


def test_im_used() -> None:
    """ im_used: 226 """
    status = _get_status(HCI.im_used())
    assert status == 226


def test_multiple_choices() -> None:
    """ multiple_choices: 300 """
    status = _get_status(HCI.multiple_choices())
    assert status == 300


def test_moved_permanently() -> None:
    """ moved_permanently: 301 """
    status = _get_status(HCI.moved_permanently())
    assert status == 301


def test_found() -> None:
    """ found: 302 """
    status = _get_status(HCI.found())
    assert status == 302


def test_see_other() -> None:
    """ see_other: 303 """
    status = _get_status(HCI.see_other())
    assert status == 303


def test_not_modified() -> None:
    """ not_modified: 304 """
    status = _get_status(HCI.not_modified())
    assert status == 304


def test_use_proxy() -> None:
    """ use_proxy: 305 """
    status = _get_status(HCI.use_proxy())
    assert status == 305


def test_switch_proxy() -> None:
    """ switch_proxy: 306 """
    status = _get_status(HCI.switch_proxy())
    assert status == 306


def test_temporary_redirect() -> None:
    """ temporary_redirect: 307 """
    status = _get_status(HCI.temporary_redirect())
    assert status == 307


def test_permanent_redirect() -> None:
    """ permanent_redirect: 308 """
    status = _get_status(HCI.permanent_redirect())
    assert status == 308


def test_bad_request() -> None:
    """ bad_request: 400 """
    status = _get_status(HCI.bad_request())
    assert status == 400


def test_unauthorized() -> None:
    """ unauthorized: 401 """
    status = _get_status(HCI.unauthorized())
    assert status == 401


def test_payment_required() -> None:
    """ payment_required: 402 """
    status = _get_status(HCI.payment_required())
    assert status == 402


def test_forbidden() -> None:
    """ forbidden: 403 """
    status = _get_status(HCI.forbidden())
    assert status == 403


def test_not_found() -> None:
    """ not_found: 404 """
    status = _get_status(HCI.not_found())
    assert status == 404


def test_method_not_allowed() -> None:
    """ method_not_allowed: 405 """
    status = _get_status(HCI.method_not_allowed())
    assert status == 405


def test_not_acceptable() -> None:
    """ not_acceptable: 406 """
    status = _get_status(HCI.not_acceptable())
    assert status == 406


def test_proxy_authentication_required() -> None:
    """ proxy_authentication_required: 407 """
    status = _get_status(HCI.proxy_authentication_required())
    assert status == 407


def test_request_timeout() -> None:
    """ request_timeout: 408 """
    status = _get_status(HCI.request_timeout())
    assert status == 408


def test_conflict() -> None:
    """ conflict: 409 """
    status = _get_status(HCI.conflict())
    assert status == 409


def test_gone() -> None:
    """ gone: 410 """
    status = _get_status(HCI.gone())
    assert status == 410


def test_length_required() -> None:
    """ length_required: 411 """
    status = _get_status(HCI.length_required())
    assert status == 411


def test_precondition_failed() -> None:
    """ precondition_failed: 412 """
    status = _get_status(HCI.precondition_failed())
    assert status == 412


def test_payload_too_large() -> None:
    """ payload_too_large: 413 """
    status = _get_status(HCI.payload_too_large())
    assert status == 413


def test_uri_too_long() -> None:
    """ uri_too_long: 414 """
    status = _get_status(HCI.uri_too_long())
    assert status == 414


def test_unsupported_media_type() -> None:
    """ unsupported_media_type: 415 """
    status = _get_status(HCI.unsupported_media_type())
    assert status == 415


def test_range_not_satisfiable() -> None:
    """ range_not_satisfiable: 416 """
    status = _get_status(HCI.range_not_satisfiable())
    assert status == 416


def test_expectation_failed() -> None:
    """ expectation_failed: 417 """
    status = _get_status(HCI.expectation_failed())
    assert status == 417


def test_im_a_teapot() -> None:
    """ im_a_teapot: 418 """
    status = _get_status(HCI.im_a_teapot())
    assert status == 418


def test_page_expired() -> None:
    """ page_expired: 419 """
    status = _get_status(HCI.page_expired())
    assert status == 419


def test_enhance_your_calm() -> None:
    """ enhance_your_calm: 420 """
    status = _get_status(HCI.enhance_your_calm())
    assert status == 420


def test_misdirected_request() -> None:
    """ misdirected_request: 421 """
    status = _get_status(HCI.misdirected_request())
    assert status == 421


def test_unprocessable_entity() -> None:
    """ unprocessable_entity: 422 """
    status = _get_status(HCI.unprocessable_entity())
    assert status == 422


def test_locked() -> None:
    """ locked: 423 """
    status = _get_status(HCI.locked())
    assert status == 423


def test_failed_dependency() -> None:
    """ failed_dependency: 424 """
    status = _get_status(HCI.failed_dependency())
    assert status == 424


def test_too_early() -> None:
    """ too_early: 425 """
    status = _get_status(HCI.too_early())
    assert status == 425


def test_upgrade_required() -> None:
    """ upgrade_required: 426 """
    status = _get_status(HCI.upgrade_required())
    assert status == 426


def test_precondition_required() -> None:
    """ precondition_required: 428 """
    status = _get_status(HCI.precondition_required())
    assert status == 428


def test_too_many_requests() -> None:
    """ too_many_requests: 429 """
    status = _get_status(HCI.too_many_requests())
    assert status == 429


def test_request_header_fields_too_large() -> None:
    """ request_header_fields_too_large: 431 """
    status = _get_status(HCI.request_header_fields_too_large())
    assert status == 431


def test_unavailable_for_legal_reasons() -> None:
    """ unavailable_for_legal_reasons: 451 """
    status = _get_status(HCI.unavailable_for_legal_reasons())
    assert status == 451


def test_invalid_token() -> None:
    """ invalid_token: 498 """
    status = _get_status(HCI.invalid_token())
    assert status == 498


def test_internal_server_error() -> None:
    """ internal_server_error: 500 """
    status = _get_status(HCI.internal_server_error())
    assert status == 500


def test_not_implemented() -> None:
    """ not_implemented: 501 """
    status = _get_status(HCI.not_implemented())
    assert status == 501


def test_bad_gateway() -> None:
    """ bad_gateway: 502 """
    status = _get_status(HCI.bad_gateway())
    assert status == 502


def test_service_unavailable() -> None:
    """ service_unavailable: 503 """
    status = _get_status(HCI.service_unavailable())
    assert status == 503


def test_gateway_timeout() -> None:
    """ gateway_timeout: 504 """
    status = _get_status(HCI.gateway_timeout())
    assert status == 504


def test_http_version_not_supported() -> None:
    """ http_version_not_supported: 505 """
    status = _get_status(HCI.http_version_not_supported())
    assert status == 505


def test_variant_also_negotiates() -> None:
    """ variant_also_negotiates: 506 """
    status = _get_status(HCI.variant_also_negotiates())
    assert status == 506


def test_insufficient_storage() -> None:
    """ insufficient_storage: 507 """
    status = _get_status(HCI.insufficient_storage())
    assert status == 507


def test_loop_detected() -> None:
    """ loop_detected: 508 """
    status = _get_status(HCI.loop_detected())
    assert status == 508


def test_bandwidth_limit_exceeded() -> None:
    """ bandwidth_limit_exceeded: 509 """
    status = _get_status(HCI.bandwidth_limit_exceeded())
    assert status == 509


def test_not_extended() -> None:
    """ not_extended: 510 """
    status = _get_status(HCI.not_extended())
    assert status == 510


def test_network_authentication_required() -> None:
    """ network_authentication_required: 511 """
    status = _get_status(HCI.network_authentication_required())
    assert status == 511
