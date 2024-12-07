"""_summary_
    File in charge of providing a boiled down interface for interracting with an s3 bucket.
"""

from typing import List, Union, Dict, Any, Optional
import boto3
from botocore.client import Config
from botocore.exceptions import BotoCoreError, ClientError
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME
from ..components import CONST


class Bucket:
    """
    Class to manage interaction with an S3-compatible bucket like MinIO.
    """

    def __init__(self, error: int = 84, success: int = 0, debug: bool = False) -> None:
        self.debug: bool = debug
        self.error: int = error
        self.success: int = success

        # ------------------------ The logging function ------------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            FILE_DESCRIPTOR,
            SAVE_TO_FILE,
            FILE_NAME,
            debug=self.debug,
            logger=self.__class__.__name__
        )
        # ----------------------- The connector address  -----------------------
        self.connection: Optional[boto3.resource] = None

    def connect(self) -> int:
        """
        Connect to the S3 bucket or MinIO service.

        Returns:
            int: success or error code.
        """
        try:
            self.connection = boto3.resource(
                's3',
                # MinIO URL
                endpoint_url=f"{CONST.MINIO_HOST}:{CONST.MINIO_PORT}",
                aws_access_key_id=CONST.MINIO_ROOT_USER,  # MinIO root user
                aws_secret_access_key=CONST.MINIO_ROOT_PASSWORD,  # MinIO password
                config=Config(signature_version='s3v4')
            )
            # Check connection by listing buckets
            self.connection.meta.client.list_buckets()
            self.disp.log_info("Connection to MinIO S3 successful.", "connect")
            return self.success
        except (BotoCoreError, ClientError) as e:
            self.disp.log_error(
                f"Failed to connect to MinIO: {str(e)}",
                "connect"
            )
            return self.error

    def is_connected(self) -> bool:
        """
        Check if the connection to the S3-compatible service is active.

        Returns:
            bool: True if connected, False otherwise.
        """
        if self.connection is None:
            self.disp.log_error("No connection object found.", "is_connected")
            return False

        try:
            # Attempt to list buckets as a simple test of the connection
            self.connection.meta.client.list_buckets()
            self.disp.log_info("Connection is active.", "is_connected")
            return True
        except (BotoCoreError, ClientError, ConnectionError) as e:
            self.disp.log_error(
                f"Connection check failed: {str(e)}",
                "is_connected"
            )
            return False

    def disconnect(self) -> int:
        """
        Disconnect from the S3-compatible service by setting the connection to None.

        Returns:
            int: success or error code.
        """
        if self.connection is None:
            self.disp.log_warning(
                "No active connection to disconnect.",
                "disconnect"
            )
            return self.error

        try:
            self.connection = None
            self.disp.log_info(
                "Disconnected from the S3-compatible service.",
                "disconnect"
            )
            return self.success
        except Exception as e:
            self.disp.log_error(
                f"Failed to disconnect: {str(e)}",
                "disconnect"
            )
            return self.error

    def get_bucket_names(self) -> Union[List[str], int]:
        """
        Retrieve a list of all bucket names.

        Returns:
            Union[List[str], int]: A list of bucket names or error code.
        """
        try:
            if self.connection is None:
                raise ConnectionError("No connection established.")
            buckets = [bucket.name for bucket in self.connection.buckets.all()]
            return buckets
        except (BotoCoreError, ClientError, ConnectionError) as e:
            self.disp.log_error(
                f"Error fetching bucket names: {str(e)}",
                "get_bucket_names"
            )
            return self.error

    def create_bucket(self, bucket_name: str) -> int:
        """
        Create a new bucket.

        Args:
            bucket_name (str): Name of the bucket to create.

        Returns:
            int: success or error code.
        """
        try:
            if self.connection is None:
                raise ConnectionError("No connection established.")
            self.connection.create_bucket(Bucket=bucket_name)
            self.disp.log_info(
                f"Bucket '{bucket_name}' created successfully.",
                "create_bucket"
            )
            return self.success
        except (BotoCoreError, ClientError, ConnectionError) as e:
            self.disp.log_error(
                f"Failed to create bucket '{bucket_name}': {str(e)}",
                "create_bucket"
            )
            return self.error

    def upload_file(self, bucket_name: str, file_path: str, key_name: Optional[str] = None) -> int:
        """
        Upload a file to the specified bucket.

        Args:
            bucket_name (str): Name of the target bucket.
            file_path (str): Path of the file to upload.
            key_name (Optional[str]): Name to save the file as in the bucket. Defaults to the file path name.

        Returns:
            int: success or error code.
        """
        key_name = key_name or file_path
        try:
            if self.connection is None:
                raise ConnectionError("No connection established.")
            self.connection.Bucket(bucket_name).upload_file(
                file_path, key_name)
            msg = f"File '{file_path}' uploaded to bucket "
            msg += f"'{bucket_name}' as '{key_name}'."
            self.disp.log_info(msg, "upload_file")
            return self.success
        except (BotoCoreError, ClientError, ConnectionError) as e:
            msg = f"Failed to upload file '{file_path}' to bucket "
            msg += f"'{bucket_name}': {str(e)}"
            self.disp.log_error(msg, "upload_file")
            return self.error

    def download_file(self, bucket_name: str, key_name: str, destination_path: str) -> int:
        """
        Download a file from the specified bucket.

        Args:
            bucket_name (str): Name of the target bucket.
            key_name (str): Name of the file to download.
            destination_path (str): Local path where the file will be saved.

        Returns:
            int: success or error code.
        """
        try:
            if self.connection is None:
                raise ConnectionError("No connection established.")
            self.connection.Bucket(bucket_name).download_file(
                key_name, destination_path)
            msg = f"File '{key_name}' downloaded from bucket "
            msg += f"'{bucket_name}' to '{destination_path}'."
            self.disp.log_info(msg, "download_file")
            return self.success
        except (BotoCoreError, ClientError, ConnectionError) as e:
            msg = f"Failed to download file '{key_name}'"
            msg += f" from bucket '{bucket_name}': {str(e)}"
            self.disp.log_error(msg, "download_file")
            return self.error

    def delete_file(self, bucket_name: str, key_name: str) -> int:
        """
        Delete a file from the specified bucket.

        Args:
            bucket_name (str): Name of the bucket.
            key_name (str): Name of the file to delete.

        Returns:
            int: success or error code.
        """
        try:
            if self.connection is None:
                raise ConnectionError("No connection established.")
            self.connection.Bucket(bucket_name).Object(key_name).delete()
            self.disp.log_info(
                f"File '{key_name}' deleted from bucket '{bucket_name}'.",
                "delete_file"
            )
            return self.success
        except (BotoCoreError, ClientError, ConnectionError) as e:
            msg = f"Failed to delete file '{key_name}' from bucket "
            msg += f"'{bucket_name}': {str(e)}"
            self.disp.log_error(msg, "delete_file")
            return self.error

    def delete_bucket(self, bucket_name: str) -> int:
        """
        Delete a bucket.

        Args:
            bucket_name (str): Name of the bucket to delete.

        Returns:
            int: success or error code.
        """
        try:
            if self.connection is None:
                raise ConnectionError("No connection established.")
            self.connection.Bucket(bucket_name).delete()
            self.disp.log_info(
                f"Bucket '{bucket_name}' deleted successfully.",
                "delete_bucket"
            )
            return self.success
        except (BotoCoreError, ClientError, ConnectionError) as e:
            self.disp.log_error(
                f"Failed to delete bucket '{bucket_name}': {str(e)}",
                "delete_bucket"
            )
            return self.error

    def get_bucket_files(self, bucket_name: str) -> Union[List[str], int]:
        """
        List all files in the specified bucket.

        Args:
            bucket_name (str): Name of the bucket.

        Returns:
            Union[List[str], int]: List of file names or error code.
        """
        try:
            if self.connection is None:
                raise ConnectionError("No connection established.")
            files = []
            for obj in self.connection.Bucket(bucket_name).objects.all():
                files.append(obj.key)
            return files
        except (BotoCoreError, ClientError, ConnectionError) as e:
            msg = f"Failed to retrieve files from bucket '{bucket_name}'"
            msg += f": {str(e)}"
            self.disp.log_error(msg, "get_bucket_files")
            return self.error

    def get_bucket_file(self, bucket_name: str, key_name: str) -> Union[Dict[str, Any], int]:
        """
        Get information about a specific file in the bucket.

        Args:
            bucket_name (str): Name of the bucket.
            key_name (str): Name of the file.

        Returns:
            Union[Dict[str, Any], int]: File metadata (path and size) or error code.
        """
        try:
            if self.connection is None:
                raise ConnectionError("No connection established.")
            obj = self.connection.Bucket(bucket_name).Object(key_name)
            return {'file_path': key_name, 'file_size': obj.content_length}
        except (BotoCoreError, ClientError, ConnectionError) as e:
            msg = f"Failed to get file '{key_name}'"
            msg += f"from bucket '{bucket_name}': {str(e)}"
            self.disp.log_error(msg, "get_bucket_file")
            return self.error
