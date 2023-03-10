/* eslint-disable testing-library/no-debugging-utils */
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import ProductSelect from "./ProductSelect";
import { GlobalContextProvider } from "../../contexts/GlobalContext";
import { currentStore } from "../../contexts/GlobalContext";

// useNavigate hook をモック
const mockedNavigator = jest.fn();
jest.mock("react-router-dom", () => ({
  ...(jest.requireActual("react-router-dom") as any),
  useNavigate: () => mockedNavigator,
}));

describe("商品選択ページのテスト", () => {
  describe("初期表示の要素存在確認", () => {
    test("商品選択画面のタイトルが表示されること", () => {
      // Arrange

      const expected = "商品選択画面";

      // Act
      render(
        <GlobalContextProvider>
          <ProductSelect />
        </GlobalContextProvider>
      );
      const actual = screen.getByRole("heading", {
        name: "商品選択画面",
      }).textContent;

      // Assert
      expect(actual).toBe(expected);
    });

    test("商品選択画面の選択オプションが表示されること", () => {
      // Arrange

      // Act
      render(
        <GlobalContextProvider>
          <ProductSelect />
        </GlobalContextProvider>
      );
      const actualProduct1Element = screen.getByRole("radio", {
        name: "商品1",
      });
      const actualProduct2Element = screen.getByRole("radio", {
        name: "商品2",
      });

      // Assert
      expect(actualProduct1Element).toBeInTheDocument();
      expect(actualProduct2Element).toBeInTheDocument();
    });

    test("次へボタンが存在すること", () => {
      // Arrange

      // Act
      render(
        <GlobalContextProvider>
          <ProductSelect />
        </GlobalContextProvider>
      );
      const actualNextButton = screen.getByRole("button", {
        name: "次へ",
      });

      // Assert
      expect(actualNextButton).toBeInTheDocument();
    });
  });

  describe("動的機能のテスト", () => {
    test("次へのボタンをクリックする時に選択された商品コードがStoreに保存されていること", () => {
      // Arrange
      const expected = "product2";

      // Act
      render(
        <GlobalContextProvider>
          <ProductSelect />
        </GlobalContextProvider>
      );
      const product2Element = screen.getByRole("radio", {
        name: "商品2",
      });
      const nextButton = screen.getByRole("button", {
        name: "次へ",
      });
      userEvent.click(product2Element);
      userEvent.click(nextButton);
      const actualState = currentStore;

      // Assert
      expect(product2Element).toBeChecked();
      expect(actualState.pages.productSelectPage.selectedProductCode).toBe(
        expected
      );
    });

    test("次へボタンをクリックすると、顧客情報入力画面に進むこと", () => {
      // Arrange
      const expectedPath = "/customer";

      // Act
      render(
        <GlobalContextProvider>
          <ProductSelect />
        </GlobalContextProvider>
      );
      const nextButton = screen.getByRole("button", {
        name: "次へ",
      });
      userEvent.click(nextButton);

      // Assert
      expect(mockedNavigator).toHaveBeenCalledWith(expectedPath);
    });
  });
});
