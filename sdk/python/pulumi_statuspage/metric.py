# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['MetricArgs', 'Metric']

@pulumi.input_type
class MetricArgs:
    def __init__(__self__, *,
                 metrics_provider_id: pulumi.Input[str],
                 page_id: pulumi.Input[str],
                 decimal_places: Optional[pulumi.Input[int]] = None,
                 display: Optional[pulumi.Input[bool]] = None,
                 metric_identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 suffix: Optional[pulumi.Input[str]] = None,
                 tooltip_description: Optional[pulumi.Input[str]] = None,
                 transform: Optional[pulumi.Input[str]] = None,
                 y_axis_hidden: Optional[pulumi.Input[bool]] = None,
                 y_axis_max: Optional[pulumi.Input[float]] = None,
                 y_axis_min: Optional[pulumi.Input[float]] = None):
        """
        The set of arguments for constructing a Metric resource.
        :param pulumi.Input[str] metrics_provider_id: ID of the metric provider
        :param pulumi.Input[str] page_id: The ID of the page this metric belongs to
        :param pulumi.Input[int] decimal_places: How many decimal places to render on the graph
        :param pulumi.Input[bool] display: Should the metric be displayed
        :param pulumi.Input[str] metric_identifier: The identifier used to look up the metric data from the provider
        :param pulumi.Input[str] name: Display name for the metric
        :param pulumi.Input[str] suffix: Suffix to describe the units on the graph
        :param pulumi.Input[str] tooltip_description: Tooltip for the metric
        :param pulumi.Input[str] transform: The transform to apply to metric before pulling into Statuspage. One of: 'average', 'count', 'max', 'min', 'sum',
               'response_time' or 'uptime'
        :param pulumi.Input[bool] y_axis_hidden: Should the values on the y axis be hidden on render
        :param pulumi.Input[float] y_axis_max: The upper bound of the y axis
        :param pulumi.Input[float] y_axis_min: The lower bound of the y axis
        """
        pulumi.set(__self__, "metrics_provider_id", metrics_provider_id)
        pulumi.set(__self__, "page_id", page_id)
        if decimal_places is not None:
            pulumi.set(__self__, "decimal_places", decimal_places)
        if display is not None:
            pulumi.set(__self__, "display", display)
        if metric_identifier is not None:
            pulumi.set(__self__, "metric_identifier", metric_identifier)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if suffix is not None:
            pulumi.set(__self__, "suffix", suffix)
        if tooltip_description is not None:
            pulumi.set(__self__, "tooltip_description", tooltip_description)
        if transform is not None:
            pulumi.set(__self__, "transform", transform)
        if y_axis_hidden is not None:
            pulumi.set(__self__, "y_axis_hidden", y_axis_hidden)
        if y_axis_max is not None:
            pulumi.set(__self__, "y_axis_max", y_axis_max)
        if y_axis_min is not None:
            pulumi.set(__self__, "y_axis_min", y_axis_min)

    @property
    @pulumi.getter(name="metricsProviderId")
    def metrics_provider_id(self) -> pulumi.Input[str]:
        """
        ID of the metric provider
        """
        return pulumi.get(self, "metrics_provider_id")

    @metrics_provider_id.setter
    def metrics_provider_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "metrics_provider_id", value)

    @property
    @pulumi.getter(name="pageId")
    def page_id(self) -> pulumi.Input[str]:
        """
        The ID of the page this metric belongs to
        """
        return pulumi.get(self, "page_id")

    @page_id.setter
    def page_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "page_id", value)

    @property
    @pulumi.getter(name="decimalPlaces")
    def decimal_places(self) -> Optional[pulumi.Input[int]]:
        """
        How many decimal places to render on the graph
        """
        return pulumi.get(self, "decimal_places")

    @decimal_places.setter
    def decimal_places(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "decimal_places", value)

    @property
    @pulumi.getter
    def display(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the metric be displayed
        """
        return pulumi.get(self, "display")

    @display.setter
    def display(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "display", value)

    @property
    @pulumi.getter(name="metricIdentifier")
    def metric_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier used to look up the metric data from the provider
        """
        return pulumi.get(self, "metric_identifier")

    @metric_identifier.setter
    def metric_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_identifier", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name for the metric
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[str]]:
        """
        Suffix to describe the units on the graph
        """
        return pulumi.get(self, "suffix")

    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "suffix", value)

    @property
    @pulumi.getter(name="tooltipDescription")
    def tooltip_description(self) -> Optional[pulumi.Input[str]]:
        """
        Tooltip for the metric
        """
        return pulumi.get(self, "tooltip_description")

    @tooltip_description.setter
    def tooltip_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tooltip_description", value)

    @property
    @pulumi.getter
    def transform(self) -> Optional[pulumi.Input[str]]:
        """
        The transform to apply to metric before pulling into Statuspage. One of: 'average', 'count', 'max', 'min', 'sum',
        'response_time' or 'uptime'
        """
        return pulumi.get(self, "transform")

    @transform.setter
    def transform(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transform", value)

    @property
    @pulumi.getter(name="yAxisHidden")
    def y_axis_hidden(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the values on the y axis be hidden on render
        """
        return pulumi.get(self, "y_axis_hidden")

    @y_axis_hidden.setter
    def y_axis_hidden(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "y_axis_hidden", value)

    @property
    @pulumi.getter(name="yAxisMax")
    def y_axis_max(self) -> Optional[pulumi.Input[float]]:
        """
        The upper bound of the y axis
        """
        return pulumi.get(self, "y_axis_max")

    @y_axis_max.setter
    def y_axis_max(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "y_axis_max", value)

    @property
    @pulumi.getter(name="yAxisMin")
    def y_axis_min(self) -> Optional[pulumi.Input[float]]:
        """
        The lower bound of the y axis
        """
        return pulumi.get(self, "y_axis_min")

    @y_axis_min.setter
    def y_axis_min(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "y_axis_min", value)


@pulumi.input_type
class _MetricState:
    def __init__(__self__, *,
                 decimal_places: Optional[pulumi.Input[int]] = None,
                 display: Optional[pulumi.Input[bool]] = None,
                 metric_identifier: Optional[pulumi.Input[str]] = None,
                 metrics_provider_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 page_id: Optional[pulumi.Input[str]] = None,
                 suffix: Optional[pulumi.Input[str]] = None,
                 tooltip_description: Optional[pulumi.Input[str]] = None,
                 transform: Optional[pulumi.Input[str]] = None,
                 y_axis_hidden: Optional[pulumi.Input[bool]] = None,
                 y_axis_max: Optional[pulumi.Input[float]] = None,
                 y_axis_min: Optional[pulumi.Input[float]] = None):
        """
        Input properties used for looking up and filtering Metric resources.
        :param pulumi.Input[int] decimal_places: How many decimal places to render on the graph
        :param pulumi.Input[bool] display: Should the metric be displayed
        :param pulumi.Input[str] metric_identifier: The identifier used to look up the metric data from the provider
        :param pulumi.Input[str] metrics_provider_id: ID of the metric provider
        :param pulumi.Input[str] name: Display name for the metric
        :param pulumi.Input[str] page_id: The ID of the page this metric belongs to
        :param pulumi.Input[str] suffix: Suffix to describe the units on the graph
        :param pulumi.Input[str] tooltip_description: Tooltip for the metric
        :param pulumi.Input[str] transform: The transform to apply to metric before pulling into Statuspage. One of: 'average', 'count', 'max', 'min', 'sum',
               'response_time' or 'uptime'
        :param pulumi.Input[bool] y_axis_hidden: Should the values on the y axis be hidden on render
        :param pulumi.Input[float] y_axis_max: The upper bound of the y axis
        :param pulumi.Input[float] y_axis_min: The lower bound of the y axis
        """
        if decimal_places is not None:
            pulumi.set(__self__, "decimal_places", decimal_places)
        if display is not None:
            pulumi.set(__self__, "display", display)
        if metric_identifier is not None:
            pulumi.set(__self__, "metric_identifier", metric_identifier)
        if metrics_provider_id is not None:
            pulumi.set(__self__, "metrics_provider_id", metrics_provider_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if page_id is not None:
            pulumi.set(__self__, "page_id", page_id)
        if suffix is not None:
            pulumi.set(__self__, "suffix", suffix)
        if tooltip_description is not None:
            pulumi.set(__self__, "tooltip_description", tooltip_description)
        if transform is not None:
            pulumi.set(__self__, "transform", transform)
        if y_axis_hidden is not None:
            pulumi.set(__self__, "y_axis_hidden", y_axis_hidden)
        if y_axis_max is not None:
            pulumi.set(__self__, "y_axis_max", y_axis_max)
        if y_axis_min is not None:
            pulumi.set(__self__, "y_axis_min", y_axis_min)

    @property
    @pulumi.getter(name="decimalPlaces")
    def decimal_places(self) -> Optional[pulumi.Input[int]]:
        """
        How many decimal places to render on the graph
        """
        return pulumi.get(self, "decimal_places")

    @decimal_places.setter
    def decimal_places(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "decimal_places", value)

    @property
    @pulumi.getter
    def display(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the metric be displayed
        """
        return pulumi.get(self, "display")

    @display.setter
    def display(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "display", value)

    @property
    @pulumi.getter(name="metricIdentifier")
    def metric_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier used to look up the metric data from the provider
        """
        return pulumi.get(self, "metric_identifier")

    @metric_identifier.setter
    def metric_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_identifier", value)

    @property
    @pulumi.getter(name="metricsProviderId")
    def metrics_provider_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the metric provider
        """
        return pulumi.get(self, "metrics_provider_id")

    @metrics_provider_id.setter
    def metrics_provider_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metrics_provider_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name for the metric
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="pageId")
    def page_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the page this metric belongs to
        """
        return pulumi.get(self, "page_id")

    @page_id.setter
    def page_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "page_id", value)

    @property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[str]]:
        """
        Suffix to describe the units on the graph
        """
        return pulumi.get(self, "suffix")

    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "suffix", value)

    @property
    @pulumi.getter(name="tooltipDescription")
    def tooltip_description(self) -> Optional[pulumi.Input[str]]:
        """
        Tooltip for the metric
        """
        return pulumi.get(self, "tooltip_description")

    @tooltip_description.setter
    def tooltip_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tooltip_description", value)

    @property
    @pulumi.getter
    def transform(self) -> Optional[pulumi.Input[str]]:
        """
        The transform to apply to metric before pulling into Statuspage. One of: 'average', 'count', 'max', 'min', 'sum',
        'response_time' or 'uptime'
        """
        return pulumi.get(self, "transform")

    @transform.setter
    def transform(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transform", value)

    @property
    @pulumi.getter(name="yAxisHidden")
    def y_axis_hidden(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the values on the y axis be hidden on render
        """
        return pulumi.get(self, "y_axis_hidden")

    @y_axis_hidden.setter
    def y_axis_hidden(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "y_axis_hidden", value)

    @property
    @pulumi.getter(name="yAxisMax")
    def y_axis_max(self) -> Optional[pulumi.Input[float]]:
        """
        The upper bound of the y axis
        """
        return pulumi.get(self, "y_axis_max")

    @y_axis_max.setter
    def y_axis_max(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "y_axis_max", value)

    @property
    @pulumi.getter(name="yAxisMin")
    def y_axis_min(self) -> Optional[pulumi.Input[float]]:
        """
        The lower bound of the y axis
        """
        return pulumi.get(self, "y_axis_min")

    @y_axis_min.setter
    def y_axis_min(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "y_axis_min", value)


class Metric(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 decimal_places: Optional[pulumi.Input[int]] = None,
                 display: Optional[pulumi.Input[bool]] = None,
                 metric_identifier: Optional[pulumi.Input[str]] = None,
                 metrics_provider_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 page_id: Optional[pulumi.Input[str]] = None,
                 suffix: Optional[pulumi.Input[str]] = None,
                 tooltip_description: Optional[pulumi.Input[str]] = None,
                 transform: Optional[pulumi.Input[str]] = None,
                 y_axis_hidden: Optional[pulumi.Input[bool]] = None,
                 y_axis_max: Optional[pulumi.Input[float]] = None,
                 y_axis_min: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        """
        Create a Metric resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] decimal_places: How many decimal places to render on the graph
        :param pulumi.Input[bool] display: Should the metric be displayed
        :param pulumi.Input[str] metric_identifier: The identifier used to look up the metric data from the provider
        :param pulumi.Input[str] metrics_provider_id: ID of the metric provider
        :param pulumi.Input[str] name: Display name for the metric
        :param pulumi.Input[str] page_id: The ID of the page this metric belongs to
        :param pulumi.Input[str] suffix: Suffix to describe the units on the graph
        :param pulumi.Input[str] tooltip_description: Tooltip for the metric
        :param pulumi.Input[str] transform: The transform to apply to metric before pulling into Statuspage. One of: 'average', 'count', 'max', 'min', 'sum',
               'response_time' or 'uptime'
        :param pulumi.Input[bool] y_axis_hidden: Should the values on the y axis be hidden on render
        :param pulumi.Input[float] y_axis_max: The upper bound of the y axis
        :param pulumi.Input[float] y_axis_min: The lower bound of the y axis
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MetricArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Metric resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param MetricArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MetricArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 decimal_places: Optional[pulumi.Input[int]] = None,
                 display: Optional[pulumi.Input[bool]] = None,
                 metric_identifier: Optional[pulumi.Input[str]] = None,
                 metrics_provider_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 page_id: Optional[pulumi.Input[str]] = None,
                 suffix: Optional[pulumi.Input[str]] = None,
                 tooltip_description: Optional[pulumi.Input[str]] = None,
                 transform: Optional[pulumi.Input[str]] = None,
                 y_axis_hidden: Optional[pulumi.Input[bool]] = None,
                 y_axis_max: Optional[pulumi.Input[float]] = None,
                 y_axis_min: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MetricArgs.__new__(MetricArgs)

            __props__.__dict__["decimal_places"] = decimal_places
            __props__.__dict__["display"] = display
            __props__.__dict__["metric_identifier"] = metric_identifier
            if metrics_provider_id is None and not opts.urn:
                raise TypeError("Missing required property 'metrics_provider_id'")
            __props__.__dict__["metrics_provider_id"] = metrics_provider_id
            __props__.__dict__["name"] = name
            if page_id is None and not opts.urn:
                raise TypeError("Missing required property 'page_id'")
            __props__.__dict__["page_id"] = page_id
            __props__.__dict__["suffix"] = suffix
            __props__.__dict__["tooltip_description"] = tooltip_description
            __props__.__dict__["transform"] = transform
            __props__.__dict__["y_axis_hidden"] = y_axis_hidden
            __props__.__dict__["y_axis_max"] = y_axis_max
            __props__.__dict__["y_axis_min"] = y_axis_min
        super(Metric, __self__).__init__(
            'statuspage:index/metric:Metric',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            decimal_places: Optional[pulumi.Input[int]] = None,
            display: Optional[pulumi.Input[bool]] = None,
            metric_identifier: Optional[pulumi.Input[str]] = None,
            metrics_provider_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            page_id: Optional[pulumi.Input[str]] = None,
            suffix: Optional[pulumi.Input[str]] = None,
            tooltip_description: Optional[pulumi.Input[str]] = None,
            transform: Optional[pulumi.Input[str]] = None,
            y_axis_hidden: Optional[pulumi.Input[bool]] = None,
            y_axis_max: Optional[pulumi.Input[float]] = None,
            y_axis_min: Optional[pulumi.Input[float]] = None) -> 'Metric':
        """
        Get an existing Metric resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] decimal_places: How many decimal places to render on the graph
        :param pulumi.Input[bool] display: Should the metric be displayed
        :param pulumi.Input[str] metric_identifier: The identifier used to look up the metric data from the provider
        :param pulumi.Input[str] metrics_provider_id: ID of the metric provider
        :param pulumi.Input[str] name: Display name for the metric
        :param pulumi.Input[str] page_id: The ID of the page this metric belongs to
        :param pulumi.Input[str] suffix: Suffix to describe the units on the graph
        :param pulumi.Input[str] tooltip_description: Tooltip for the metric
        :param pulumi.Input[str] transform: The transform to apply to metric before pulling into Statuspage. One of: 'average', 'count', 'max', 'min', 'sum',
               'response_time' or 'uptime'
        :param pulumi.Input[bool] y_axis_hidden: Should the values on the y axis be hidden on render
        :param pulumi.Input[float] y_axis_max: The upper bound of the y axis
        :param pulumi.Input[float] y_axis_min: The lower bound of the y axis
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MetricState.__new__(_MetricState)

        __props__.__dict__["decimal_places"] = decimal_places
        __props__.__dict__["display"] = display
        __props__.__dict__["metric_identifier"] = metric_identifier
        __props__.__dict__["metrics_provider_id"] = metrics_provider_id
        __props__.__dict__["name"] = name
        __props__.__dict__["page_id"] = page_id
        __props__.__dict__["suffix"] = suffix
        __props__.__dict__["tooltip_description"] = tooltip_description
        __props__.__dict__["transform"] = transform
        __props__.__dict__["y_axis_hidden"] = y_axis_hidden
        __props__.__dict__["y_axis_max"] = y_axis_max
        __props__.__dict__["y_axis_min"] = y_axis_min
        return Metric(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="decimalPlaces")
    def decimal_places(self) -> pulumi.Output[Optional[int]]:
        """
        How many decimal places to render on the graph
        """
        return pulumi.get(self, "decimal_places")

    @property
    @pulumi.getter
    def display(self) -> pulumi.Output[Optional[bool]]:
        """
        Should the metric be displayed
        """
        return pulumi.get(self, "display")

    @property
    @pulumi.getter(name="metricIdentifier")
    def metric_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier used to look up the metric data from the provider
        """
        return pulumi.get(self, "metric_identifier")

    @property
    @pulumi.getter(name="metricsProviderId")
    def metrics_provider_id(self) -> pulumi.Output[str]:
        """
        ID of the metric provider
        """
        return pulumi.get(self, "metrics_provider_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Display name for the metric
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pageId")
    def page_id(self) -> pulumi.Output[str]:
        """
        The ID of the page this metric belongs to
        """
        return pulumi.get(self, "page_id")

    @property
    @pulumi.getter
    def suffix(self) -> pulumi.Output[Optional[str]]:
        """
        Suffix to describe the units on the graph
        """
        return pulumi.get(self, "suffix")

    @property
    @pulumi.getter(name="tooltipDescription")
    def tooltip_description(self) -> pulumi.Output[Optional[str]]:
        """
        Tooltip for the metric
        """
        return pulumi.get(self, "tooltip_description")

    @property
    @pulumi.getter
    def transform(self) -> pulumi.Output[Optional[str]]:
        """
        The transform to apply to metric before pulling into Statuspage. One of: 'average', 'count', 'max', 'min', 'sum',
        'response_time' or 'uptime'
        """
        return pulumi.get(self, "transform")

    @property
    @pulumi.getter(name="yAxisHidden")
    def y_axis_hidden(self) -> pulumi.Output[Optional[bool]]:
        """
        Should the values on the y axis be hidden on render
        """
        return pulumi.get(self, "y_axis_hidden")

    @property
    @pulumi.getter(name="yAxisMax")
    def y_axis_max(self) -> pulumi.Output[Optional[float]]:
        """
        The upper bound of the y axis
        """
        return pulumi.get(self, "y_axis_max")

    @property
    @pulumi.getter(name="yAxisMin")
    def y_axis_min(self) -> pulumi.Output[Optional[float]]:
        """
        The lower bound of the y axis
        """
        return pulumi.get(self, "y_axis_min")
