import MockAdapter from "axios-mock-adapter";
import { axiosInstance } from "./axios-instance";
import Address from "./address";


const axiosMock = new MockAdapter(axiosInstance);

describe("address apiのテスト", () => {
  beforeEach(() => {
    // axiosMockに登録したMockをクリア
    axiosMock.reset();
  });
  test("address apiから住所を取得できること", async () => {
    // Arrange
    axiosMock.onGet("/api/v1/address?postcode=1840015").reply(200, {
      address: "東京都XXXXXX",
    });
    const expected = "東京都XXXXXX";

    // Act
    const target = new Address();
    const response = await target.getAddress("1840015");
    const actual = response.address;

    // Assert
    expect(actual).toBe(expected);
  });
});
