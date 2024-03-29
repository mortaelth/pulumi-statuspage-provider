// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as statuspage from "pulumi-statuspage";
 *
 * const statuspagePingdom = new statuspage.MetricsProvider("statuspagePingdom", {
 *     apiToken: "a-pingdom-api-token",
 *     pageId: "pageid",
 *     type: "Pingdom",
 * });
 * ```
 *
 * ## Import
 *
 * `statuspage_metrics_provider` can be imported using the ID of the metrics provider, e.g.
 *
 * ```sh
 * $ pulumi import statuspage:index/metricsProvider:MetricsProvider statuspage_pingdom my-page-id/my-metrics-provider-id
 * ```
 */
export class MetricsProvider extends pulumi.CustomResource {
    /**
     * Get an existing MetricsProvider resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MetricsProviderState, opts?: pulumi.CustomResourceOptions): MetricsProvider {
        return new MetricsProvider(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'statuspage:index/metricsProvider:MetricsProvider';

    /**
     * Returns true if the given object is an instance of MetricsProvider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MetricsProvider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MetricsProvider.__pulumiType;
    }

    /**
     * Required by the Datadog and NewRelic type metrics providers.
     */
    public readonly apiKey!: pulumi.Output<string | undefined>;
    /**
     * Required by the Librato and Pingdom-type metrics provider.
     */
    public readonly apiToken!: pulumi.Output<string | undefined>;
    /**
     * Required by the Pingdom and Datadog type metrics providers.
     */
    public readonly applicationKey!: pulumi.Output<string | undefined>;
    /**
     * Required by the Librato and Pingdom type metrics providers.
     */
    public readonly email!: pulumi.Output<string | undefined>;
    /**
     * Required by the NewRelic-type metrics provider
     */
    public readonly metricBaseUri!: pulumi.Output<string | undefined>;
    /**
     * the id of the page this component belongs to
     */
    public readonly pageId!: pulumi.Output<string>;
    /**
     * Required by the Pingdom-type metrics provider.
     */
    public readonly password!: pulumi.Output<string | undefined>;
    /**
     * One of `Pingdom`, `NewRelic`, `Librato`, `Datadog`, or `Self`
     */
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a MetricsProvider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MetricsProviderArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MetricsProviderArgs | MetricsProviderState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as MetricsProviderState | undefined;
            resourceInputs["apiKey"] = state ? state.apiKey : undefined;
            resourceInputs["apiToken"] = state ? state.apiToken : undefined;
            resourceInputs["applicationKey"] = state ? state.applicationKey : undefined;
            resourceInputs["email"] = state ? state.email : undefined;
            resourceInputs["metricBaseUri"] = state ? state.metricBaseUri : undefined;
            resourceInputs["pageId"] = state ? state.pageId : undefined;
            resourceInputs["password"] = state ? state.password : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as MetricsProviderArgs | undefined;
            if ((!args || args.pageId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'pageId'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["apiKey"] = args?.apiKey ? pulumi.secret(args.apiKey) : undefined;
            resourceInputs["apiToken"] = args?.apiToken ? pulumi.secret(args.apiToken) : undefined;
            resourceInputs["applicationKey"] = args?.applicationKey ? pulumi.secret(args.applicationKey) : undefined;
            resourceInputs["email"] = args ? args.email : undefined;
            resourceInputs["metricBaseUri"] = args ? args.metricBaseUri : undefined;
            resourceInputs["pageId"] = args ? args.pageId : undefined;
            resourceInputs["password"] = args?.password ? pulumi.secret(args.password) : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["apiKey", "apiToken", "applicationKey", "password"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(MetricsProvider.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MetricsProvider resources.
 */
export interface MetricsProviderState {
    /**
     * Required by the Datadog and NewRelic type metrics providers.
     */
    apiKey?: pulumi.Input<string>;
    /**
     * Required by the Librato and Pingdom-type metrics provider.
     */
    apiToken?: pulumi.Input<string>;
    /**
     * Required by the Pingdom and Datadog type metrics providers.
     */
    applicationKey?: pulumi.Input<string>;
    /**
     * Required by the Librato and Pingdom type metrics providers.
     */
    email?: pulumi.Input<string>;
    /**
     * Required by the NewRelic-type metrics provider
     */
    metricBaseUri?: pulumi.Input<string>;
    /**
     * the id of the page this component belongs to
     */
    pageId?: pulumi.Input<string>;
    /**
     * Required by the Pingdom-type metrics provider.
     */
    password?: pulumi.Input<string>;
    /**
     * One of `Pingdom`, `NewRelic`, `Librato`, `Datadog`, or `Self`
     */
    type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a MetricsProvider resource.
 */
export interface MetricsProviderArgs {
    /**
     * Required by the Datadog and NewRelic type metrics providers.
     */
    apiKey?: pulumi.Input<string>;
    /**
     * Required by the Librato and Pingdom-type metrics provider.
     */
    apiToken?: pulumi.Input<string>;
    /**
     * Required by the Pingdom and Datadog type metrics providers.
     */
    applicationKey?: pulumi.Input<string>;
    /**
     * Required by the Librato and Pingdom type metrics providers.
     */
    email?: pulumi.Input<string>;
    /**
     * Required by the NewRelic-type metrics provider
     */
    metricBaseUri?: pulumi.Input<string>;
    /**
     * the id of the page this component belongs to
     */
    pageId: pulumi.Input<string>;
    /**
     * Required by the Pingdom-type metrics provider.
     */
    password?: pulumi.Input<string>;
    /**
     * One of `Pingdom`, `NewRelic`, `Librato`, `Datadog`, or `Self`
     */
    type: pulumi.Input<string>;
}
