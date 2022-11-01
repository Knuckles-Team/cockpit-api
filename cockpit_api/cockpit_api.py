#!/usr/bin/python
# coding: utf-8

import json
import requests
import urllib3

try:
    from cockpit_api.decorators import require_auth
except ModuleNotFoundError:
    from decorators import require_auth
try:
    from cockpit_api.exceptions import (AuthError, UnauthorizedError, ParameterError, MissingParameterError)
except ModuleNotFoundError:
    from exceptions import (AuthError, UnauthorizedError, ParameterError, MissingParameterError)


class Api(object):

    def __init__(self, url=None, token=None, verify=True):
        if url is None:
            raise MissingParameterError

        self._session = requests.Session()
        self.url = url
        self.token = token
        if self.token:
            self.headers = {
                'api-key': self.token,
                'Content-Type': 'application/json'
            }
        else:
            raise MissingParameterError

        self.verify = verify

        if self.verify is False:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        response = self._session.get(f'{self.url}/pages/menus', headers=self.headers, verify=self.verify)

        if response.status_code == 403:
            raise UnauthorizedError
        elif response.status_code == 401:
            raise AuthError
        elif response.status_code == 404:
            raise ParameterError

    ####################################################################################################################
    #                                            Content API                                                           #
    ####################################################################################################################
    @require_auth
    def get_content_item(self, model=None, model_filter=None, locale=None, fields=None, populate=None):
        data = None
        if model is None:
            raise MissingParameterError
        api_parameters = None
        if model_filter:
            if api_parameters:
                api_parameters = f'{api_parameters}&filter={model_filter}'
            else:
                api_parameters = f'&filter={model_filter}'
        if locale:
            if api_parameters:
                api_parameters = f'{api_parameters}&locale={locale}'
            else:
                api_parameters = f'&locale={locale}'
        if fields:
            if api_parameters:
                api_parameters = f'{api_parameters}&fields={fields}'
            else:
                api_parameters = f'&fields={fields}'
        if populate:
            if api_parameters:
                api_parameters = f'{api_parameters}&populate={populate}'
            else:
                api_parameters = f'&populate={populate}'
        response = self._session.get(f'{self.url}/content/item/{model}{api_parameters}', headers=self.headers,
                                     data=data, verify=self.verify)
        try:
            return response.json()
        except ValueError and AttributeError:
            return response

    @require_auth
    def post_content_item(self, model=None, data=None):
        if model is None:
            raise MissingParameterError
        if data and len(data) > 0:
            try:
                data = json.dumps(data, indent=4)
            except ValueError:
                raise ParameterError
        response = self._session.post(f'{self.url}/content/item/{model}', headers=self.headers, data=data,
                                      verify=self.verify)
        try:
            return response.json()
        except ValueError and AttributeError:
            return response

    @require_auth
    def get_content_item_by_id(self, model=None, item_id=None, locale=None, fields=None, populate=None):
        data = None
        if model is None or item_id is None:
            raise MissingParameterError
        api_parameters = None
        if locale:
            if api_parameters:
                api_parameters = f'{api_parameters}&locale={locale}'
            else:
                api_parameters = f'&locale={locale}'
        if fields:
            if api_parameters:
                api_parameters = f'{api_parameters}&fields={fields}'
            else:
                api_parameters = f'&fields={fields}'
        if populate:
            if api_parameters:
                api_parameters = f'{api_parameters}&populate={populate}'
            else:
                api_parameters = f'&populate={populate}'
        response = self._session.get(f'{self.url}/content/item/{model}/{item_id}{api_parameters}', headers=self.headers,
                                     data=data, verify=self.verify)
        try:
            return response.json()
        except ValueError and AttributeError:
            return response

    @require_auth
    def delete_content_item_by_id(self, model=None, item_id=None):
        data = None
        if model is None or item_id is None:
            raise MissingParameterError
        response = self._session.delete(f'{self.url}/content/item/{model}/{item_id}', headers=self.headers, data=data,
                                        verify=self.verify)
        try:
            return response.json()
        except ValueError and AttributeError:
            return response

    @require_auth
    def get_content(self, model=None, model_filter=None, model_sort=None, locale=None, fields=None, limit=None,
                    skip=None, populate=None):
        data = None
        if model is None:
            raise MissingParameterError
        api_parameters = None
        if model_filter:
            if api_parameters:
                api_parameters = f'{api_parameters}&filter={model_filter}'
            else:
                api_parameters = f'&filter={model_filter}'
        if model_sort:
            if api_parameters:
                api_parameters = f'{api_parameters}&sort={model_sort}'
            else:
                api_parameters = f'&sort={model_sort}'
        if locale:
            if api_parameters:
                api_parameters = f'{api_parameters}&locale={locale}'
            else:
                api_parameters = f'&locale={locale}'
        if fields:
            if api_parameters:
                api_parameters = f'{api_parameters}&fields={fields}'
            else:
                api_parameters = f'&fields={fields}'
        if limit:
            if api_parameters:
                api_parameters = f'{api_parameters}&limit={limit}'
            else:
                api_parameters = f'&limit={limit}'
        if skip:
            if api_parameters:
                api_parameters = f'{api_parameters}&skip={skip}'
            else:
                api_parameters = f'&skip={skip}'
        if populate:
            if api_parameters:
                api_parameters = f'{api_parameters}&populate={populate}'
            else:
                api_parameters = f'&populate={populate}'
        response = self._session.get(f'{self.url}/content/items/{model}{api_parameters}', headers=self.headers,
                                     data=data, verify=self.verify)
        try:
            return response.json()
        except ValueError and AttributeError:
            return response

    ####################################################################################################################
    #                                               Assets API                                                         #
    ####################################################################################################################
    @require_auth
    def get_asset(self, asset_id=None):
        if asset_id is None:
            raise MissingParameterError
        response = self._session.get(f'{self.url}/assets/{asset_id}', headers=self.headers, verify=self.verify)
        try:
            return response.json()
        except ValueError and AttributeError:
            return response

    @require_auth
    def get_image_asset(self, image_id=None, resize_mode="None", width=None, height=None, quality=None, mime=None,
                        auto_redirect=None, cache_invalidation_time=None, binary_generated_thumbnail=None):
        if image_id is None:
            raise MissingParameterError
        api_parameters = None
        if resize_mode:
            if resize_mode not in ['thumbnail', 'bestFit', 'resize', 'fitToWidth', 'fitToHeight']:
                raise ParameterError
            if api_parameters:
                api_parameters = f'{api_parameters}&m={resize_mode}'
            else:
                api_parameters = f'&m={resize_mode}'
        if width:
            if not isinstance(width, int):
                raise ParameterError
            if api_parameters:
                api_parameters = f'{api_parameters}&w={width}'
            else:
                api_parameters = f'&w={width}'
        if height:
            if not isinstance(height, int):
                raise ParameterError
            if api_parameters:
                api_parameters = f'{api_parameters}&h={height}'
            else:
                api_parameters = f'&h={height}'
        if quality:
            if not isinstance(quality, int):
                raise ParameterError
            if api_parameters:
                api_parameters = f'{api_parameters}&q={quality}'
            else:
                api_parameters = f'&q={quality}'
        if mime:
            if not isinstance(mime, int):
                raise ParameterError
            if api_parameters:
                api_parameters = f'{api_parameters}&mime={mime}'
            else:
                api_parameters = f'&mime={mime}'
        if auto_redirect:
            if not isinstance(auto_redirect, int):
                raise ParameterError
            if api_parameters:
                api_parameters = f'{api_parameters}&re={auto_redirect}'
            else:
                api_parameters = f'&re={auto_redirect}'
        if cache_invalidation_time:
            if not isinstance(cache_invalidation_time, str):
                raise ParameterError
            if api_parameters:
                api_parameters = f'{api_parameters}&t={cache_invalidation_time}'
            else:
                api_parameters = f'&t={cache_invalidation_time}'
        if binary_generated_thumbnail:
            if not isinstance(binary_generated_thumbnail, int):
                raise ParameterError
            if api_parameters:
                api_parameters = f'{api_parameters}&o={binary_generated_thumbnail}'
            else:
                api_parameters = f'&o={binary_generated_thumbnail}'
        response = self._session.get(f'{self.url}/assets/image/{image_id}{api_parameters}', headers=self.headers,
                                     verify=self.verify)
        try:
            return response.json()
        except ValueError and AttributeError:
            return response
