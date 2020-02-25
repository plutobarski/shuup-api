# -*- coding: utf-8 -*-
# This file is part of Shuup API.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from shuup_api.utils import reverse_api_url


def test_reverse_urls(admin_user):
    assert reverse_api_url('users-list') == "/api/test/user/"
