from typing import List, Optional

import requests

from .base_client import BaseClient
from .types.timeseries_types import TimeseriesType, TimeseriesDataPointType, TimeseriesDataType
from .utils import filter_none_values_from_dict

Response = requests.models.Response


class TimeseriesClient(BaseClient):
    """
    A client for handling the timeseries section of NODA Self-host API
    """

    def __init__(self,
                 base_url: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None
                 ) -> None:
        super().__init__(base_url, username, password)
        self._timeseries_api_path = 'timeseries'

    def get_timeseries(self,
                       limit: Optional[int] = None,
                       offset: Optional[int] = None,
                       tags: Optional[List[str]] = None
                       ) -> List[TimeseriesType]:
        """Fetches timeseries from NODA Self-host API

        Args:
            limit (Optional[int]): The numbers of items to return.
            offset (Optional[int]): The number of items to skip before starting to collect the result set.
            tags (Optional[List[str]]): List of tags to match on.

        Returns:
            List[:class:`.TimeseriesType`]

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.get(
            url=f'{self._base_url}/{self._api_version}/{self._timeseries_api_path}',
            params=filter_none_values_from_dict({
                'limit': limit,
                'offset': offset,
                'tags': tags
            })
        )
        return self._process_response(response)

    def create_timeseries(self,
                          name: str,
                          si_unit: str,
                          thing_uuid: Optional[str] = None,
                          lower_bound: Optional[int] = None,
                          upper_bound: Optional[int] = None,
                          tags: Optional[List[str]] = None
                          ) -> TimeseriesType:
        """Add a new timeseries to the NODA Self-host API

        Args:
            name (str): The name of the timeseries
            si_unit (str): The SI unit assigned to this timeseries
            thing_uuid (Optional[str]): UUID of the thing associated to this timeseries
            lower_bound (Optional[int]): The lower bound of a time series.
            upper_bound (Optional[int]): The upper bound of a time series.
            tags (Optional[List[str]]): Tags pinned on the timeseries.

        Returns:
            :class:`.TimeseriesType`

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.post(
            url=f'{self._base_url}/{self._api_version}/{self._timeseries_api_path}',
            json=filter_none_values_from_dict({
                'name': name,
                'si_unit': si_unit,
                'thing_uuid': thing_uuid,
                'lower_bound': lower_bound,
                'upper_bound': upper_bound,
                'tags': tags
            })
        )
        return self._process_response(response)

    def get_timeseries_by_uuid(self, timeseries_uuid: str) -> TimeseriesType:
        """Returns a timeseries from NODA Self-host API by UUID

        Args:
            timeseries_uuid (str): UUID of timeseries to fetch.

        Returns:
            :class:`.TimeseriesType`

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostNotFoundException`: The requested resource was not found.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.get(
            url=f'{self._base_url}/{self._api_version}/{self._timeseries_api_path}/{timeseries_uuid}'
        )
        return self._process_response(response)

    def update_timeseries(self,
                          timeseries_uuid: str,
                          name: Optional[str] = None,
                          si_unit: Optional[str] = None,
                          thing_uuid: Optional[str] = None,
                          lower_bound: Optional[int] = None,
                          upper_bound: Optional[int] = None,
                          tags: Optional[List[str]] = None
                          ) -> None:
        """Updates a timeseries from NODA Self-host API

        Args:
            timeseries_uuid (str): UUID of timeseries to update.
            name (Optional[str]): The name of the user
            si_unit (Optional[str]): The SI unit assigned to this timeseries
            thing_uuid (Optional[str]): UUID of the thing associated to this timeseries
            lower_bound (Optional[int]): The lower bound of a time series.
            upper_bound (Optional[int]): The upper bound of a time series.
            tags (Optional[List[str]]): Tags pinned on this timeseries

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostNotFoundException`: The requested resource was not found.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.put(
            url=f'{self._base_url}/{self._api_version}/{self._timeseries_api_path}/{timeseries_uuid}',
            json=filter_none_values_from_dict({
                'name': name,
                'si_unit': si_unit,
                'thing_uuid': thing_uuid,
                'lower_bound': lower_bound,
                'upper_bound': upper_bound,
                'tags': tags
            })
        )
        return self._process_response(response)

    def delete_timeseries(self, timeseries_uuid: str) -> None:
        """Deletes a timeseries from NODA Self-host API

        Args:
            timeseries_uuid (str): UUID of timeseries to delete.

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostNotFoundException`: The requested resource was not found.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.delete(
            url=f'{self._base_url}/{self._api_version}/{self._timeseries_api_path}/{timeseries_uuid}'
        )
        return self._process_response(response)

    def get_timeseries_data(self,
                            timeseries_uuid: str,
                            start: str,
                            end: str,
                            unit: Optional[str] = None,
                            ge: Optional[int] = None,
                            le: Optional[int] = None,
                            precision: Optional[str] = None,
                            aggregate: Optional[str] = None,
                            timezone: Optional[str] = None
                            ) -> List[TimeseriesDataPointType]:
        """Fetch a range of timeseries data from NODA Self-host API

        Args:
            timeseries_uuid (str): UUID of timeseries to query.
            start (datetime str): Start (>=) of time period. The period (start to end) can not exceed 1 year.
                Must be in format: YYYY-MM-DDThh:mm:ss+hh:mm (as defined by RFC 3339, section 5.6.)
            end (datetime str): End (<=) of time period. The period (start to end) can not exceed 1 year.
                Must be in format: YYYY-MM-DDThh:mm:ss+hh:mm (as defined by RFC 3339, section 5.6.)
            unit (Optional[str]): The SI unit of the result. A cast will occur if the base unit differs.
            ge (Optional[int]): Value should be greater or equal to (>=) this.
            le (Optional[int]): Value should be less or equal to (<=) this.
            precision (Optional[str]): Truncate all timestamps and perform aggregate operations on the grouping.
                Available values : microseconds, milliseconds, second, minute, minute5, minute10,
                minute15, minute20, minute30, hour, day, week, month, year, decade, century, millennia
            aggregate (Optional[str]): When using precision. Select this aggregate function instead of the default avg
                when computing the result. Does nothing when precision is not set.
                Available values:

                    -   avg

                    -   min

                    -   max

                    -   sum

                    -   count

            timezone (Optional[str]): Act as this time zone. Defaults to UTC.

        Returns:
            List[:class:`.TimeseriesDataPointType`]

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostNotFoundException`: The requested resource was not found.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.get(
            url=f'{self._base_url}/{self._api_version}/{self._timeseries_api_path}/{timeseries_uuid}/data',
            params=filter_none_values_from_dict({
                'start': start,
                'end': end,
                'unit': unit,
                'ge': ge,
                'le': le,
                'precision': precision,
                'aggregate': aggregate,
                'timezone': timezone
            })
        )
        return self._process_response(response)

    def create_timeseries_data(self,
                               timeseries_uuid: str,
                               data_points: List[TimeseriesDataPointType],
                               unit: Optional[str] = None
                               ) -> None:
        """Add data points to a timeseries from NODA Self-host API

        Args:
            timeseries_uuid (str): UUID of timeseries to query.
            unit (Optional[str]): The SI unit of the result. A cast will occur if the base unit differs.
            data_points (List[TimeseriesDataPointType]): A list of data points.

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostNotFoundException`: The requested resource was not found.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.post(
            url=f'{self._base_url}/{self._api_version}/{self._timeseries_api_path}/{timeseries_uuid}/data',
            params=filter_none_values_from_dict({'unit': unit}),
            json=data_points
        )
        return self._process_response(response)

    def delete_timeseries_data(self,
                               timeseries_uuid: str,
                               start: str,
                               end: str,
                               ge: Optional[int] = None,
                               le: Optional[int] = None
                               ) -> None:
        """Delete a range of timeseries data from NODA Self-host API

        Args:
            timeseries_uuid (str): UUID of timeseries to query.
            start (datetime str): Start (>=) of time period. The period (start to end) can not exceed 1 year.
                Must be in format: YYYY-MM-DDThh:mm:ss+hh:mm (as defined by RFC 3339, section 5.6.)
            end (datetime str): End (<=) of time period. The period (start to end) can not exceed 1 year.
                Must be in format: YYYY-MM-DDThh:mm:ss+hh:mm (as defined by RFC 3339, section 5.6.)
            ge (Optional[int]): Value should be greater or equal to (>=) this.
            le (Optional[int]): Value should be less or equal to (<=) this.

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostNotFoundException`: The requested resource was not found.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.delete(
            url=f'{self._base_url}/{self._api_version}/{self._timeseries_api_path}/{timeseries_uuid}/data',
            params=filter_none_values_from_dict({
                'start': start,
                'end': end,
                'ge': ge,
                'le': le
            })
        )
        return self._process_response(response)

    def get_multiple_timeseries_data(self,
                                     uuids: List[str],
                                     start: str,
                                     end: str,
                                     unit: Optional[str] = None,
                                     ge: Optional[int] = None,
                                     le: Optional[int] = None,
                                     precision: Optional[str] = None,
                                     aggregate: Optional[str] = None,
                                     timezone: Optional[str] = None
                                     ) -> List[TimeseriesDataType]:
        """Fetch multiple ranges of timeseries data from NODA Self-host API

        Args:
            uuids (List[str]): A series of timeseries UUIDs to search for.
            start (datetime str): Start (>=) of time period. The period (start to end) can not exceed 1 year.
                Must be in format: YYYY-MM-DDThh:mm:ss+hh:mm (as defined by RFC 3339, section 5.6.)
            end (datetime str): End (<=) of time period. The period (start to end) can not exceed 1 year.
                Must be in format: YYYY-MM-DDThh:mm:ss+hh:mm (as defined by RFC 3339, section 5.6.)
            unit (optional[str]): The SI unit of the result. A cast will occur if the base unit differs.
            ge (optional[int]): Value should be greater or equal to (>=) this.
            le (optional[int]): Value should be less or equal to (<=) this.
            precision (optional[str]): Truncate all timestamps and perform aggregate operations on the grouping.
                Available values : microseconds, milliseconds, second, minute, minute5, minute10,
                minute15, minute20, minute30, hour, day, week, month, year, decade, century, millennia
            aggregate (optional[str]): When using precision. Select this aggregate function instead of the default avg
                when computing the result. Does nothing when precision is not set.
                Available values:

                    -   avg

                    -   min

                    -   max

                    -   sum

                    -   count

            timezone (optional[str]): Act as this time zone. Defaults to UTC.

        Returns:
            List[:class:`.TimeseriesDataType`]

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostNotFoundException`: The requested resource was not found.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.get(
            url=f'{self._base_url}/{self._api_version}/tsquery',
            params=filter_none_values_from_dict({
                'uuids': uuids,
                'start': start,
                'end': end,
                'unit': unit,
                'ge': ge,
                'le': le,
                'precision': precision,
                'aggregate': aggregate,
                'timezone': timezone
            })
        )
        return self._process_response(response)
