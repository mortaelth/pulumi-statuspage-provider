// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package statuspage

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/mortaelth/pulumi-statuspage-provider/sdk/go/statuspage/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "statuspage:index/component:Component":
		r = &Component{}
	case "statuspage:index/componentGroup:ComponentGroup":
		r = &ComponentGroup{}
	case "statuspage:index/metric:Metric":
		r = &Metric{}
	case "statuspage:index/metricsProvider:MetricsProvider":
		r = &MetricsProvider{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:statuspage" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	r := &Provider{}
	err := ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return r, err
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"statuspage",
		"index/component",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"statuspage",
		"index/componentGroup",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"statuspage",
		"index/metric",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"statuspage",
		"index/metricsProvider",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"statuspage",
		&pkg{version},
	)
}