# at-coder

[AtCoder](https://atcoder.jp/)の解答用Dockerコンテナ

## Get started

Dockerイメージをビルドし、コンテナを立ち上げる

```sh
$ docker-compose build
$ docker-compose run py sh
```

問題用のプロジェクトを作成し、問題を解くPythonと入出力のファイルを編集

```sh
$ acc create -t abc001_a
$ vi problems/abc001_a/main.py
$ vi problems/abc001_a/01.in
$ vi problems/abc001_a/01.out
```

`-g`を指定すると入出力例をファイルに保存する

```sh
$ acc create -t abc001_a -g
$ vi problems/abc001_a/main.py
```

AtCoderのログイン情報を記載した`.env`ファイルをディレクトリトップに作成しておく必要がある

```sh
AC_USERNAME=username
AC_PASSWORD=password
```

テストケースを実行

```sh
$ acc test -t abc001_a
...

All test cases are passed.
```

解き終えた問題は`solved`ディレクトリに移動

```sh
$ acc clean
Done.
```
