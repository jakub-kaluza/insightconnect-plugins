import insightconnect_plugin_runtime
from .schema import LookupIPAddressInput, LookupIPAddressOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_recorded_future.util.util import AvailableInputs
from komand_recorded_future.util.api import Endpoint


class LookupIPAddress(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_IP_address",
            description=Component.DESCRIPTION,
            input=LookupIPAddressInput(),
            output=LookupIPAddressOutput(),
        )

    def run(self, params={}):
        comment = params.get(Input.COMMENT)
        if not comment:
            comment = None
        try:
            return {
                Output.DATA: insightconnect_plugin_runtime.helper.clean(
                    self.connection.client.make_request(
                        Endpoint.lookup_ip_address(params.get(Input.IP_ADDRESS)),
                        {"fields": AvailableInputs.IpFields, "comment": comment},
                    ).get("data")
                )
            }
        except AttributeError as e:
            raise PluginException(
                cause="Recorded Future returned unexpected response.",
                assistance="Please check that the provided inputs are correct and try again.",
                data=e,
            )
