from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple,
    Union,
)

from vkbottle import ABCRule

from vkbottle.tools.dev.mini_types.base import BaseMessageMin
from vkbottle.tools.validator import (
    ABCValidator
)

DEFAULT_PREFIXES = ["!", "/"]
DEFAULT_ALIASES = ["Command", "command"]
STANDARD_PERMISSION = ['0']
PayloadMap = List[Tuple[str, Union[type, Callable[[Any], bool], ABCValidator, Any]]]
PayloadMapStrict = List[Tuple[str, ABCValidator]]
PayloadMapDict = Dict[str, Union[dict, type]]


class CommandRuleCustom(ABCRule[BaseMessageMin]):

    def __init__(
        self,
        command_aliases: Optional[List[str]] = None,
        prefixes: Optional[List[str]] = None,
        args_count: int = 0,
        sep: str = " ",
    ):
        self.prefixes = prefixes or DEFAULT_PREFIXES
        self.command_aliases = command_aliases or DEFAULT_ALIASES
        self.args_count = args_count
        self.sep = sep

    async def check(self, event: BaseMessageMin) -> Union[dict, bool]:
        for prefix in self.prefixes:
            for command_text in self.command_aliases:
                text_length = len(prefix + command_text)
                text_length_with_sep = text_length + len(self.sep)
                if event.text.startswith(prefix + command_text):
                    if not self.args_count and len(event.text) == text_length:
                        return True
                    elif self.args_count and self.sep in event.text:
                        args = event.text[text_length_with_sep:].split(self.sep)
                        return {"args": args} if len(args) == self.args_count and all(args) else False
        return False


class PermissionRule(ABCRule[BaseMessageMin]):

    def __init__(self, accessed_pls: Optional[List[str]] = None):
        self.accessed_pls = accessed_pls or STANDARD_PERMISSION

    async def check(self, event: BaseMessageMin) -> Union[dict, bool]:
        for lvl in self.accessed_pls:
            # TODO: Make a request with the level of rights of the user in the database that called the command.
            #  The query will return True\False
            if lvl:
                return True

        return False
