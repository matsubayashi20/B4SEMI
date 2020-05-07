テストコードの実行方法

親ディレクトリ(つまり B4SEMI/ )で
$ python -m unittest discover tests
を実行．
上記コマンドの最後に指定したフォルダ(この場合だと tests)内の
test**.py を全て検索し，
さらに上記ファイル内の TestCase を継承したクラス内で定義された
test**()メソッドが全て実行される．

