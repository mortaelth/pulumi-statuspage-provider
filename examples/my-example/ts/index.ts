import * as statuspage from "pulumi-statuspage";

export const component = new statuspage.Component("my-component", {
  pageId: "my-page",
  name: "My Component",
});

export const componentGroup = new statuspage.ComponentGroup(
  "my-component-group",
  {
    pageId: "my-page",
    name: "My Component Group",
    components: [component.id],
  }
);
