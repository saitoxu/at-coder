# at-coder

[AtCoder](https://atcoder.jp/)の解答用Dockerコンテナ

## Get started

Dockerイメージをビルドし、コンテナを立ち上げる

```sh
$ docker-compose build
$ docker-compose run py sh
```

## How to use

問題を解くときに便利な`acc`コマンドがある

### `acc create`

問題用のプロジェクトを作成する。その後問題を解くPythonと入出力のファイルを編集

```sh
$ acc create -t abc001_a
$ vi problems/abc001_a/main.py
$ vi problems/abc001_a/01.in
$ vi problems/abc001_a/01.out
```

`-g`を指定すると問題にある入出力例もファイルに保存する

```sh
$ acc create -t abc001_a -g
$ vi problems/abc001_a/main.py
```

事前にAtCoderのログイン情報を記載した`.env`ファイルをディレクトリトップに作成しておく必要がある

```sh
AC_USERNAME=username
AC_PASSWORD=password
```

### `acc test`

テストケースを実行する

```sh
$ acc test -t abc001_a
...

All test cases are passed.
```

問題ディレクトリに`0x.in`, `0x.out`のように入出力のファイルが必要

### `acc clean`

解き終えた問題を`solved`ディレクトリに移動

```sh
$ acc clean
Done.
```

解き終えていない問題はproblemsディレクトリ直下に`.unsolved`ファイルを作成し、以下のようにそのディレクトリ名を記載しておくと移動対象にならない

```
agc026_b
agc041_b
```
