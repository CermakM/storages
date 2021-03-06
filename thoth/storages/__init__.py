#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# thoth-storages
# Copyright(C) 2018 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Storage and database adapters for Thoth."""

from .advisers import AdvisersResultsStore
from .advisers_cache import AdvisersCacheStore
from .analyses import AnalysisResultsStore
from .analyses_cache import AnalysesCacheStore
from .buildlogs import BuildLogsStore
from .ceph import CephStore
from .graph import GraphDatabase
from .provenance import ProvenanceResultsStore
from .provenance_cache import ProvenanceCacheStore
from .result_schema import RESULT_SCHEMA
from .solvers import SolverResultsStore

__name__ = 'thoth-storages'
__version__ = "0.7.2"
