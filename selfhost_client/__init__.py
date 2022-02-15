__version__ = '0.1.0'

import logging
from .client import SelfHostClient
from .alerts_client import AlertsClient
from .base_client import BaseClient
from .datasets_client import DatasetsClient
from .groups_client import GroupsClient
from .policies_client import PoliciesClient
from .programs_client import ProgramsClient
from .things_client import ThingsClient
from .timeseries_client import TimeseriesClient
from .users_client import UsersClient
from .exceptions import (
    SelfHostBadRequestException,
    SelfHostUnauthorizedException,
    SelfHostForbiddenException,
    SelfHostNotFoundException,
    SelfHostMethodNotAllowedException,
    SelfHostConflictException,
    SelfHostTooManyRequestsException,
    SelfHostInternalServerException,
    SelfHostFatalErrorException
)
from .types.dataset_types import DatasetType, DatasetResponse
from .types.program_types import ProgramType
from .types.timeseries_types import (
    TimeseriesType,
    TimeseriesDataType,
    TimeseriesDataPointType,
    TimeseriesDataPointResponse,
    TimeseriesDataResponse
)
from .types.thing_types import ThingType
from .types.user_types import UserType, UserTokenType, CreatedUserTokenResponse, UserTokenResponse
from .types.group_types import GroupType
from .types.policy_types import PolicyType
from .types.alert_types import AlertType, CreatedAlertResponse, AlertResponse

logging.getLogger(__name__).addHandler(logging.NullHandler())
