import { Route, Routes } from "react-router-dom";
import Customer from "../pages/Customer/Customer";
import ProductSelect from "../pages/ProductSelect/ProductSelect";

export default function Router() {
  return (
    <Routes>
      <Route path="/" element={<ProductSelect />} />
      <Route path="/customer" element={<Customer />} />
    </Routes>
  );
}
