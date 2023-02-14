import { useGlobalContext } from "../contexts/GlobalContext";

export default function Products(props: { products: Product[] }) {
  // Data Model
  let products: Product[] = [
    {
      code: "product1",
      name: "商品1",
    },
    {
      code: "product2",
      name: "商品2",
    },
  ];
  if (props.products.length > 0) {
    products = props.products;
  }

  // Data Binding
  const { store, selectProduct } = useGlobalContext();
  const selectedProductFromState = store.pages.productSelectPage.selectedProductCode;

  // Event Method
  function onChangeProduct(event: React.ChangeEvent<HTMLInputElement>) {
    selectProduct(event.target.value);
  }

  // HTML
  return (
    <div>
      {products.map((product) => {
        return (
          <label key={product.name}>
            <input
              type="radio"
              value={product.code}
              checked={selectedProductFromState === product.code}
              onChange={onChangeProduct}
            />
            {product.name}
          </label>
        );
      })}
    </div>
  );
}

type Product = {
  code: string;
  name: string;
};
