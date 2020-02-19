## Get started

Dockerイメージをビルドし、コンテナを立ち上げる

```sh
$ docker-compose build
$ docker-compose run py sh
```

問題用のプロジェクトを作成し、問題を解くPythonと入出力のファイルを編集

```sh
$ acc create -p abc001_a
$ vi problems/abc001_a/main.py
$ vi problems/abc001_a/01.in
$ vi problems/abc001_a/01.out
```

`-g`を指定すると入出力例をファイルに保存する

```sh
$ acc create -p abc001_a -g
$ vi problems/abc001_a/main.py
```

テストケースを実行

```sh
$ acc test -p abc001_a
...

All test cases are passed.
```
