import { ComponentMeta, ComponentStory } from "@storybook/react";

import Products from "./Products";
import { GlobalContextProvider } from "../contexts/GlobalContext";
import StoreFixture from "../test-utils/StoreFixture";

export default {
  title: "Components/Products",
  component: Products,
} as ComponentMeta<typeof Products>;

const Template: ComponentStory<typeof Products> = (args) => (
  <GlobalContextProvider>
    <Products {...args} />
  </GlobalContextProvider>
);

export const SingleProduct = Template.bind({});
SingleProduct.args = {
  products: [
    {
      code: "product1",
      name: "商品1",
    },
  ],
};

export const TwoProducts = Template.bind({});
TwoProducts.args = {
  products: [
    {
      code: "product1",
      name: "商品1",
    },
    {
      code: "product2",
      name: "商品2",
    },
  ],
};

export const secondProductIsSelected = () => {
  const mockStore = StoreFixture.product2SelectedStore();
  const products = [
    {
      code: "product1",
      name: "商品1",
    },
    {
      code: "product2",
      name: "商品2",
    },
  ];
  return (
    <GlobalContextProvider mockStore={mockStore}>
      <Products products={products} />
    </GlobalContextProvider>
  );
};

export const ThreeProducts = Template.bind({});
ThreeProducts.args = {
  products: [
    {
      code: "product1",
      name: "商品1",
    },
    {
      code: "product2",
      name: "商品2",
    },
    {
      code: "product3",
      name: "商品3",
    },
  ],
};
