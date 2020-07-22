# -*- coding: utf-8 -*-
# This file is part of Shuup API.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

#: The namespace to be used in API urls to help reversing them.
#: This setting must be configured in Django project urls to include this as the namespace.
#: For example:
#   url(r'^api/', include('shuup_api.urls', namespace=settings.SHUUP_API_URLS_NAMESPACE)),
#:
SHUUP_API_URLS_NAMESPACE = ""
SHUUP_API_TOKEN_AGE = 12
