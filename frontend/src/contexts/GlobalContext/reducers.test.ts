import StoreFixture from "../../test-utils/StoreFixture";
import { globalReducer } from "./reducers";

describe("reducer unit tests", () => {
  test("selectProduct reducerを実行して、productが選択された状態になること", () => {
    // Arrange
    const expected = StoreFixture.initialStore();
    expected.pages.productSelectPage.selectedProductCode = "product2";

    // Act
    const actual = globalReducer(StoreFixture.initialStore(), {
      type: "SELECT_PRODUCT",
      payload: "product2",
    });

    // Assert
    expect(actual).toEqual(expected);
  });
});
