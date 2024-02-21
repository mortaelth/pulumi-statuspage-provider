// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as statuspage from "@pulumi/statuspage";
 *
 * const myGroup = new statuspage.ComponentGroup("myGroup", {
 *     components: [statuspage_component.my_component.id],
 *     description: "Created by terraform",
 *     pageId: "pageid",
 * });
 * ```
 *
 * ## Import
 *
 * `statuspage_component_group` can be imported using the ID of the component group, e.g.
 *
 * ```sh
 *  $ pulumi import statuspage:index/componentGroup:ComponentGroup my_group my-page-id/my-component-group-id
 * ```
 */
export class ComponentGroup extends pulumi.CustomResource {
    /**
     * Get an existing ComponentGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ComponentGroupState, opts?: pulumi.CustomResourceOptions): ComponentGroup {
        return new ComponentGroup(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'statuspage:index/componentGroup:ComponentGroup';

    /**
     * Returns true if the given object is an instance of ComponentGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ComponentGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ComponentGroup.__pulumiType;
    }

    /**
     * List of component IDs
     */
    public readonly components!: pulumi.Output<string[]>;
    /**
     * description of the component group
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * name of the component group
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * the id of the page this component belongs to
     */
    public readonly pageId!: pulumi.Output<string>;

    /**
     * Create a ComponentGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ComponentGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ComponentGroupArgs | ComponentGroupState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ComponentGroupState | undefined;
            resourceInputs["components"] = state ? state.components : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["pageId"] = state ? state.pageId : undefined;
        } else {
            const args = argsOrState as ComponentGroupArgs | undefined;
            if ((!args || args.components === undefined) && !opts.urn) {
                throw new Error("Missing required property 'components'");
            }
            if ((!args || args.pageId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'pageId'");
            }
            resourceInputs["components"] = args ? args.components : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["pageId"] = args ? args.pageId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ComponentGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ComponentGroup resources.
 */
export interface ComponentGroupState {
    /**
     * List of component IDs
     */
    components?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * description of the component group
     */
    description?: pulumi.Input<string>;
    /**
     * name of the component group
     */
    name?: pulumi.Input<string>;
    /**
     * the id of the page this component belongs to
     */
    pageId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ComponentGroup resource.
 */
export interface ComponentGroupArgs {
    /**
     * List of component IDs
     */
    components: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * description of the component group
     */
    description?: pulumi.Input<string>;
    /**
     * name of the component group
     */
    name?: pulumi.Input<string>;
    /**
     * the id of the page this component belongs to
     */
    pageId: pulumi.Input<string>;
}