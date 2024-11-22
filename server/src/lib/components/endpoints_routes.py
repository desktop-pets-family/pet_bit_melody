"""_summary_
    This is the file in charge of storing the endpoints_initialised ready to be imported into the server class.
"""
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME
from .runtime_data import RuntimeData
from .password_handling import PasswordHandling
from .endpoints import Bonus, UserEndpoints, Services, Mandatory, Applets


class Endpoints:
    """_summary_
    """

    def __init__(self, runtime_data: RuntimeData, success: int = 0, error: int = 84, debug: bool = False) -> None:
        """_summary_

        Args:
            runtime_data (RuntimeData): _description_
            success (int, optional): _description_. Defaults to 0.
            error (int, optional): _description_. Defaults to 84.
            debug (bool, optional): _description_. Defaults to False.
        """
        self.debug: bool = debug
        self.success: int = success
        self.error: int = error
        self.runtime_data_initialised: RuntimeData = runtime_data
        self.password_handling_initialised: PasswordHandling = PasswordHandling(
            self.error,
            self.success,
            self.debug
        )
        self.disp: Disp = Disp(
            TOML_CONF,
            SAVE_TO_FILE,
            FILE_NAME,
            FILE_DESCRIPTOR,
            debug=self.debug,
            logger=self.__class__.__name__
        )
        # ------------------- Initialize endpoints sub-classes ------------------
        self.bonus: Bonus = Bonus(
            runtime_data=runtime_data,
            success=success,
            error=error,
            debug=debug
        )
        self.services: Services = Services(
            runtime_data=self.runtime_data_initialised,
            success=self.success,
            error=self.error,
            debug=self.debug
        )
        self.user_endpoints: UserEndpoints = UserEndpoints(
            runtime_data=runtime_data,
            success=success,
            error=error,
            debug=debug
        )
        self.mandatory: Mandatory = Mandatory(
            runtime_data=runtime_data,
            success=success,
            error=error,
            debug=debug
        )
        self.applets: Applets = Applets(
            runtime_data=runtime_data,
            success=success,
            error=error,
            debug=debug
        )

    def inject_routes(self) -> None:
        """_summary_
        """
        # Bonus routes
        self.runtime_data_initialised.paths_initialised.add_path(
            "", self.bonus.get_welcome, [
                "GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"
            ]
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/", self.bonus.get_welcome, [
                "GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"
            ]
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/", self.bonus.get_welcome, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/bucket_names", self.bonus.get_s3_bucket_names, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/get_table", self.bonus.get_table, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/stop", self.bonus.post_stop_server, "PUT"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/trigger_action/{id}", self.bonus.trigger_endpoint, "GET"
        )

        # Services routes
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/services", self.services.get_services, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/service/name/{name}", self.services.get_service_name, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/service/{id}", self.services.get_service_id, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/services/{tags}", self.services.get_services_by_tag, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/recent_services", self.services.get_recent_services, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/service/{name}", self.services.create_service, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/service/{service_id}", self.services.update_service, "PUT"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/service/{service_id}", self.services.patch_service, "PATCH"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/service_id/name/{name}", self.services.get_service_id_by_name, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/service/{service_id}", self.services.delete_service, "DELETE"
        )

        # Authentication routes
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/login", self.user_endpoints.post_login, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/register", self.user_endpoints.post_register, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/send_email_verification", self.user_endpoints.post_send_email_verification, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/reset_password", self.user_endpoints.put_reset_password, "PATCH"
        )

        # Oauth routes
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/oauth/login", self.runtime_data_initialised.oauth_authentication_initialised.oauth_login, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/oauth/callback", self.runtime_data_initialised.oauth_authentication_initialised.oauth_callback, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/oauth/{provider}", self.runtime_data_initialised.oauth_authentication_initialised.add_oauth_provider, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/oauth/{provider}", self.runtime_data_initialised.oauth_authentication_initialised.update_oauth_provider_data, "PUT"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/oauth/{provider}", self.runtime_data_initialised.oauth_authentication_initialised.patch_oauth_provider_data, "PATCH"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/oauth/{provider}", self.runtime_data_initialised.oauth_authentication_initialised.delete_oauth_provider, "DELETE"
        )

        # Users routes
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/user", self.user_endpoints.patch_user, "PATCH"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/user", self.user_endpoints.put_user, "PUT"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/user", self.user_endpoints.get_user, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/user", self.user_endpoints.delete_user, "DELETE"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/user_favicon", self.user_endpoints.put_user_favicon, "PUT"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/user_favicon", self.user_endpoints.delete_user_favicon, "DELETE"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/logout", self.user_endpoints.post_logout, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/user_id", self.user_endpoints.get_user_id, "GET"
        )
        
        # Applets routes
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/applet", self.applets.create_applet, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/applet/{id}", self.applets.put_applet_by_id, "PUT"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/applet/{id}", self.applets.get_applet_by_id, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/applet/{id}", self.applets.delete_applet_by_id, "DELETE"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/applets", self.applets.get_all_applets, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/user_applets", self.applets.get_user_applets, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/applets/{tags}", self.applets.get_applets_by_tags, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/recent_applets", self.applets.get_recent_applets, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/connect_applets/{id}", self.applets.post_connect_applet, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/disconnect_applets/{id}", self.applets.delete_disconnect_applet, "DELETE"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/triggers/{service_name}", self.applets.get_triggers_by_service_name, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            "/api/v1/reactions/{service_name}", self.applets.get_reactions_by_service_name, "GET"
        )

        # Mandatory routes
        self.runtime_data_initialised.paths_initialised.add_path(
            "/about.json", self.mandatory.get_about, "GET"
        )
