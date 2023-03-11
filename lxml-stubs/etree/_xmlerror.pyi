#
# Types for lxml/xmlerror.pxi
#

import enum
from logging import Logger
from typing import Collection, Iterator, final
from typing_extensions import Self

@final
class _LogEntry:
    @property
    def doamin(self) -> ErrorDomains: ...
    @property
    def type(self) -> ErrorTypes: ...
    @property
    def level(self) -> ErrorLevels: ...
    @property
    def line(self) -> int: ...
    @property
    def column(self) -> int: ...
    @property
    def doamin_name(self) -> str: ...
    @property
    def type_name(self) -> str: ...
    @property
    def level_name(self) -> str: ...
    @property
    def message(self) -> str: ...
    @property
    def filename(self) -> str | None: ...
    @property
    def path(self) -> str: ...

class _BaseErrorLog:
    @property
    def last_error(self) -> _LogEntry: ...
    # copy() method is originally under _BaseErrorLog class. However
    # PyErrorLog overrides it with a dummy version, denoting it
    # shouldn't be used. So move copy() to the only other subclass
    # inherited from _BaseErrorLog, that is _ListErrorLog.
    def receive(self, log_entry: _LogEntry) -> None: ...

class _ListErrorLog(_BaseErrorLog, Collection[_LogEntry]):
    def __iter__(self) -> Iterator[_LogEntry]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, __k: int) -> _LogEntry: ...
    def __contains__(self, __o: object) -> bool: ...
    def filter_domains(self, domains: int | tuple[int]) -> _ListErrorLog: ...
    def filter_types(self, types: int | tuple[int]) -> _ListErrorLog: ...
    def filter_levels(self, levels: int | tuple[int]) -> _ListErrorLog: ...
    def filter_from_level(self, level: int) -> _ListErrorLog: ...
    def filter_from_fatals(self) -> _ListErrorLog: ...
    def filter_from_errors(self) -> _ListErrorLog: ...
    def filter_from_warnings(self) -> _ListErrorLog: ...
    def clear(self) -> None: ...
    # Context manager behavior is internal to cython, not usable
    # in python code, so dropped altogether.
    # copy() is originally implemented in _BaseErrorLog, see
    # comment there for more info.
    def copy(self) -> Self: ...

# The interaction between _ListErrorLog and _ErrorLog is interesting.
# _ListErrorLog is the base class, and unlikely to be instantiated
# directly. _ErrorLog class instantiates _ListErrorLog object, and
# patches it with extra runtime methods.
# Here we merge all extra _ErrorLog methods into _ListErrorLog,
# and make _Errorlog a function instead. Mypy become ferocious when
# the idea of returning different object via __new__() comes up
def _ErrorLog() -> _ListErrorLog: ...

class _RotatingErrorLog(_ListErrorLog): ...

# Maybe there's some sort of hidden commercial version of lxml
# that supports _DomainErrorLog? Anyway, the class in open source
# lxml is entirely broken and not touched since 2006.

def clear_error_log() -> None: ...

class PyErrorLog(_BaseErrorLog):
    @property
    def level_map(self) -> dict[int, int]: ...
    def __init__(self, logger_name: str | None = ..., logger: Logger = ...) -> None: ...
    # copy() is disallowed, implementation chooses to fail in a
    # silent way by returning dummy object. We skip it altogether.
    def log(self, log_entry: _LogEntry, message: str, *args: object) -> None: ...

def use_global_python_log(log: PyErrorLog) -> None: ...

# Container for libxml2 constants
# It's overkill to include zillions of constants into type checker;
# and more no-no for updating constants along with each lxml releases
# unless these stubs are bundled with lxml together. So we only do
# minimal enums which do not involve much work. No ErrorTypes. Never.
class ErrorLevels(enum.IntEnum):
    NONE = ...
    WARNING = ...
    ERROR = ...
    FATAL = ...

class ErrorDomains(enum.IntEnum):
    NONE = ...
    PARSER = ...
    TREE = ...
    NAMESPACE = ...
    DTD = ...
    HTML = ...
    MEMORY = ...
    OUTPUT = ...
    IO = ...
    FTP = ...
    HTTP = ...
    XINCLUDE = ...
    XPATH = ...
    XPOINTER = ...
    REGEXP = ...
    DATATYPE = ...
    SCHEMASP = ...
    SCHEMASV = ...
    RELAXNGP = ...
    RELAXNGV = ...
    CATALOG = ...
    C14N = ...
    XSLT = ...
    VALID = ...
    CHECK = ...
    WRITER = ...
    MODULE = ...
    I18N = ...
    SCHEMATRONV = ...
    BUFFER = ...
    URI = ...

class ErrorTypes(enum.IntEnum):
    def __getattr__(self, name: str) -> ErrorTypes: ...

class RelaxNGErrorTypes(enum.IntEnum):
    RELAXNG_OK = ...
    RELAXNG_ERR_MEMORY = ...
    RELAXNG_ERR_TYPE = ...
    RELAXNG_ERR_TYPEVAL = ...
    RELAXNG_ERR_DUPID = ...
    RELAXNG_ERR_TYPECMP = ...
    RELAXNG_ERR_NOSTATE = ...
    RELAXNG_ERR_NODEFINE = ...
    RELAXNG_ERR_LISTEXTRA = ...
    RELAXNG_ERR_LISTEMPTY = ...
    RELAXNG_ERR_INTERNODATA = ...
    RELAXNG_ERR_INTERSEQ = ...
    RELAXNG_ERR_INTEREXTRA = ...
    RELAXNG_ERR_ELEMNAME = ...
    RELAXNG_ERR_ATTRNAME = ...
    RELAXNG_ERR_ELEMNONS = ...
    RELAXNG_ERR_ATTRNONS = ...
    RELAXNG_ERR_ELEMWRONGNS = ...
    RELAXNG_ERR_ATTRWRONGNS = ...
    RELAXNG_ERR_ELEMEXTRANS = ...
    RELAXNG_ERR_ATTREXTRANS = ...
    RELAXNG_ERR_ELEMNOTEMPTY = ...
    RELAXNG_ERR_NOELEM = ...
    RELAXNG_ERR_NOTELEM = ...
    RELAXNG_ERR_ATTRVALID = ...
    RELAXNG_ERR_CONTENTVALID = ...
    RELAXNG_ERR_EXTRACONTENT = ...
    RELAXNG_ERR_INVALIDATTR = ...
    RELAXNG_ERR_DATAELEM = ...
    RELAXNG_ERR_VALELEM = ...
    RELAXNG_ERR_LISTELEM = ...
    RELAXNG_ERR_DATATYPE = ...
    RELAXNG_ERR_VALUE = ...
    RELAXNG_ERR_LIST = ...
    RELAXNG_ERR_NOGRAMMAR = ...
    RELAXNG_ERR_EXTRADATA = ...
    RELAXNG_ERR_LACKDATA = ...
    RELAXNG_ERR_INTERNAL = ...
    RELAXNG_ERR_ELEMWRONG = ...
    RELAXNG_ERR_TEXTWRONG = ...
