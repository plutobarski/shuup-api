# -*- coding: utf-8 -*-
# This file is part of Shuup API.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf import settings
from rest_framework.reverse import reverse


def reverse_api_url(view_name, args=None, kwargs=None, request=None):
    if settings.SHUUP_API_URLS_NAMESPACE:
        view_name = "{}:{}".format(settings.SHUUP_API_URLS_NAMESPACE, view_name)
    return reverse(view_name, args=args, kwargs=kwargs, request=request)
