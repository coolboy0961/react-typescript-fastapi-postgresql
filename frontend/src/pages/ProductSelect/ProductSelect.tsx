import { useNavigate } from "react-router-dom";
import Products from "../../components/Products";

export default function ProductSelect() {
  // Data Model

  // Data Binding

  // Event Method
  const navigate = useNavigate();
  function onClickToNextPage() {
    navigate("/customer");
  }

  // HTML
  return (
    <>
      <h1>商品選択画面</h1>
      <Products products={[]}/>
      <button onClick={onClickToNextPage}>次へ</button>
    </>
  );
}