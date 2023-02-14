import { ComponentMeta, ComponentStory } from "@storybook/react";
import { GlobalContextProvider } from "../../contexts/GlobalContext";
import { MemoryRouter } from "react-router-dom";
import { within, userEvent, waitFor } from "@storybook/testing-library";
import { expect } from "@storybook/jest";
import Customer from "./Customer";
import MockAdapter from "axios-mock-adapter/types";
import AxiosMock from "../../test-utils/AxiosMock";

export default {
  title: "Pages/Customer",
  component: Customer,
} as ComponentMeta<typeof Customer>;

const Template = (mockApi?: (axiosMock: MockAdapter) => void) => (
  <GlobalContextProvider>
    <MemoryRouter>
      {mockApi && <AxiosMock mockApi={mockApi} />}
      <Customer />
    </MemoryRouter>
  </GlobalContextProvider>
);

export const Default: ComponentStory<typeof Customer> = () => {
  const mockApi = (axiosMock: MockAdapter) => {
    axiosMock.onGet("/api/v1/address?postcode=1840014").reply(200, {
      address: "東京都XXXXXX",
    });
  };
  return Template(mockApi);
};
Default.storyName = "Customerページの手動動作確認";

export const FilledName: ComponentStory<typeof Customer> = () => {
  return Template();
};
FilledName.storyName =
  "氏名の入力欄に入力したデータはvalueにBindingされていること";
FilledName.play = async ({ canvasElement }: any) => {
  // Arrange
  const expected = "React太郎";

  // Act
  const canvas = within(canvasElement);
  const nameInputElement = canvas.getByTestId("name-input-text");
  userEvent.type(nameInputElement, expected);

  // Assert
  expect(nameInputElement).toHaveDisplayValue(expected);
};

export const NameValidationErrorRequired: ComponentStory<typeof Customer> =
  () => {
    return Template();
  };
NameValidationErrorRequired.storyName =
  "氏名の入力欄に入力せずに次へのボタンをクリックするとエラーメッセージが表示される";
NameValidationErrorRequired.play = async ({ canvasElement }: any) => {
  // Arrange
  const expected = "this is required";

  // Act
  const canvas = within(canvasElement);
  const nextButton = canvas.getByRole("button", {
    name: "次へ",
  });
  userEvent.click(nextButton);

  // Assert
  canvas.findByText(expected);
};

export const NameValidationErrorTooLong: ComponentStory<typeof Customer> =
  () => {
    return Template();
  };
NameValidationErrorTooLong.storyName =
  "氏名の入力欄に9桁の文字を入力して、次へのボタンをクリックするとエラーメッセージが表示される";
NameValidationErrorTooLong.play = async ({ canvasElement }: any) => {
  // Arrange
  const expected = "this is too long";

  // Act
  const canvas = within(canvasElement);
  const nameInputElement = canvas.getByTestId("name-input-text");
  userEvent.type(nameInputElement, "aaaaaaaaa");
  const nextButton = canvas.getByRole("button", {
    name: "次へ",
  });
  userEvent.click(nextButton);

  // Assert
  canvas.findByText(expected);
};

export const FilledSex: ComponentStory<typeof Customer> = () => {
  return Template();
};
FilledSex.storyName =
  "性別のプルダウンリストで[男]を選択してSelectのvalueにBindingされていること";
FilledSex.play = async ({ canvasElement }: any) => {
  // Arrange
  const expected = "male";

  // Act
  const canvas = within(canvasElement);
  const sexSelectElement = canvas.getByRole("combobox", {
    name: "性別：",
  });
  userEvent.selectOptions(sexSelectElement, expected);

  // Assert
  expect(sexSelectElement).toHaveValue(expected);
};

export const AutoFilledAddress1: ComponentStory<typeof Customer> = () => {
  const mockApi = (axiosMock: MockAdapter) => {
    axiosMock.onGet("/api/v1/address?postcode=1840015").reply(200, {
      address: "東京都XXXXXX",
    });
  };
  return Template(mockApi);
};
AutoFilledAddress1.storyName =
  "郵便番号を入れて、チェックボタンをクリックすると、住所が「住所1」に入ること";
AutoFilledAddress1.play = async ({ canvasElement }: any) => {
  // Arrange
  const expected = "東京都XXXXXX";

  // Act
  const canvas = within(canvasElement);
  const postcodeInputElement = canvas.getByTestId("postcode-input-text");
  userEvent.type(postcodeInputElement, "1840015");
  const addressInputButtonElement = canvas.getByRole("button", {
    name: "住所入力",
  });
  userEvent.click(addressInputButtonElement);

  await waitFor(() => {
    const actual = canvas
      .getByTestId("address1-input-text")
      .getAttribute("value");
    // Assert
    expect(actual).toBe(expected);
  });
};
