# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['MetricsProviderArgs', 'MetricsProvider']

@pulumi.input_type
class MetricsProviderArgs:
    def __init__(__self__, *,
                 page_id: pulumi.Input[str],
                 type: pulumi.Input[str],
                 api_key: Optional[pulumi.Input[str]] = None,
                 api_token: Optional[pulumi.Input[str]] = None,
                 application_key: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 metric_base_uri: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MetricsProvider resource.
        :param pulumi.Input[str] page_id: the id of the page this component belongs to
        :param pulumi.Input[str] type: One of `Pingdom`, `NewRelic`, `Librato`, `Datadog`, or `Self`
        :param pulumi.Input[str] api_key: Required by the Datadog and NewRelic type metrics providers.
        :param pulumi.Input[str] api_token: Required by the Librato and Pingdom-type metrics provider.
        :param pulumi.Input[str] application_key: Required by the Pingdom and Datadog type metrics providers.
        :param pulumi.Input[str] email: Required by the Librato and Pingdom type metrics providers.
        :param pulumi.Input[str] metric_base_uri: Required by the NewRelic-type metrics provider
        :param pulumi.Input[str] password: Required by the Pingdom-type metrics provider.
        """
        pulumi.set(__self__, "page_id", page_id)
        pulumi.set(__self__, "type", type)
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if api_token is not None:
            pulumi.set(__self__, "api_token", api_token)
        if application_key is not None:
            pulumi.set(__self__, "application_key", application_key)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if metric_base_uri is not None:
            pulumi.set(__self__, "metric_base_uri", metric_base_uri)
        if password is not None:
            pulumi.set(__self__, "password", password)

    @property
    @pulumi.getter(name="pageId")
    def page_id(self) -> pulumi.Input[str]:
        """
        the id of the page this component belongs to
        """
        return pulumi.get(self, "page_id")

    @page_id.setter
    def page_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "page_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        One of `Pingdom`, `NewRelic`, `Librato`, `Datadog`, or `Self`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        Required by the Datadog and NewRelic type metrics providers.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="apiToken")
    def api_token(self) -> Optional[pulumi.Input[str]]:
        """
        Required by the Librato and Pingdom-type metrics provider.
        """
        return pulumi.get(self, "api_token")

    @api_token.setter
    def api_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_token", value)

    @property
    @pulumi.getter(name="applicationKey")
    def application_key(self) -> Optional[pulumi.Input[str]]:
        """
        Required by the Pingdom and Datadog type metrics providers.
        """
        return pulumi.get(self, "application_key")

    @application_key.setter
    def application_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_key", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        Required by the Librato and Pingdom type metrics providers.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="metricBaseUri")
    def metric_base_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Required by the NewRelic-type metrics provider
        """
        return pulumi.get(self, "metric_base_uri")

    @metric_base_uri.setter
    def metric_base_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_base_uri", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Required by the Pingdom-type metrics provider.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)


@pulumi.input_type
class _MetricsProviderState:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[str]] = None,
                 api_token: Optional[pulumi.Input[str]] = None,
                 application_key: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 metric_base_uri: Optional[pulumi.Input[str]] = None,
                 page_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MetricsProvider resources.
        :param pulumi.Input[str] api_key: Required by the Datadog and NewRelic type metrics providers.
        :param pulumi.Input[str] api_token: Required by the Librato and Pingdom-type metrics provider.
        :param pulumi.Input[str] application_key: Required by the Pingdom and Datadog type metrics providers.
        :param pulumi.Input[str] email: Required by the Librato and Pingdom type metrics providers.
        :param pulumi.Input[str] metric_base_uri: Required by the NewRelic-type metrics provider
        :param pulumi.Input[str] page_id: the id of the page this component belongs to
        :param pulumi.Input[str] password: Required by the Pingdom-type metrics provider.
        :param pulumi.Input[str] type: One of `Pingdom`, `NewRelic`, `Librato`, `Datadog`, or `Self`
        """
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if api_token is not None:
            pulumi.set(__self__, "api_token", api_token)
        if application_key is not None:
            pulumi.set(__self__, "application_key", application_key)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if metric_base_uri is not None:
            pulumi.set(__self__, "metric_base_uri", metric_base_uri)
        if page_id is not None:
            pulumi.set(__self__, "page_id", page_id)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        Required by the Datadog and NewRelic type metrics providers.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="apiToken")
    def api_token(self) -> Optional[pulumi.Input[str]]:
        """
        Required by the Librato and Pingdom-type metrics provider.
        """
        return pulumi.get(self, "api_token")

    @api_token.setter
    def api_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_token", value)

    @property
    @pulumi.getter(name="applicationKey")
    def application_key(self) -> Optional[pulumi.Input[str]]:
        """
        Required by the Pingdom and Datadog type metrics providers.
        """
        return pulumi.get(self, "application_key")

    @application_key.setter
    def application_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_key", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        Required by the Librato and Pingdom type metrics providers.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="metricBaseUri")
    def metric_base_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Required by the NewRelic-type metrics provider
        """
        return pulumi.get(self, "metric_base_uri")

    @metric_base_uri.setter
    def metric_base_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_base_uri", value)

    @property
    @pulumi.getter(name="pageId")
    def page_id(self) -> Optional[pulumi.Input[str]]:
        """
        the id of the page this component belongs to
        """
        return pulumi.get(self, "page_id")

    @page_id.setter
    def page_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "page_id", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Required by the Pingdom-type metrics provider.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        One of `Pingdom`, `NewRelic`, `Librato`, `Datadog`, or `Self`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class MetricsProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 api_token: Optional[pulumi.Input[str]] = None,
                 application_key: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 metric_base_uri: Optional[pulumi.Input[str]] = None,
                 page_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_statuspage as statuspage

        statuspage_pingdom = statuspage.MetricsProvider("statuspagePingdom",
            api_token="a-pingdom-api-token",
            page_id="pageid",
            type="Pingdom")
        ```

        ## Import

        `statuspage_metrics_provider` can be imported using the ID of the metrics provider, e.g.

        ```sh
        $ pulumi import statuspage:index/metricsProvider:MetricsProvider statuspage_pingdom my-page-id/my-metrics-provider-id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: Required by the Datadog and NewRelic type metrics providers.
        :param pulumi.Input[str] api_token: Required by the Librato and Pingdom-type metrics provider.
        :param pulumi.Input[str] application_key: Required by the Pingdom and Datadog type metrics providers.
        :param pulumi.Input[str] email: Required by the Librato and Pingdom type metrics providers.
        :param pulumi.Input[str] metric_base_uri: Required by the NewRelic-type metrics provider
        :param pulumi.Input[str] page_id: the id of the page this component belongs to
        :param pulumi.Input[str] password: Required by the Pingdom-type metrics provider.
        :param pulumi.Input[str] type: One of `Pingdom`, `NewRelic`, `Librato`, `Datadog`, or `Self`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MetricsProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_statuspage as statuspage

        statuspage_pingdom = statuspage.MetricsProvider("statuspagePingdom",
            api_token="a-pingdom-api-token",
            page_id="pageid",
            type="Pingdom")
        ```

        ## Import

        `statuspage_metrics_provider` can be imported using the ID of the metrics provider, e.g.

        ```sh
        $ pulumi import statuspage:index/metricsProvider:MetricsProvider statuspage_pingdom my-page-id/my-metrics-provider-id
        ```

        :param str resource_name: The name of the resource.
        :param MetricsProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MetricsProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 api_token: Optional[pulumi.Input[str]] = None,
                 application_key: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 metric_base_uri: Optional[pulumi.Input[str]] = None,
                 page_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MetricsProviderArgs.__new__(MetricsProviderArgs)

            __props__.__dict__["api_key"] = None if api_key is None else pulumi.Output.secret(api_key)
            __props__.__dict__["api_token"] = None if api_token is None else pulumi.Output.secret(api_token)
            __props__.__dict__["application_key"] = None if application_key is None else pulumi.Output.secret(application_key)
            __props__.__dict__["email"] = email
            __props__.__dict__["metric_base_uri"] = metric_base_uri
            if page_id is None and not opts.urn:
                raise TypeError("Missing required property 'page_id'")
            __props__.__dict__["page_id"] = page_id
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apiKey", "apiToken", "applicationKey", "password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(MetricsProvider, __self__).__init__(
            'statuspage:index/metricsProvider:MetricsProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_key: Optional[pulumi.Input[str]] = None,
            api_token: Optional[pulumi.Input[str]] = None,
            application_key: Optional[pulumi.Input[str]] = None,
            email: Optional[pulumi.Input[str]] = None,
            metric_base_uri: Optional[pulumi.Input[str]] = None,
            page_id: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'MetricsProvider':
        """
        Get an existing MetricsProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: Required by the Datadog and NewRelic type metrics providers.
        :param pulumi.Input[str] api_token: Required by the Librato and Pingdom-type metrics provider.
        :param pulumi.Input[str] application_key: Required by the Pingdom and Datadog type metrics providers.
        :param pulumi.Input[str] email: Required by the Librato and Pingdom type metrics providers.
        :param pulumi.Input[str] metric_base_uri: Required by the NewRelic-type metrics provider
        :param pulumi.Input[str] page_id: the id of the page this component belongs to
        :param pulumi.Input[str] password: Required by the Pingdom-type metrics provider.
        :param pulumi.Input[str] type: One of `Pingdom`, `NewRelic`, `Librato`, `Datadog`, or `Self`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MetricsProviderState.__new__(_MetricsProviderState)

        __props__.__dict__["api_key"] = api_key
        __props__.__dict__["api_token"] = api_token
        __props__.__dict__["application_key"] = application_key
        __props__.__dict__["email"] = email
        __props__.__dict__["metric_base_uri"] = metric_base_uri
        __props__.__dict__["page_id"] = page_id
        __props__.__dict__["password"] = password
        __props__.__dict__["type"] = type
        return MetricsProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[Optional[str]]:
        """
        Required by the Datadog and NewRelic type metrics providers.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="apiToken")
    def api_token(self) -> pulumi.Output[Optional[str]]:
        """
        Required by the Librato and Pingdom-type metrics provider.
        """
        return pulumi.get(self, "api_token")

    @property
    @pulumi.getter(name="applicationKey")
    def application_key(self) -> pulumi.Output[Optional[str]]:
        """
        Required by the Pingdom and Datadog type metrics providers.
        """
        return pulumi.get(self, "application_key")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[Optional[str]]:
        """
        Required by the Librato and Pingdom type metrics providers.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="metricBaseUri")
    def metric_base_uri(self) -> pulumi.Output[Optional[str]]:
        """
        Required by the NewRelic-type metrics provider
        """
        return pulumi.get(self, "metric_base_uri")

    @property
    @pulumi.getter(name="pageId")
    def page_id(self) -> pulumi.Output[str]:
        """
        the id of the page this component belongs to
        """
        return pulumi.get(self, "page_id")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        Required by the Pingdom-type metrics provider.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        One of `Pingdom`, `NewRelic`, `Librato`, `Datadog`, or `Self`
        """
        return pulumi.get(self, "type")

