from typing import Any

from bs4 import BeautifulSoup

from .._types import SupportsRead, _AnyStr
from ..etree import _ElementTree, _ElemFactory
from . import HtmlElement

def fromstring(
    data: _AnyStr | SupportsRead[str] | SupportsRead[bytes],
    beautifulsoup: type[BeautifulSoup] | None = ...,
    makeelement: _ElemFactory[HtmlElement] | None = ...,
    **bsargs: Any
) -> HtmlElement: ...
def parse(
    file: _AnyStr | SupportsRead[str] | SupportsRead[bytes],
    beautifulsoup: type[BeautifulSoup] | None = ...,
    makeelement: _ElemFactory[HtmlElement] | None = ...,
    **bsargs: Any
) -> _ElementTree: ...
def convert_tree(
    beautiful_soup_tree: BeautifulSoup,
    makeelement: _ElemFactory[HtmlElement] | None = ...,
) -> list[HtmlElement]: ...