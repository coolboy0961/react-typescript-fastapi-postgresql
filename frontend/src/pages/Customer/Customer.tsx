import { useState } from "react";
import { useForm } from "react-hook-form";
import { apis } from "../../apis/apis";

export default function Customer() {
  // Data Model
  const sexOptions = [
    { value: "", label: "---" },
    { value: "male", label: "男" },
    { value: "female", label: "女" },
  ];

  // Data Binding
  const [sex, setSex] = useState("");
  const [postcode, setPostcode] = useState("");
  const [address1, setAddress1] = useState("");
  const [display, setDisplay] = useState(false);

  // Event Method
  function onChangeSex(event: any) {
    setSex(event.target.value);
  }
  function onChangePostcode(event: any) {
    setPostcode(event.target.value);
  }
  function onChangeAddress1(event: any) {
    setAddress1(event.target.value);
  }
  async function onClickAddressInput(event: any) {
    const response = await apis.address.getAddress(postcode);
    const address = response.address;
    setAddress1(address);
  }

  // Validation Check
  interface IFormInput {
    name: string;
  }
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<IFormInput>({
    mode: "onSubmit",
    reValidateMode: "onChange",
  });
  const onNextButtonClick = handleSubmit((data) => {
    console.log(JSON.stringify(data));
  });

  // HTML
  return (
    <>
      <h1>顧客情報入力画面</h1>
      { display && <h1 style={{display: 'none'}}>test</h1> }
      <label>
        氏名：
        <input
          {...register("name", {
            required: "this is required",
            maxLength: {
              value: 8,
              message: "this is too long",
            },
          })}
          type="text"
          data-testid="name-input-text"
        />
        <p>{errors.name?.message}</p>
      </label>
      <br />
      <label>
        性別：
        <select
          data-testid="sex-pull-down-list"
          value={sex}
          onChange={onChangeSex}
        >
          {sexOptions.map((option) => {
            return (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            );
          })}
        </select>
      </label>
      <div>
        <span>住所</span>
        <br />
        <label>
          郵便番号：
          <input
            type="text"
            data-testid="postcode-input-text"
            value={postcode}
            onChange={onChangePostcode}
          />
        </label>
        <button onClick={onClickAddressInput}>住所入力</button>
        <br />
        <label>
          住所1：
          <input
            type="text"
            data-testid="address1-input-text"
            value={address1}
            onChange={onChangeAddress1}
          />
        </label>
        <br />
        <label>
          住所2：
          <input type="text" data-testid="address2-input-text" />
        </label>
      </div>
      <br />
      <button onClick={onNextButtonClick}>次へ</button>
    </>
  );
}
