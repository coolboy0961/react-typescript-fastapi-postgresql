# 仮想環境作成
```
export PIPENV_VENV_IN_PROJECT=true && pipenv --python 3.10
```

# 仮想環境削除
```
pipenv --rm
```

# ディレクトリ構成
```
├── Pipfile
├── Pipfile.lock
├── __files # WireMock起動時に自動生成するフォルダ、使っていない
├── __init__.py
├── config.py # 環境変数を導入するためのファイル
├── env
│   ├── local.env # ローカルでAPIを起動する時に導入する環境変数のファイル
│   └── unit-test.env # ユニットテストする時に導入する環境変数のファイル
├── local.db # ローカルでAPIを起動する時とAPIテストする時にに利用するDBのファイル
├── main.py # FastApiのmainファイル Framework & Drivers
├── mappings # WireMock起動時に自動生成するフォルダ、使っていない
├── readme.md
├── src # プロダクトコードのフォルダ(Clean Architectureに基づいたディレクトリ構成)
│   ├── application # Application Business Rule
│   │   └── usecases
│   │       └── UserUsecase.py
│   ├── domain # Enterprise Business Rule
│   │   └── entities
│   │       ├── CameraEntity.py
│   │       └── UserEntity.py
│   ├── exception # 異常系関連クラス
│   │   ├── CustomException.py
│   │   └── ErrorCodes.py
│   ├── infrastructure # Framework & Drivers
│   │   ├── ExternalApiClient.py
│   │   └── database.py
│   └── interface # Interface Adapters
│       ├── controllers # 理想はこの部分もFastApiの機能を使わないようにすべきだが、現実的にそうすると、FastApiの便利機能が使えなくなるのでトレードオフが必要
│       │   └── user_controller.py
│       └── gateways
│           ├── external_apis
│           │   └── CameraExternalApi.py
│           └── repositories # 理想はこの部分もFastApiの機能を使わないようにすべきだが、現実的にそうすると、FastApiの便利機能が使えなくなるのでトレードオフが必要
│               ├── CameraRepository.py
│               ├── UserRepository.py
│               └── models
│                   ├── CameraModel.py
│                   └── UserModel.py
└── tests # テストコードのフォルダ
    ├── __init__.py
    ├── api-test
    │   └── test_user.py
    ├── conftest.py # pytestの設定ファイル、主にfixtureを定義する場所
    └── unit-test
        ├── controllers
        │   └── test_user_controller.py
        ├── gateways
        │   ├── external_apis
        │   │   └── test_camera_external_api.py
        │   └── repositories
        │       ├── test_camera_repository.py
        │       └── test_user_repository.py
        ├── test.db # ユニットテストする時に利用するDBのファイル
        └── usecases
            └── test_user_usecase.py
```