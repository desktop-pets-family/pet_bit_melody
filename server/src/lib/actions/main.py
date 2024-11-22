"""_summary_
    The main file of this section, in charge of the action processing
"""

import os
from typing import Dict, Union, List, Any
from time import sleep
from random import uniform, randint
from string import ascii_letters, digits
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME

from ..components.runtime_data import RuntimeData
from ..components import CONST

from .variables import Variables
from .logger import ActionLogger
from .action_management import ActionManagement
from .trigger_management import TriggerManagement
from . import constants as ACONST


class ActionsMain:
    """_summary_
    """

    def __init__(self, runtime_data: RuntimeData, error: int = 84, success: int = 0, debug: bool = False):
        """_summary_
            Class in charge of processing the actions.

        Args:
            runtime_data (RuntimeData): _description_
            error (int, optional): _description_. Defaults to 84.
            success (int, optional): _description_. Defaults to 0.
            debug (bool, optional): _description_. Defaults to False.
        """
        # -------------------------- Inherited values --------------------------
        self.error = error
        self.debug = debug
        self.success = success
        self.runtime_data = runtime_data
        # ---------------------- The visual logger class  ----------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            SAVE_TO_FILE,
            FILE_NAME,
            FILE_DESCRIPTOR,
            debug=self.debug,
            logger=self.__class__.__name__
        )
        # -------------------------- Internal classes --------------------------
        self.variables: Variables = Variables(
            success=self.success,
            error=self.error,
            debug=self.debug
        )
        self.logger: ActionLogger = ActionLogger(
            runtime_data=self.runtime_data,
            success=self.success,
            error=self.error,
            debug=self.debug
        )

    def cache_busting(self, length: int) -> int:
        """_summary_
            Function in charge of generating a cache busting string.

        Args:
            length (int): _description_: The action id.

        Returns:
            int: _description_: The result of the cache busting.
        """
        node_text = "cache_busting"
        data = str(ascii_letters + digits)
        data_length = len(data)-1
        cache_busting = f"{node_text}_"
        for i in range(0, length):
            cache_busting += data[randint(0, data_length)]
        cache_busting += f"_{node_text}"
        return cache_busting

    def random_delay(self, max_value: float = 1) -> float:
        """_summary_
            Function in charge of generating a random delay.
        """
        delay = uniform(0, max_value)
        delay = int(delay * 100) / 100
        return delay

    def get_action_ids(self) -> Union[int, List[str]]:
        """_summary_
            Function in charge of getting the action ids.
        """
        title = "get_action_ids"
        self.disp.log_debug("Getting the action ids", title)
        action_ids = self.runtime_data.database_link.get_data_from_table(
            table=CONST.TAB_ACTIONS,
            column=["id"],
            beautify=False
        )
        self.disp.log_debug(f"action_ids = {action_ids}", title)
        if action_ids == self.error:
            return self.error
        self.disp.log_debug("Processing ids.", title)
        res = []
        for i in action_ids:
            res.append(i[0])
        self.disp.log_debug(f"processed ids = {res}", title)
        return res

    def lock_action(self, node: int) -> int:
        """_summary_
            Function in charge of locking an action.

        Args:
            node (int): _description_: The action to lock.

        Returns:
            int: _description_: Returns self.success if it succeeded, self.error otherwise
        """
        title = "lock_action"
        self.disp.log_debug(f"Locking action {node}.", title)
        if self.is_action_locked(node) is True:
            self.disp.log_debug(f"Action {node} already locked.", title)
            return self.error
        locked = self.runtime_data.database_link.update_data_in_table(
            table=CONST.TAB_ACTIONS,
            column=["running"],
            data=["1"],
            where=f"id={node}"
        )
        if locked == self.error:
            msg = f"Failed to lock action {node} by process {os.getpid()}"
            self.disp.log_debug(msg, title)
            self.logger.log_success(
                log_type=ACONST.TYPE_SERVICE,
                action_id=node,
                message=msg,
                resolved=True
            )
            return self.error
        msg = f"Action {node} locked by process {os.getpid()}."
        self.disp.log_debug(msg, title)
        self.logger.log_success(
            log_type=ACONST.TYPE_SERVICE,
            action_id=node,
            message=msg,
            resolved=True
        )
        return self.success

    def unlock_action(self, node: int) -> int:
        """_summary_
            Function in charge of unlocking an action.

        Args:
            node (int): _description_: The action to unlock.

        Returns:
            int: _description_: Returns self.success if it succeeded, self.error otherwise
        """
        title = "unlock_action"
        self.disp.log_debug(f"Unlocking action {node}.", title)
        if self.is_action_locked(node) is False:
            self.disp.log_debug(f"Action {node} already unlocked.", title)
            return self.error
        locked = self.runtime_data.database_link.update_data_in_table(
            table=CONST.TAB_ACTIONS,
            column=["running"],
            data=["0"],
            where=f"id={node}"
        )
        if locked == self.error:
            msg = f"Failed to unlock action {node} by process {os.getpid()}"
            self.disp.log_debug(msg, title)
            self.logger.log_success(
                log_type=ACONST.TYPE_SERVICE,
                action_id=node,
                message=msg,
                resolved=True
            )
            return self.error
        msg = f"Action {node} unlocked by process {os.getpid()}."
        self.disp.log_debug(msg, title)
        self.logger.log_success(
            log_type=ACONST.TYPE_SERVICE,
            action_id=node,
            message=msg,
            resolved=True
        )
        return self.success

    def dump_scope(self, action_id: int, scope: Any, log_type: str = ACONST.TYPE_RUNTIME_ERROR) -> int:
        """_summary_
            Dump the content of the scope to the logging database before clearing the cache.

        Args:
            scope (Any): _description_: The concerned scope.

        Returns:
            int: _description_: The status of how the scope dumping went.
        """
        title = "dump_scope"
        # data = self.variables.get_scope(scope=scope)
        # data = self.variables.sanitize_for_json(data)
        # try:
        #     data = json.dumps(
        #         data,
        #         skipkeys=False,
        #         ensure_ascii=True,
        #         check_circular=True,
        #         allow_nan=True,
        #         cls=None,
        #         indent=None,
        #         sort_keys=False,
        #     )
        # except Exception:
        #     data = f"{data}"
        # self.logger.log_info(
        #     log_type=log_type,
        #     action_id=action_id,
        #     message=data,
        #     resolved=False
        # )
        self.disp.log_warning(
            "Scope dumping is disabled for time reasons.",
            title
        )
        return self.success

    def process_action_node(self, node: int) -> int:
        """_summary_
            Function in charge of processing a given action.

        Args:
            node (int): _description_

        Returns:
            int: _description_
        """
        title = "process_action_node"
        variable_scope = f"action_{node}"
        action_detail = self.runtime_data.database_link.get_data_from_table(
            table=CONST.TAB_ACTIONS,
            column="*",
            where=f"id={node}",
            beautify=True
        )
        if action_detail == self.error:
            msg = f"Failed to get the action {node} details"
            msg += f"for process {os.getpid()}."
            self.disp.log_critical(msg, title)
            self.logger.log_fatal(
                log_type=ACONST.TYPE_SERVICE,
                action_id=node,
                message=msg,
                resolved=False
            )
            return self.error
        self.disp.log_debug(
            f"action_detail = {action_detail}",
            title
        )
        self.variables.create_scope(scope_name=variable_scope)
        self.variables.clear_variables(scope=variable_scope)
        cache_busting = self.cache_busting(10)
        node_key = f"node_data_{node}_{cache_busting}"
        self.variables.add_variable(
            name=node_key,
            variable_data=action_detail[0],
            variable_type=type(action_detail[0]),
            scope=variable_scope
        )
        trigger_node: TriggerManagement = TriggerManagement(
            variable=self.variables,
            logger=self.logger,
            runtime_data=self.runtime_data,
            action_id=node,
            error=self.error,
            success=self.success,
            scope=variable_scope,
            debug=self.debug,
            delay=CONST.API_REQUEST_DELAY
        )
        action_node: ActionManagement = ActionManagement(
            variable=self.variables,
            logger=self.logger,
            runtime_data=self.runtime_data,
            action_id=node,
            error=self.error,
            success=self.success,
            scope=variable_scope,
            debug=self.debug,
            delay=CONST.API_REQUEST_DELAY
        )
        try:
            status = trigger_node.run(node_key)
        except Exception as e:
            self.logger.log_fatal(
                log_type=ACONST.TYPE_SERVICE_TRIGGER,
                action_id=node,
                message=f"Failed to run the trigger node: {e}",
                resolved=False
            )
            self.dump_scope(
                action_id=node,
                scope=variable_scope,
                log_type=ACONST.TYPE_SERVICE_TRIGGER
            )
            self.variables.clear_variables(scope=variable_scope)
            self.unlock_action(node)
            return self.error
        if status == self.error:
            self.logger.log_fatal(
                log_type=ACONST.TYPE_SERVICE_TRIGGER,
                action_id=node,
                message="Failed to run the trigger node.",
                resolved=False
            )
            self.dump_scope(
                action_id=node,
                scope=variable_scope,
                log_type=ACONST.TYPE_SERVICE_TRIGGER
            )
            self.variables.clear_variables(scope=variable_scope)
            self.unlock_action(node)
            return self.error
        try:
            status = action_node.run(node_key)
        except Exception as e:
            self.logger.log_fatal(
                log_type=ACONST.TYPE_SERVICE_ACTION,
                action_id=node,
                message=f"Failed to run the action node: {e}",
                resolved=False
            )
            self.dump_scope(
                action_id=node,
                scope=variable_scope,
                log_type=ACONST.TYPE_SERVICE_ACTION
            )
            self.unlock_action(node)
            return self.error
        if status == self.error:
            self.logger.log_fatal(
                log_type=ACONST.TYPE_SERVICE_ACTION,
                action_id=node,
                message="Failed to run the action node.",
                resolved=False
            )
            self.dump_scope(
                action_id=node,
                scope=variable_scope,
                log_type=ACONST.TYPE_SERVICE_ACTION
            )
            self.unlock_action(node)
            return self.error
        self.unlock_action(node)
        return self.success

    def is_action_locked(self, node: int) -> bool:
        """_summary_
            Function in charge of checking if the action is locked.

        Args:
            node (int): _description_

        Returns:
            bool: _description_
        """
        title = "is_action_locked"
        self.disp.log_debug(f"Checking if action {node} is locked.", title)
        locked = self.runtime_data.database_link.get_data_from_table(
            table=CONST.TAB_ACTIONS,
            column=["running"],
            where=f"id={node}",
            beautify=False
        )
        self.disp.log_debug(f"action info = {locked}", title)
        if locked == self.error or len(locked) == 0:
            return True
        if locked[0][0] == 1:
            self.disp.log_debug(f"Action {node} is locked.", title)
            return True
        self.disp.log_debug(f"Action {node} is not locked.", title)
        return False

    def execute_actions(self) -> Dict[str, int]:
        """_summary_
            The function in charge of processing actions.

        Returns:
            int: _description_: The statuses of all the runs.
        """
        delay = self.random_delay(1)
        sleep(delay)
        execution_statuses = {}
        actions = self.get_action_ids()
        if actions == self.error:
            return self.error
        for action in actions:
            if self.is_action_locked(action) is True:
                continue
            if self.lock_action(action) != self.success:
                continue
            execution_statuses[action] = self.process_action_node(action)
        return execution_statuses
