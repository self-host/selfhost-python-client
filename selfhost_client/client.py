from .alerts_client import AlertsClient
from .datasets_client import DatasetsClient
from .groups_client import GroupsClient
from .policies_client import PoliciesClient
from .programs_client import ProgramsClient
from .things_client import ThingsClient
from .timeseries_client import TimeseriesClient
from .users_client import UsersClient


class SelfHostClient(
    UsersClient,
    GroupsClient,
    PoliciesClient,
    ThingsClient,
    TimeseriesClient,
    DatasetsClient,
    ProgramsClient,
    AlertsClient
):
    """
    A class for handling all sections of NODA Self-host API combined into one client
    """
    pass
