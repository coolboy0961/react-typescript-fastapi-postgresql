import { Store } from "../contexts/GlobalContext/types";

export default class StoreFixture {
  /**
   * 初期状態のStateオブジェクトを返す
   * @returns 初期状態のState
   */
  static initialStore(): Store {
    return {
      user: {
        name: "",
        address: "",
        age: 0,
      },
      pages: {
        productSelectPage: {
          selectedProductCode: "product1",
        },
      },
    };
  }

  /**
   * product2が選択されている状態のStateオブジェクトを返す
   */
  static product2SelectedStore(): Store {
    return {
      user: {
        name: "",
        address: "",
        age: 0,
      },
      pages: {
        productSelectPage: {
          selectedProductCode: "product2",
        },
      },
    };
  }
}
