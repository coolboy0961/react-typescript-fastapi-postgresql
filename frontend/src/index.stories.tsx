import React from "react";
import { ComponentMeta, ComponentStory } from "@storybook/react";
import { MemoryRouter } from "react-router-dom";
import Router from "./router/Router";
import { GlobalContextProvider } from "./contexts/GlobalContext";

export default {
  title: "Pages/Index",
} as ComponentMeta<typeof GlobalContextProvider>;

/**
 * Indexページから後続ページに遷移できるStory
 * @link https://chestozo.medium.com/how-to-mock-location-inside-storybook-stories-76a7c0705354
 */
export const Default: ComponentStory<typeof GlobalContextProvider> = () => {
  return (
    <GlobalContextProvider>
      <MemoryRouter initialEntries={["/"]}>
        <Router />
      </MemoryRouter>
    </GlobalContextProvider>
  );
};
