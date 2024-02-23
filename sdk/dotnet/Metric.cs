// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Statuspage
{
    [StatuspageResourceType("statuspage:index/metric:Metric")]
    public partial class Metric : global::Pulumi.CustomResource
    {
        /// <summary>
        /// How many decimal places to render on the graph
        /// </summary>
        [Output("decimalPlaces")]
        public Output<int?> DecimalPlaces { get; private set; } = null!;

        /// <summary>
        /// Should the metric be displayed
        /// </summary>
        [Output("display")]
        public Output<bool?> Display { get; private set; } = null!;

        /// <summary>
        /// The identifier used to look up the metric data from the provider
        /// </summary>
        [Output("metricIdentifier")]
        public Output<string?> MetricIdentifier { get; private set; } = null!;

        /// <summary>
        /// ID of the metric provider
        /// </summary>
        [Output("metricsProviderId")]
        public Output<string> MetricsProviderId { get; private set; } = null!;

        /// <summary>
        /// Display name for the metric
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the page this metric belongs to
        /// </summary>
        [Output("pageId")]
        public Output<string> PageId { get; private set; } = null!;

        /// <summary>
        /// Suffix to describe the units on the graph
        /// </summary>
        [Output("suffix")]
        public Output<string?> Suffix { get; private set; } = null!;

        /// <summary>
        /// Tooltip for the metric
        /// </summary>
        [Output("tooltipDescription")]
        public Output<string?> TooltipDescription { get; private set; } = null!;

        /// <summary>
        /// The transform to apply to metric before pulling into Statuspage. One of: 'average', 'count', 'max', 'min', 'sum',
        /// 'response_time' or 'uptime'
        /// </summary>
        [Output("transform")]
        public Output<string?> Transform { get; private set; } = null!;

        /// <summary>
        /// Should the values on the y axis be hidden on render
        /// </summary>
        [Output("yAxisHidden")]
        public Output<bool?> YAxisHidden { get; private set; } = null!;

        /// <summary>
        /// The upper bound of the y axis
        /// </summary>
        [Output("yAxisMax")]
        public Output<double?> YAxisMax { get; private set; } = null!;

        /// <summary>
        /// The lower bound of the y axis
        /// </summary>
        [Output("yAxisMin")]
        public Output<double?> YAxisMin { get; private set; } = null!;


        /// <summary>
        /// Create a Metric resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Metric(string name, MetricArgs args, CustomResourceOptions? options = null)
            : base("statuspage:index/metric:Metric", name, args ?? new MetricArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Metric(string name, Input<string> id, MetricState? state = null, CustomResourceOptions? options = null)
            : base("statuspage:index/metric:Metric", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/mortaelth/pulumi-statuspage-provider/releases/",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Metric resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Metric Get(string name, Input<string> id, MetricState? state = null, CustomResourceOptions? options = null)
        {
            return new Metric(name, id, state, options);
        }
    }

    public sealed class MetricArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// How many decimal places to render on the graph
        /// </summary>
        [Input("decimalPlaces")]
        public Input<int>? DecimalPlaces { get; set; }

        /// <summary>
        /// Should the metric be displayed
        /// </summary>
        [Input("display")]
        public Input<bool>? Display { get; set; }

        /// <summary>
        /// The identifier used to look up the metric data from the provider
        /// </summary>
        [Input("metricIdentifier")]
        public Input<string>? MetricIdentifier { get; set; }

        /// <summary>
        /// ID of the metric provider
        /// </summary>
        [Input("metricsProviderId", required: true)]
        public Input<string> MetricsProviderId { get; set; } = null!;

        /// <summary>
        /// Display name for the metric
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the page this metric belongs to
        /// </summary>
        [Input("pageId", required: true)]
        public Input<string> PageId { get; set; } = null!;

        /// <summary>
        /// Suffix to describe the units on the graph
        /// </summary>
        [Input("suffix")]
        public Input<string>? Suffix { get; set; }

        /// <summary>
        /// Tooltip for the metric
        /// </summary>
        [Input("tooltipDescription")]
        public Input<string>? TooltipDescription { get; set; }

        /// <summary>
        /// The transform to apply to metric before pulling into Statuspage. One of: 'average', 'count', 'max', 'min', 'sum',
        /// 'response_time' or 'uptime'
        /// </summary>
        [Input("transform")]
        public Input<string>? Transform { get; set; }

        /// <summary>
        /// Should the values on the y axis be hidden on render
        /// </summary>
        [Input("yAxisHidden")]
        public Input<bool>? YAxisHidden { get; set; }

        /// <summary>
        /// The upper bound of the y axis
        /// </summary>
        [Input("yAxisMax")]
        public Input<double>? YAxisMax { get; set; }

        /// <summary>
        /// The lower bound of the y axis
        /// </summary>
        [Input("yAxisMin")]
        public Input<double>? YAxisMin { get; set; }

        public MetricArgs()
        {
        }
        public static new MetricArgs Empty => new MetricArgs();
    }

    public sealed class MetricState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// How many decimal places to render on the graph
        /// </summary>
        [Input("decimalPlaces")]
        public Input<int>? DecimalPlaces { get; set; }

        /// <summary>
        /// Should the metric be displayed
        /// </summary>
        [Input("display")]
        public Input<bool>? Display { get; set; }

        /// <summary>
        /// The identifier used to look up the metric data from the provider
        /// </summary>
        [Input("metricIdentifier")]
        public Input<string>? MetricIdentifier { get; set; }

        /// <summary>
        /// ID of the metric provider
        /// </summary>
        [Input("metricsProviderId")]
        public Input<string>? MetricsProviderId { get; set; }

        /// <summary>
        /// Display name for the metric
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the page this metric belongs to
        /// </summary>
        [Input("pageId")]
        public Input<string>? PageId { get; set; }

        /// <summary>
        /// Suffix to describe the units on the graph
        /// </summary>
        [Input("suffix")]
        public Input<string>? Suffix { get; set; }

        /// <summary>
        /// Tooltip for the metric
        /// </summary>
        [Input("tooltipDescription")]
        public Input<string>? TooltipDescription { get; set; }

        /// <summary>
        /// The transform to apply to metric before pulling into Statuspage. One of: 'average', 'count', 'max', 'min', 'sum',
        /// 'response_time' or 'uptime'
        /// </summary>
        [Input("transform")]
        public Input<string>? Transform { get; set; }

        /// <summary>
        /// Should the values on the y axis be hidden on render
        /// </summary>
        [Input("yAxisHidden")]
        public Input<bool>? YAxisHidden { get; set; }

        /// <summary>
        /// The upper bound of the y axis
        /// </summary>
        [Input("yAxisMax")]
        public Input<double>? YAxisMax { get; set; }

        /// <summary>
        /// The lower bound of the y axis
        /// </summary>
        [Input("yAxisMin")]
        public Input<double>? YAxisMin { get; set; }

        public MetricState()
        {
        }
        public static new MetricState Empty => new MetricState();
    }
}
