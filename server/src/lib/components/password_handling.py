"""
    File containing the class in charge of handling password for the server
"""
import bcrypt
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME


class PasswordHandling:
    """__summary__
    """

    def __init__(self, error: int = 84, success: int = 0, debug: bool = False) -> None:
        self.debug: bool = debug
        self.success: int = success
        self.error: int = error
        self.salt_rounds = 10
        # ------------------------ The logging function ------------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            FILE_DESCRIPTOR,
            SAVE_TO_FILE,
            FILE_NAME,
            debug=self.debug,
            logger=self.__class__.__name__
        )

    def hash_password(self, password: str) -> str:
        """
            The function to hash the password for the security
        Args:
            password (str): The entered password

        Returns:
            str: The hashed password
        """
        title = "_hash_password"
        self.disp.log_debug("Enter hash password", f"{title}")
        if isinstance(password, bytes) is False:
            password = bytes(password, encoding="utf-8")
            self.disp.log_debug("Start register endpoint", f"{title}")
        salt = bcrypt.gensalt(rounds=self.salt_rounds)
        safe_password = bcrypt.hashpw(password, salt)
        return safe_password.decode("utf-8")

    def check_password(self, password: str, password_hash: bytes) -> bool:
        """
            The function to check the entered password with the hashed password
        Args:
            password (str): The entered password
            password_hash (bytes): The hashed password

        Returns:
            bool: True if it's the same, False if not
        """
        msg = f"password = {type(password)}, "
        msg += f"password_hash = {type(password_hash)}"
        self.disp.log_debug(msg, "check_password")
        if isinstance(password, bytes) is False:
            password = password.encode("utf-8")
        if isinstance(password_hash, bytes) is False:
            password_hash = password_hash.encode("utf-8")
        msg = f"password = {type(password)}, password_hash = "
        msg += f"{type(password_hash)}"
        self.disp.log_debug(msg, "check_password")
        return bcrypt.checkpw(password, password_hash)
