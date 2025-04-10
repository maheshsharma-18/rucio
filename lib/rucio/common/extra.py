# Copyright European Organization for Nuclear Research (CERN) since 2012
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import importlib
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from collections.abc import Iterable
    from types import ModuleType


def import_extras(module_list: 'Iterable[str]') -> dict[str, "Optional[ModuleType]"]:
    out = dict()
    for mod in module_list:
        out[mod] = None
        try:
            out[mod] = importlib.import_module(mod)
        except ImportError:
            pass
    return out
