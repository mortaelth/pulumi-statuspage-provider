// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package statuspage

import (
	"context"
	"reflect"

	"errors"
	"github.com/mortaelth/pulumi-statuspage-provider/sdk/go/statuspage/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Import
//
// `statuspage_component` can be imported using the ID of the component, e.g.
//
// ```sh
// $ pulumi import statuspage:index/component:Component my_component my-page-id/my-component-id
// ```
type Component struct {
	pulumi.CustomResourceState

	// Email address to send automation events to
	AutomationEmail pulumi.StringOutput `pulumi:"automationEmail"`
	// Description of the component
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Name of the component
	Name pulumi.StringOutput `pulumi:"name"`
	// Should this component be shown component only if in degraded state
	OnlyShowIfDegraded pulumi.BoolPtrOutput `pulumi:"onlyShowIfDegraded"`
	// the id of the page this component belongs to
	PageId pulumi.StringOutput `pulumi:"pageId"`
	// Should this component be showcased
	//
	// The following attributes are exported:
	Showcase pulumi.BoolPtrOutput `pulumi:"showcase"`
	// status of the component - must be one of `operational`, `underMaintenance`, `degradedPerformance`, `partialOutage`, `majorOutage` or ` `
	Status pulumi.StringPtrOutput `pulumi:"status"`
}

// NewComponent registers a new resource with the given unique name, arguments, and options.
func NewComponent(ctx *pulumi.Context,
	name string, args *ComponentArgs, opts ...pulumi.ResourceOption) (*Component, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.PageId == nil {
		return nil, errors.New("invalid value for required argument 'PageId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Component
	err := ctx.RegisterResource("statuspage:index/component:Component", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetComponent gets an existing Component resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetComponent(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ComponentState, opts ...pulumi.ResourceOption) (*Component, error) {
	var resource Component
	err := ctx.ReadResource("statuspage:index/component:Component", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Component resources.
type componentState struct {
	// Email address to send automation events to
	AutomationEmail *string `pulumi:"automationEmail"`
	// Description of the component
	Description *string `pulumi:"description"`
	// Name of the component
	Name *string `pulumi:"name"`
	// Should this component be shown component only if in degraded state
	OnlyShowIfDegraded *bool `pulumi:"onlyShowIfDegraded"`
	// the id of the page this component belongs to
	PageId *string `pulumi:"pageId"`
	// Should this component be showcased
	//
	// The following attributes are exported:
	Showcase *bool `pulumi:"showcase"`
	// status of the component - must be one of `operational`, `underMaintenance`, `degradedPerformance`, `partialOutage`, `majorOutage` or ` `
	Status *string `pulumi:"status"`
}

type ComponentState struct {
	// Email address to send automation events to
	AutomationEmail pulumi.StringPtrInput
	// Description of the component
	Description pulumi.StringPtrInput
	// Name of the component
	Name pulumi.StringPtrInput
	// Should this component be shown component only if in degraded state
	OnlyShowIfDegraded pulumi.BoolPtrInput
	// the id of the page this component belongs to
	PageId pulumi.StringPtrInput
	// Should this component be showcased
	//
	// The following attributes are exported:
	Showcase pulumi.BoolPtrInput
	// status of the component - must be one of `operational`, `underMaintenance`, `degradedPerformance`, `partialOutage`, `majorOutage` or ` `
	Status pulumi.StringPtrInput
}

func (ComponentState) ElementType() reflect.Type {
	return reflect.TypeOf((*componentState)(nil)).Elem()
}

type componentArgs struct {
	// Description of the component
	Description *string `pulumi:"description"`
	// Name of the component
	Name *string `pulumi:"name"`
	// Should this component be shown component only if in degraded state
	OnlyShowIfDegraded *bool `pulumi:"onlyShowIfDegraded"`
	// the id of the page this component belongs to
	PageId string `pulumi:"pageId"`
	// Should this component be showcased
	//
	// The following attributes are exported:
	Showcase *bool `pulumi:"showcase"`
	// status of the component - must be one of `operational`, `underMaintenance`, `degradedPerformance`, `partialOutage`, `majorOutage` or ` `
	Status *string `pulumi:"status"`
}

// The set of arguments for constructing a Component resource.
type ComponentArgs struct {
	// Description of the component
	Description pulumi.StringPtrInput
	// Name of the component
	Name pulumi.StringPtrInput
	// Should this component be shown component only if in degraded state
	OnlyShowIfDegraded pulumi.BoolPtrInput
	// the id of the page this component belongs to
	PageId pulumi.StringInput
	// Should this component be showcased
	//
	// The following attributes are exported:
	Showcase pulumi.BoolPtrInput
	// status of the component - must be one of `operational`, `underMaintenance`, `degradedPerformance`, `partialOutage`, `majorOutage` or ` `
	Status pulumi.StringPtrInput
}

func (ComponentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*componentArgs)(nil)).Elem()
}

type ComponentInput interface {
	pulumi.Input

	ToComponentOutput() ComponentOutput
	ToComponentOutputWithContext(ctx context.Context) ComponentOutput
}

func (*Component) ElementType() reflect.Type {
	return reflect.TypeOf((**Component)(nil)).Elem()
}

func (i *Component) ToComponentOutput() ComponentOutput {
	return i.ToComponentOutputWithContext(context.Background())
}

func (i *Component) ToComponentOutputWithContext(ctx context.Context) ComponentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ComponentOutput)
}

// ComponentArrayInput is an input type that accepts ComponentArray and ComponentArrayOutput values.
// You can construct a concrete instance of `ComponentArrayInput` via:
//
//	ComponentArray{ ComponentArgs{...} }
type ComponentArrayInput interface {
	pulumi.Input

	ToComponentArrayOutput() ComponentArrayOutput
	ToComponentArrayOutputWithContext(context.Context) ComponentArrayOutput
}

type ComponentArray []ComponentInput

func (ComponentArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Component)(nil)).Elem()
}

func (i ComponentArray) ToComponentArrayOutput() ComponentArrayOutput {
	return i.ToComponentArrayOutputWithContext(context.Background())
}

func (i ComponentArray) ToComponentArrayOutputWithContext(ctx context.Context) ComponentArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ComponentArrayOutput)
}

// ComponentMapInput is an input type that accepts ComponentMap and ComponentMapOutput values.
// You can construct a concrete instance of `ComponentMapInput` via:
//
//	ComponentMap{ "key": ComponentArgs{...} }
type ComponentMapInput interface {
	pulumi.Input

	ToComponentMapOutput() ComponentMapOutput
	ToComponentMapOutputWithContext(context.Context) ComponentMapOutput
}

type ComponentMap map[string]ComponentInput

func (ComponentMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Component)(nil)).Elem()
}

func (i ComponentMap) ToComponentMapOutput() ComponentMapOutput {
	return i.ToComponentMapOutputWithContext(context.Background())
}

func (i ComponentMap) ToComponentMapOutputWithContext(ctx context.Context) ComponentMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ComponentMapOutput)
}

type ComponentOutput struct{ *pulumi.OutputState }

func (ComponentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Component)(nil)).Elem()
}

func (o ComponentOutput) ToComponentOutput() ComponentOutput {
	return o
}

func (o ComponentOutput) ToComponentOutputWithContext(ctx context.Context) ComponentOutput {
	return o
}

// Email address to send automation events to
func (o ComponentOutput) AutomationEmail() pulumi.StringOutput {
	return o.ApplyT(func(v *Component) pulumi.StringOutput { return v.AutomationEmail }).(pulumi.StringOutput)
}

// Description of the component
func (o ComponentOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Component) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Name of the component
func (o ComponentOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Component) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Should this component be shown component only if in degraded state
func (o ComponentOutput) OnlyShowIfDegraded() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Component) pulumi.BoolPtrOutput { return v.OnlyShowIfDegraded }).(pulumi.BoolPtrOutput)
}

// the id of the page this component belongs to
func (o ComponentOutput) PageId() pulumi.StringOutput {
	return o.ApplyT(func(v *Component) pulumi.StringOutput { return v.PageId }).(pulumi.StringOutput)
}

// Should this component be showcased
//
// The following attributes are exported:
func (o ComponentOutput) Showcase() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Component) pulumi.BoolPtrOutput { return v.Showcase }).(pulumi.BoolPtrOutput)
}

// status of the component - must be one of `operational`, `underMaintenance`, `degradedPerformance`, `partialOutage`, `majorOutage` or ` `
func (o ComponentOutput) Status() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Component) pulumi.StringPtrOutput { return v.Status }).(pulumi.StringPtrOutput)
}

type ComponentArrayOutput struct{ *pulumi.OutputState }

func (ComponentArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Component)(nil)).Elem()
}

func (o ComponentArrayOutput) ToComponentArrayOutput() ComponentArrayOutput {
	return o
}

func (o ComponentArrayOutput) ToComponentArrayOutputWithContext(ctx context.Context) ComponentArrayOutput {
	return o
}

func (o ComponentArrayOutput) Index(i pulumi.IntInput) ComponentOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Component {
		return vs[0].([]*Component)[vs[1].(int)]
	}).(ComponentOutput)
}

type ComponentMapOutput struct{ *pulumi.OutputState }

func (ComponentMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Component)(nil)).Elem()
}

func (o ComponentMapOutput) ToComponentMapOutput() ComponentMapOutput {
	return o
}

func (o ComponentMapOutput) ToComponentMapOutputWithContext(ctx context.Context) ComponentMapOutput {
	return o
}

func (o ComponentMapOutput) MapIndex(k pulumi.StringInput) ComponentOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Component {
		return vs[0].(map[string]*Component)[vs[1].(string)]
	}).(ComponentOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ComponentInput)(nil)).Elem(), &Component{})
	pulumi.RegisterInputType(reflect.TypeOf((*ComponentArrayInput)(nil)).Elem(), ComponentArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ComponentMapInput)(nil)).Elem(), ComponentMap{})
	pulumi.RegisterOutputType(ComponentOutput{})
	pulumi.RegisterOutputType(ComponentArrayOutput{})
	pulumi.RegisterOutputType(ComponentMapOutput{})
}
