# doubler

[![test](https://github.com/KaitoKubota/doubler/actions/workflows/test.yml/badge.svg)](https://github.com/KaitoKubota/doubler/actions/workflows/test.yml)

標準入力から数値を読み込み、計算して出力するコマンドです。

## インストール方法
```bash
$ git clone https://github.com/KaitoKubota/doubler.git
$ cd doubler
$ pip install .　
```


## 使い方
1個の数字を計算する場合：
```bash
echo 10 | doubler

# 出力結果: 100.0
```
たくさんの数字を一気に計算する場合：
```bash
seq 5 | doubler

# 出力結果:
# 1.0
# 4.0
# 9.0
# 16.0
# 25.0
```

## ライセンス
このソフトウェアは、BSD 3-Clause License の下で公開されています。 詳細については、LICENSE を確認してください。