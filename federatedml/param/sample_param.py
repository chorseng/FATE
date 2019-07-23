#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
from federatedml.param.base_param import BaseParam


class SampleParam(BaseParam):
    """
    Define the sample method

    Parameters
    ----------
    mode: str, accepted 'random','stratified'' only in this version, specify samplet to use, default: 'random'

    method: str, accepted 'downsample','upsample' only in this version. default: 'downsample'

    fractions: None or float or list, if mode equals to random, it should be a float number greater than 0, otherwise a list of float elements. default: None

    random_state: int, RandomState instance or None, default: None
    """

    def __init__(self, mode="random", method="downsample", fractions=None, random_state=None, task_type="hetero", need_run=True):
        self.mode = mode
        self.method = method
        self.fractions = fractions
        self.random_state = random_state
        self.task_type = task_type
        self.need_run = need_run

    def check(self):
        descr = "sample param"
        self.mode = self.check_and_change_lower(self.mode,
                                                   ["random", "stratified"],
                                                   descr)

        self.method = self.check_and_change_lower(self.method,
                                                     ["upsample", "downsample"],
                                                     descr)

        return True
