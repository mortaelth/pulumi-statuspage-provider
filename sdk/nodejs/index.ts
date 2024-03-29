// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { ComponentArgs, ComponentState } from "./component";
export type Component = import("./component").Component;
export const Component: typeof import("./component").Component = null as any;
utilities.lazyLoad(exports, ["Component"], () => require("./component"));

export { ComponentGroupArgs, ComponentGroupState } from "./componentGroup";
export type ComponentGroup = import("./componentGroup").ComponentGroup;
export const ComponentGroup: typeof import("./componentGroup").ComponentGroup = null as any;
utilities.lazyLoad(exports, ["ComponentGroup"], () => require("./componentGroup"));

export { MetricArgs, MetricState } from "./metric";
export type Metric = import("./metric").Metric;
export const Metric: typeof import("./metric").Metric = null as any;
utilities.lazyLoad(exports, ["Metric"], () => require("./metric"));

export { MetricsProviderArgs, MetricsProviderState } from "./metricsProvider";
export type MetricsProvider = import("./metricsProvider").MetricsProvider;
export const MetricsProvider: typeof import("./metricsProvider").MetricsProvider = null as any;
utilities.lazyLoad(exports, ["MetricsProvider"], () => require("./metricsProvider"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));


// Export sub-modules:
import * as config from "./config";

export {
    config,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "statuspage:index/component:Component":
                return new Component(name, <any>undefined, { urn })
            case "statuspage:index/componentGroup:ComponentGroup":
                return new ComponentGroup(name, <any>undefined, { urn })
            case "statuspage:index/metric:Metric":
                return new Metric(name, <any>undefined, { urn })
            case "statuspage:index/metricsProvider:MetricsProvider":
                return new MetricsProvider(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("statuspage", "index/component", _module)
pulumi.runtime.registerResourceModule("statuspage", "index/componentGroup", _module)
pulumi.runtime.registerResourceModule("statuspage", "index/metric", _module)
pulumi.runtime.registerResourceModule("statuspage", "index/metricsProvider", _module)
pulumi.runtime.registerResourcePackage("statuspage", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:statuspage") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
