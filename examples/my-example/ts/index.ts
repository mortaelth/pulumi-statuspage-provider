import * as statuspage from "pulumi-statuspage";
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
const pageId = config.require("pageId");

export const component = new statuspage.Component("my-component", {
  name: "[ci-test]",
  pageId,
});

export const componentGroup = new statuspage.ComponentGroup(
  "my-component-group",
  {
    name: "[ci-test-group]",
    pageId,
    components: [component.id],
  }
);
