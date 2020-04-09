# Switch Album Sorter

## 使用方法

- 以下のディレクトリ構造を任意の場所に構築する。

```
.
└── (任意のフォルダ名A) ※1
    └── (任意B)
        ├── After
        ├── Album ※2
        └── (任意C)
            ├── README.md
            ├── main.py
            └── fold_id.py
```

- ※1 :ここのディレクトリ内に以下の構造で仕分けが行われる。

```
.
└── (任意A)
    └── sw_hogehoge(ゲームタイトル)
        ├── img
            └── ~.jpg
        └── movie
            └── ~.mp4
```

- ※2 :SwitchのSDカード内にある`Album`フォルダをここに配置する。`shutil.move`を使用するので**バックアップ推奨**。

- `main.py`を実行すると、`fold_id.py`に記載されている情報を元に仕分けを行う。

## fold_id.pyの編集について

- 仕分け前に、`fold_id.py`の中身を編集する。
- 正しく編集しないと、対象外のファイルが仕分けされない。
- アルバム内にある、`2020010112345600-hogehoge.jpg` のファイル名の`hogehoge`の部分に記載されている文字列を控える。
- `fold_id.py`に記載されている`dict(dict型)`を以下の形式に則って編集する。

```py
# hogehoge = さっき控えた文字列
# gametitle = ゲームタイトル、これが仕分け後のフォルダ名になる

dict = {'hogehoge': 'gametitle', ...}
```

