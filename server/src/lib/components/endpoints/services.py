"""
This file contains every method about services
"""

from typing import Any, List
from fastapi import Response, Request
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME
from .. import constants as CONST
from ..runtime_data import RuntimeData
from ..http_codes import HCI


class Services:
    """
    The class that contains every method about services
    """

    def __init__(self, runtime_data: RuntimeData, success: int = 0, error: int = 84, debug: bool = False) -> None:
        """_summary_
        The constructor of the services class
        """
        self.debug: bool = debug
        self.success: int = success
        self.error: int = error
        self.runtime_data_initialised: RuntimeData = runtime_data
        self.disp: Disp = Disp(
            TOML_CONF,
            SAVE_TO_FILE,
            FILE_NAME,
            FILE_DESCRIPTOR,
            debug=self.debug,
            logger=self.__class__.__name__
        )

    async def get_services(self, request: Request) -> Response:
        """
        The method to get every services contained in the db
        """
        title = "get_services"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        self.disp.log_debug(f"Token = {token}", title)
        if not token:
            return self.runtime_data_initialised.boilerplate_responses_initialised.unauthorized(
                title,
                token
            )
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_correct(
            token
        ) is False:
            return self.runtime_data_initialised.boilerplate_responses_initialised.invalid_token(
                title
            )
        services_data = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_SERVICES,
            "*"
        )
        if not services_data or isinstance(services_data, int):
            body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
                title=title,
                message="services not found.",
                resp="not found",
                token=token,
                error=True
            )
            return HCI.not_found(
                content=body,
                content_type=CONST.CONTENT_TYPE,
                headers=self.runtime_data_initialised.json_header
            )
        self.disp.log_debug(f"Retrieved data {services_data}", title)
        for i, service in enumerate(services_data):
            if "api_key" in service:
                services_data[i]["api_key"] = self.runtime_data_initialised.boilerplate_non_http_initialised.hide_api_key(
                    service["api_key"]
                )
            services_data[i]["created_at"] = self.runtime_data_initialised.database_link.datetime_to_string(
                service["created_at"])
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message=services_data,
            resp="success",
            token=token
        )
        return HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    async def get_service_name(self, request: Request, name: str) -> Response:
        """
        The method to get a service by it's name
        """
        title = "Get service by name"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        self.disp.log_debug(f"Token = {token}", title)
        if not token:
            return self.runtime_data_initialised.boilerplate_responses_initialised.unauthorized(
                title,
                token
            )
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_correct(
            token
        ) is False:
            return self.runtime_data_initialised.boilerplate_responses_initialised.invalid_token(
                title
            )
        service_data = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_SERVICES,
            "*",
            f"name='{name}'"
        )
        if not service_data or isinstance(service_data, int):
            body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
                title=title,
                message="service not found.",
                resp="not found",
                token=token,
                error=True
            )
            return HCI.not_found(
                content=body,
                content_type=CONST.CONTENT_TYPE,
                headers=self.runtime_data_initialised.json_header
            )
        for i, service in enumerate(service_data):
            if "api_key" in service:
                service_data[i]["api_key"] = self.runtime_data_initialised.boilerplate_non_http_initialised.hide_api_key(
                    service["api_key"]
                )
            service_data[i]["created_at"] = self.runtime_data_initialised.database_link.datetime_to_string(
                service["created_at"])
        self.disp.log_debug(f"Service found: {service_data}", title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message=service_data,
            resp="success",
            token=token
        )
        return HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    async def get_service_id(self, request: Request, id: str) -> Response:
        """
        The method to get a service by it's id
        """
        title = "Get service by id"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        self.disp.log_debug(f"Token = {token}", title)
        if not token:
            return self.runtime_data_initialised.boilerplate_responses_initialised.unauthorized(
                title,
                token
            )
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_correct(
            token
        ) is False:
            return self.runtime_data_initialised.boilerplate_responses_initialised.invalid_token(
                title
            )
        service_data = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_SERVICES,
            "*",
            f"id='{id}'",
            beautify=True
        )
        if isinstance(service_data, int):
            return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(
                title,
                token
            )
        for i, service in enumerate(service_data):
            if "api_key" in service:
                service_data[i]["api_key"] = self.runtime_data_initialised.boilerplate_non_http_initialised.hide_api_key(
                    service["api_key"]
                )
            service_data[i]["created_at"] = self.runtime_data_initialised.database_link.datetime_to_string(
                service["created_at"]
            )
        if len(service_data) == 1:
            service_data = service_data[0]
        self.disp.log_debug(f"Service found: {service_data}", title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message=service_data,
            resp="success",
            token=token
        )
        return HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    async def get_services_by_tag(self, request: Request, tags: str) -> Response:
        """
        The function to get and filter every services by specifics tag
        """
        title = "get_services_by_tag"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        self.disp.log_debug(f"Token = {token}", title)
        if not token:
            return self.runtime_data_initialised.boilerplate_responses_initialised.unauthorized(
                title,
                token
            )
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_correct(
            token
        ) is False:
            return self.runtime_data_initialised.boilerplate_responses_initialised.invalid_token(
                title
            )
        if not tags or tags == "":
            return self.runtime_data_initialised.boilerplate_responses_initialised.bad_request(
                title,
                token
            )
        tags_list = tags.split(":")
        services_data = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_SERVICES,
            "*"
        )
        filtered_services: list[dict] = []
        for i, service in enumerate(services_data):
            if "api_key" in service:
                service[i]["api_key"] = self.runtime_data_initialised.boilerplate_non_http_initialised.hide_api_key(
                    service["api_key"]
                )
            for _, element in enumerate(tags_list):
                if element in service["tags"]:
                    filtered_services.append(service)
        if not filtered_services:
            body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
                title=title,
                message=f"No services found with the given tags '{tags}'.",
                resp="not found",
                token=token,
                error=True
            )
            return HCI.not_found(
                content=body,
                content_type=CONST.CONTENT_TYPE,
                headers=self.runtime_data_initialised.json_header
            )
        for i, service in enumerate(filtered_services):
            filtered_services[i]["created_at"] = self.runtime_data_initialised.database_link.datetime_to_string(
                service["created_at"])
        msg = f"Services with guven tags '{tags}': "
        msg += f"{filtered_services}"
        self.disp.log_debug(msg, title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message=filtered_services,
            resp="success",
            token=token
        )
        return HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    async def get_recent_services(self, request: Request) -> Response:
        """
        The function to get and filter every services by the most recent to the oldest
        """
        title = "get_recent_services"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        self.disp.log_debug(f"Token = {token}", title)
        if not token:
            return self.runtime_data_initialised.boilerplate_responses_initialised.unauthorized(
                title,
                token
            )
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_correct(
            token
        ) is False:
            return self.runtime_data_initialised.boilerplate_responses_initialised.invalid_token(
                title
            )
        service_data = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_SERVICES,
            "*"
        )
        recent_services = sorted(
            service_data, key=lambda x: x["created_at"], reverse=True
        )[:10]
        if not recent_services:
            body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
                title=title,
                message="No recent services found.",
                resp="not found",
                token=token,
                error=True
            )
            return HCI.not_found(
                content=body,
                content_type=CONST.CONTENT_TYPE,
                headers=self.runtime_data_initialised.json_header
            )
        for i, service in enumerate(recent_services):
            if "api_key" in service:
                service_data[i]["api_key"] = self.runtime_data_initialised.boilerplate_non_http_initialised.hide_api_key(
                    service["api_key"]
                )
            recent_services[i]["created_at"] = self.runtime_data_initialised.database_link.datetime_to_string(
                service["created_at"])
        self.disp.log_debug(f"Recent services: {recent_services}", title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message=recent_services,
            resp="success",
            token=token
        )
        return HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    async def get_service_id_by_name(self, request: Request, name: str) -> Response:
        """
        The function to get a service id by the name
        """
        title = "get_service_id_by_name"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        self.disp.log_debug(f"Token = {token}", title)
        if not token:
            return self.runtime_data_initialised.boilerplate_responses_initialised.unauthorized(
                title,
                token
            )
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_correct(
            token
        ) is False:
            return self.runtime_data_initialised.boilerplate_responses_initialised.invalid_token(
                title
            )
        retrieved_id = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_SERVICES,
            "id",
            f"name='{name}'"
        )
        if isinstance(retrieved_id, int):
            return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(
                title,
                token
            )
        service_id = str(retrieved_id[0]["id"])
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message=service_id,
            resp="success",
            token=token
        )
        return HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    async def create_service(self, request: Request, name: str) -> Response:
        """
        Create a new service (Only for admin account)
        """
        title: str = "create_service"
        token: str = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        if not token:
            return self.runtime_data_initialised.boilerplate_responses_initialised.unauthorized(
                title,
                token
            )
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_admin(
            token
        ) is False:
            return self.runtime_data_initialised.boilerplate_responses_initialised.unauthorized(title, token)
        if not name:
            return self.runtime_data_initialised.boilerplate_responses_initialised.bad_request(
                title,
                token
            )
        self.disp.log_debug(f"Service name: {name}", title)
        response = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_SERVICES,
            "*",
            f"name='{name}'"
        )
        if isinstance(response, int) is False:
            return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(
                title,
                token
            )
        request_body = await self.runtime_data_initialised.boilerplate_incoming_initialised.get_body(request)
        if not request_body or not all(key in request_body for key in ("url", "api_key", "category", "type", "tags", "colour", "description")):
            return self.runtime_data_initialised.boilerplate_responses_initialised.bad_request(
                title,
                token
            )
        self.disp.log_debug(f"Request body: {request_body}", title)
        data: list = [
            name,
            request_body["url"],
            request_body["api_key"],
            request_body["category"],
            str(0),
            request_body["type"],
            request_body["tags"],
            "NOW()",
            str(int(False)),
            request_body["colour"],
            request_body["description"]
        ]
        self.disp.log_debug(f"Generated data: {data}", title)
        columns: List[Any] = self.runtime_data_initialised.database_link.get_table_column_names(
            CONST.TAB_SERVICES)
        if isinstance(columns, int):
            return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(
                title,
                token
            )
        columns.pop(0)
        self.disp.log_debug(f"Columns: {columns}", title)
        if self.runtime_data_initialised.database_link.insert_data_into_table(CONST.TAB_SERVICES, data, columns) == self.error:
            return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(
                title,
                token
            )
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message="The new service is created successfully.",
            resp="success",
            token=token
        )
        return HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    async def update_service(self, request: Request, service_id: str) -> Response:
        """
        Update a service data (Only for admin account)
        """
        title: str = "update_service"
        token: str = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        if not token:
            return self.runtime_data_initialised.boilerplate_responses_initialised.unauthorized(
                title,
                token
            )
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_admin(
            token
        ) is False:
            return self.runtime_data_initialised.boilerplate_responses_initialised.unauthorized(title, token)
        if not service_id:
            return self.runtime_data_initialised.boilerplate_responses_initialised.bad_request(
                title,
                token
            )
        self.disp.log_debug(f"Service id: {service_id}", title)
        if isinstance(self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_SERVICES,
            "*",
            f"id='{service_id}'"
        ), int):
            msg = f"Failed to retrieve data from '{CONST.TAB_SERVICES}'"
            msg += " table."
            self.disp.log_error(msg, title)
            return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(
                title,
                token
            )
        request_body = await self.runtime_data_initialised.boilerplate_incoming_initialised.get_body(
            request
        )
        if not request_body or not all(key in request_body for key in ("name", "url", "api_key", "category", "tags", "colour", "description")):
            return self.runtime_data_initialised.boilerplate_responses_initialised.bad_request(
                title,
                token
            )
        self.disp.log_debug(f"Request body: {request_body}", title)
        data: list = [
            request_body["name"],
            request_body["url"],
            request_body["api_key"],
            request_body["category"],
            request_body["tags"],
            request_body["colour"],
            request_body["description"]
        ]
        self.disp.log_debug(f"Generated data: {data}", title)
        columns: list = self.runtime_data_initialised.database_link.get_table_column_names(
            CONST.TAB_SERVICES
        )
        if isinstance(columns, int):
            msg = "Failed to retrieve columns from "
            msg += f"'{CONST.TAB_SERVICES}' table."
            self.disp.log_error(msg, title)
            return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(
                title,
                token
            )
        columns.pop(0)
        columns.pop(4)
        columns.pop(4)
        columns.pop(5)
        columns.pop(5)
        self.disp.log_debug(f"Columns: {columns}", title)
        if self.runtime_data_initialised.database_link.update_data_in_table(
            CONST.TAB_SERVICES,
            data,
            columns,
            f"id='{service_id}'"
        ) == self.error:
            msg = f"Failed to update data in '{CONST.TAB_SERVICES}"
            msg += "' table."
            self.disp.log_error(msg, title)
            return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(
                title,
                token
            )
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message="The service is updated successfully.",
            resp="success",
            token=token
        )
        return HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    async def patch_service(self, request: Request, service_id: str) -> Response:
        """
        Update a service value (Only for admin account)
        """
        title: str = "update_service"
        token: str = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        if not token:
            return self.runtime_data_initialised.boilerplate_responses_initialised.unauthorized(
                title,
                token
            )
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_admin(
            token
        ) is False:
            return self.runtime_data_initialised.boilerplate_responses_initialised.unauthorized(title, token)
        if not service_id:
            return self.runtime_data_initialised.boilerplate_responses_initialised.bad_request(
                title,
                token
            )
        self.disp.log_debug(f"Service id: {service_id}", title)
        if isinstance(self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_SERVICES,
            "*",
            f"id='{service_id}'"
        ), int):
            msg = f"Failed to retrieve data from '{CONST.TAB_SERVICES}'"
            msg += "table."
            self.disp.log_error(msg, title)
            return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(
                title,
                token
            )
        request_body = await self.runtime_data_initialised.boilerplate_incoming_initialised.get_body(
            request
        )
        if not request_body:
            return self.runtime_data_initialised.boilerplate_responses_initialised.bad_request(
                title,
                token
            )
        self.disp.log_debug(f"Request body: {request_body}", title)
        if "name" in request_body:
            if self.runtime_data_initialised.boilerplate_non_http_initialised.update_single_data(
                CONST.TAB_SERVICES,
                "id",
                "name",
                service_id,
                request_body
            ) == self.error:
                return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(title, token)
        if "url" in request_body:
            if self.runtime_data_initialised.boilerplate_non_http_initialised.update_single_data(
                CONST.TAB_SERVICES,
                "id",
                "url",
                service_id,
                request_body
            ) == self.error:
                return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(title, token)
        if "api_key" in request_body:
            if self.runtime_data_initialised.boilerplate_non_http_initialised.update_single_data(
                CONST.TAB_SERVICES,
                "id",
                "api_key",
                service_id,
                request_body
            ) == self.error:
                return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(title, token)
        if "category" in request_body:
            if self.runtime_data_initialised.boilerplate_non_http_initialised.update_single_data(
                CONST.TAB_SERVICES,
                "id",
                "category",
                service_id,
                request_body
            ) == self.error:
                return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(title, token)
        if "tags" in request_body:
            if self.runtime_data_initialised.boilerplate_non_http_initialised.update_single_data(
                CONST.TAB_SERVICES,
                "id",
                "tags",
                service_id,
                request_body
            ) == self.error:
                return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(title, token)
        if "colour" in request_body:
            if self.runtime_data_initialised.boilerplate_non_http_initialised.update_single_data(
                CONST.TAB_SERVICES,
                "id",
                "colour",
                service_id,
                request_body
            ) == self.error:
                return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(title, token)
        if "description" in request_body:
            if self.runtime_data_initialised.boilerplate_non_http_initialised.update_single_data(
                CONST.TAB_SERVICES,
                "id",
                "description",
                service_id,
                request_body
            ) == self.error:
                return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(title, token)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message="The service value is updated successfully.",
            resp="success",
            token=token
        )
        return HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    async def delete_service(self, request: Request, service_id: str) -> Response:
        """
        The function to delete a service from the database
        """
        title: str = "delete_oauth_provider"
        if not service_id:
            return self.runtime_data_initialised.boilerplate_responses_initialised.provider_not_given(
                title,
                None
            )
        self.disp.log_debug(f"Service id: {service_id}", title)
        token: str = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        self.disp.log_debug(f"Token gotten: {token}", title)
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_correct(token) is False:
            self.disp.log_error("You're not admin.", title)
            return self.runtime_data_initialised.boilerplate_responses_initialised.insuffisant_rights(
                title,
                token
            )
        retrived_data = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_SERVICES,
            "*",
            f"id='{service_id}'"
        )
        if isinstance(retrived_data, int):
            return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(
                title,
                token
            )
        provider_name = retrived_data[0]["name"]
        # Add a code to delete every users actions with this service
        # Add a code to delete every applets with this service
        if retrived_data[0]["oauth"] == 1:
            if self.runtime_data_initialised.database_link.drop_data_from_table(
                CONST.TAB_ACTIVE_OAUTHS,
                f"service_id='{service_id}'"
            ) == self.error:
                return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(
                    title,
                    token
                )
            if self.runtime_data_initialised.database_link.drop_data_from_table(
                CONST.TAB_USER_OAUTH_CONNECTION,
                f"provider_name='{provider_name}'"
            ) == self.error:
                return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(
                    title,
                    token
                )
        if self.runtime_data_initialised.database_link.drop_data_from_table(
            CONST.TAB_SERVICES,
            f"id='{service_id}'"
        ) == self.error:
            return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(
                title,
                token
            )
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message="The service has been deleted successfully.",
            resp="success",
            token=token,
        )
        return HCI.success(
            body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )
