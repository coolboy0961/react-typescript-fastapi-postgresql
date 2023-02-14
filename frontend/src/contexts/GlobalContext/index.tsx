import { createContext, useContext, useReducer } from "react";
import { globalReducer } from "./reducers";
import { GlobalContextType, Store } from "./types";

const GlobalContext = createContext<GlobalContextType>({
  store: initStore(),
  selectProduct: () => {},
});

export const useGlobalContext = (): GlobalContextType =>
  useContext<GlobalContextType>(GlobalContext);

interface GlobalContextProviderProps {
  children?: React.ReactNode;
  /**
   * Test only!
   * テストを行うときに状態をモックするために利用する。
   * 
   * usage:
   * ```
   *  const mockStore = StoreFixture.initialStore();
      render(
        <GlobalContextProvider mockStore={mockStore}>
          <Products products={[]} />
        </GlobalContextProvider>
      );
   * ```
   */
  mockStore?: Store;
}

/**
 * Test only!!
 * Test時に現状の状態を取得する
 */
export let currentStore: Store;
export const GlobalContextProvider = ({
  children,
  mockStore,
}: GlobalContextProviderProps) => {
  const [store, dispatch] = useReducer(
    globalReducer,
    mockStore ? mockStore : initStore()
  );
  currentStore = store;
  /**
   * 商品選択のアクション
   * @param productCode プロダクトコード
   */
  function selectProduct(productCode: string) {
    dispatch({
      type: "SELECT_PRODUCT",
      payload: productCode,
    });
  }
  return (
    <GlobalContext.Provider
      value={{
        store,
        selectProduct,
      }}
    >
      {children}
    </GlobalContext.Provider>
  );
};

function initStore() {
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
  } as Store;
}