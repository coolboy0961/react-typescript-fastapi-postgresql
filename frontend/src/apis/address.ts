import { axiosInstance } from "./axios-instance";

export default class Address {

  /**
   * BFF の GET api/v1/address APIを呼び出すメソッド
   */
  async getAddress(postcode: string): Promise<AddressResponse> {
    const response = await axiosInstance.get(`/api/v1/address?postcode=${postcode}`);
    return response.data;
  }
}

type AddressResponse = {
  address: string;
};