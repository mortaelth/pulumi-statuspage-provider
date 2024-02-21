#!/bin/bash

make tfgen
make build_sdks
make install_nodejs_sdk

rm -f ~/.pulumi/bin/pulumi-resource-statuspage
cp ./bin/pulumi-resource-statuspage ~/.pulumi/bin/pulumi-resource-statuspagecd 
make install_nodejs_sdk
cd examples/my-example/ts
yarn link "@pulumi/statuspage"
