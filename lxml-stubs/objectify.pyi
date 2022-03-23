from typing import Any, Iterator

from ._types import _AnyStr, _NSMapArg
from .etree import ElementBase, QName, _Element, _ElemFactory
from .etree._parser import _DefEtreeParsers

class ObjectifiedElement(ElementBase):
    def __iter__(self) -> Iterator[ObjectifiedElement]: ...
    def __reversed__(self) -> Iterator[ObjectifiedElement]: ...
    def __getattr__(self, __k: str) -> ObjectifiedElement: ...

def fromstring(
    text: _AnyStr,
    parser: _DefEtreeParsers[_Element] | None = ...,
    *,
    base_url: _AnyStr = ...,
) -> ObjectifiedElement: ...

class ElementMaker:
    def __init__(
        self,
        namespace: str | None = ...,
        nsmap: _NSMapArg | None = ...,
        annotate: bool = ...,
        # same signature as etree.Element()
        makeelement: _ElemFactory[ObjectifiedElement] | None = ...,
    ) -> None: ...
    def __call__(
        self,
        tag: str | QName,  # No bytes here
        # Although, by default, the ElementMaker only accepts _Element and types
        # interpretable by the default typemap (that is str, CDATA and dict)
        # as children, the typemap can be expanded to make sure items of any
        # type are accepted.
        *children: Any,
        **attrib: str,
    ) -> ObjectifiedElement: ...
    # __getattr__ here is special. ElementMaker is a factory that generates
    # elements with any tag provided as attribute name, as long as the name
    # does not conflict with the basic object methods (including python keywords
    # like "class" and "for", which are common in HTML)
    def __getattr__(self, name: str) -> _ElemFactory[ObjectifiedElement]: ...

E: ElementMaker
