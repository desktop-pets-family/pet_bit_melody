"""_summary_
    This is the file in charge of storing the endpoints_initialised ready to be imported into the server class.
"""
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME
from .runtime_data import RuntimeData
from .password_handling import PasswordHandling
from .endpoints import Bonus, UserEndpoints, Applets, Project, Edit


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
        # ------------------------------ Base url ------------------------------
        self.api_base: str = "/api/v1/"
        # ------------------ Initialize endpoints sub-classes  -----------------
        self.bonus: Bonus = Bonus(
            runtime_data=runtime_data,
            success=success,
            error=error,
            debug=debug
        )
        self.user_endpoints: UserEndpoints = UserEndpoints(
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
        self.project: Project = Project(
            runtime_data=runtime_data,
            success=success,
            error=error,
            debug=debug
        )
        self.edit: Edit = Edit(
            runtime_data=runtime_data,
            success=success,
            error=error,
            debug=debug
        )

    def inject_routes(self) -> None:
        """_summary_
        """
        # Home route
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
            f"{self.api_base}/", self.bonus.get_welcome, "GET"
        )

        # Manage the server stop
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/stop", self.bonus.post_stop_server, "PUT"
        )

        # Endpoints regarding project management
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/project/new", self.project.post_project_new, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/project/reset", self.project.post_project_reset, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/project/play", self.project.post_project_play, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/project/save", self.project.post_project_save, "PUT"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/project/stop", self.project.post_project_stop, "PUT"
        )

        # Audio generation (For playing)
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/generate_audio", self.applets.post_generate_audio, "POST"
        )

        # Project edition
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/edit/instruments", self.edit.get_edit_instruments, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/edit/instrument_range", self.edit.get_edit_instruments_range, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/edit/undo", self.edit.put_edit_undo, "PUT"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/edit/redo", self.edit.put_edit_redo, "PUT"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/edit/repeat", self.edit.put_edit_repeat, "PUT"
        )

        # Authentication routes
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/account/login", self.user_endpoints.post_login, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/account/register", self.user_endpoints.post_register, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/account/send_email_verification", self.user_endpoints.post_send_email_verification, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/account/reset_password", self.user_endpoints.put_reset_password, "PATCH"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/account/logout", self.user_endpoints.post_logout, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/account/settings", self.user_endpoints.get_account_settings, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/account/settings", self.user_endpoints.put_account_settings, "PUT"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/account/settings", self.user_endpoints.patch_account_settings, "PATCH"
        )

        # Oauth routes
        # self.runtime_data_initialised.paths_initialised.add_path(
        #     f"{self.api_base}/oauth/login", self.runtime_data_initialised.oauth_authentication_initialised.oauth_login, "POST"
        # )
        # self.runtime_data_initialised.paths_initialised.add_path(
        #     f"{self.api_base}/oauth/callback", self.runtime_data_initialised.oauth_authentication_initialised.oauth_callback, "POST"
        # )
        # self.runtime_data_initialised.paths_initialised.add_path(
        #     f"{self.api_base}/oauth/{provider}", self.runtime_data_initialised.oauth_authentication_initialised.add_oauth_provider, "POST"
        # )
        # self.runtime_data_initialised.paths_initialised.add_path(
        #     f"{self.api_base}/oauth/{provider}", self.runtime_data_initialised.oauth_authentication_initialised.update_oauth_provider_data, "PUT"
        # )
        # self.runtime_data_initialised.paths_initialised.add_path(
        #     f"{self.api_base}/oauth/{provider}", self.runtime_data_initialised.oauth_authentication_initialised.patch_oauth_provider_data, "PATCH"
        # )
        # self.runtime_data_initialised.paths_initialised.add_path(
        #     f"{self.api_base}/oauth/{provider}", self.runtime_data_initialised.oauth_authentication_initialised.delete_oauth_provider, "DELETE"
        # )

        # Users routes
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/user", self.user_endpoints.patch_user, "PATCH"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/user", self.user_endpoints.put_user, "PUT"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/user", self.user_endpoints.get_user, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/user", self.user_endpoints.delete_user, "DELETE"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/user_favicon", self.user_endpoints.put_user_favicon, "PUT"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/user_favicon", self.user_endpoints.delete_user_favicon, "DELETE"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/logout", self.user_endpoints.post_logout, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/user_id", self.user_endpoints.get_user_id, "GET"
        )

        # Applets routes
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/applet", self.applets.create_applet, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/applet/{id}", self.applets.put_applet_by_id, "PUT"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/applet/{id}", self.applets.get_applet_by_id, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/applet/{id}", self.applets.delete_applet_by_id, "DELETE"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/applets", self.applets.get_all_applets, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/user_applets", self.applets.get_user_applets, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/applets/{tags}", self.applets.get_applets_by_tags, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/recent_applets", self.applets.get_recent_applets, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/connect_applets/{id}", self.applets.post_connect_applet, "POST"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/disconnect_applets/{id}", self.applets.delete_disconnect_applet, "DELETE"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/triggers/{service_name}", self.applets.get_triggers_by_service_name, "GET"
        )
        self.runtime_data_initialised.paths_initialised.add_path(
            f"{self.api_base}/reactions/{service_name}", self.applets.get_reactions_by_service_name, "GET"
        )
