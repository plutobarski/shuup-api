# -*- coding: utf-8 -*-
# This file is part of Shuup API.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
# See https://stackoverflow.com/questions/14567586/
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class ObtainExpiringAuthToken(views.ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        token, created = Token.objects.get_or_create(user=serializer.validated_data['user'])
        if not created:
            token.delete()
            token = Token.objects.create(user=serializer.validated_data['user'])

        return Response({'token': token.key})


refresh_auth_token = ObtainExpiringAuthToken.as_view()
