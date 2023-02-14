export type Store = {
  user: User;
  pages: Pages;
};

export type User = {
  name: string;
  age: number;
  address: string;
};

export type Pages = {
  productSelectPage: ProductSelectPage;
};

export type ProductSelectPage = {
  selectedProductCode: string;
};

export type GlobalContextType = {
  store: Store;
  selectProduct: (productCode: string) => void;
};