import { Store } from "./types";

export const SELECT_PRODUCT = "SELECT_PRODUCT";

type GlobalReducerAction = {
  type: "SELECT_PRODUCT";
  payload: string;
};

/**
 * 商品選択のReducer
 * @param productCode 商品コード
 * @param state 現在の状態
 * @returns 次の状態
 */
function selectProduct(state: Store, productCode: string) {
  const copyState: Store = JSON.parse(JSON.stringify(state));
  copyState.pages.productSelectPage.selectedProductCode = productCode;
  return copyState;
}

/**
 * グローバルのReducer
 * @param state 現在の状態
 * @param action アクション
 * @returns 次の状態
 */
export const globalReducer: React.Reducer<Store, GlobalReducerAction> = (
  state: Store,
  action: GlobalReducerAction
) => {
  switch (action.type) {
    case SELECT_PRODUCT:
      return selectProduct(state, action.payload);
    default:
      return state;
  }
};
