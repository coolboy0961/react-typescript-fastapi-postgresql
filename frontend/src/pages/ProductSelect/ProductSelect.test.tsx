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
    xtest("初期ステータスでproduct1が選択されている", () => {
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

      // Assert
      expect(actualProduct1Element).toBeChecked();
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
    xtest("商品1と商品2をそれぞれ選択できること", () => {
      // 商品1を選択できること

      // Arrange

      // Act
      render(
        <GlobalContextProvider>
          <ProductSelect />
        </GlobalContextProvider>
      );
      const product1Element = screen.getByRole("radio", {
        name: "商品1",
      });
      const product2Element = screen.getByRole("radio", {
        name: "商品2",
      });
      userEvent.click(product1Element);
      // Assert
      expect(product1Element).toBeChecked();

      // 商品2を選択すると、商品1の選択が外れること
      // Arrange
      // Act
      userEvent.click(product2Element);
      // Assert
      expect(product1Element).not.toBeChecked();
      expect(product2Element).toBeChecked();
    });

    test("次へのボタンをクリックすると、選択された商品コードがStoreに保存されること", () => {
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
