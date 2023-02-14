import { ComponentMeta } from "@storybook/react";
import ProductSelect from "./ProductSelect";
import { GlobalContextProvider } from "../../contexts/GlobalContext";
import { MemoryRouter } from "react-router-dom";

export default {
  title: "Pages/ProductSelect",
  component: ProductSelect,
} as ComponentMeta<typeof ProductSelect>;

export const Default = () => {
  return (
    <GlobalContextProvider>
      <MemoryRouter>
        <ProductSelect />
      </MemoryRouter>
    </GlobalContextProvider>
  );
};
