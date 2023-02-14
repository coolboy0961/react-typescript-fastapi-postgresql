import { useEffect } from "react";
import MockAdapter from "axios-mock-adapter";
import { axiosInstance } from "../apis/axios-instance";

interface IProps {
  mockApi: (adapter: MockAdapter) => void;
}

const axiosMock = new MockAdapter(axiosInstance);

/**
 * StoryBookのstoriesでaxios mockApi adapterを利用するためのコンポーネント
 * 
 * 
 * Usage:
   ```
   export const Default = () => {
    const mockApi = (axiosMock: MockAdapter) => {
      axiosMock.onGet('/api/meetings/1').reply(200, {
        id: 1,
        title: 'A Meeting',
      });
    };
    return (
      <>
        <AxiosMock mockApi={mockApi} />
        <Meeting />
      </>
    );
  };
  ```
 * @param mockApi モックの内容を定義するメソッド
 * @see https://gist.github.com/rafaelrozon/ed86efbea53094726e162dc05882cddc
 */
function AxiosMock({ mockApi }: IProps) {
  useEffect(() => {
    mockApi(axiosMock);
    return () => {
      axiosMock.reset();
    };
  }, [mockApi]);
  return <></>;
}

export default AxiosMock;
