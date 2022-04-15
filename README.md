# FolderBreaker
フォルダの中に保存されているファイルを全て外に出してから空になったフォルダを削除するモジュールです．

コマンドラインで実行する場合の例
```
$python3 folder_breaker.py /home/usr/parent_dir
```

Pythonモジュールとしてインポートする場合の例
```
import folder_breaker as fb

fb.breakAllFolder('/home/usr/parent_dir')
```

上記の例の場合，引数で与えたディレクトリより下の階層にあるサブディレクトリを全て削除した上で，中に格納されているファイルを全て'parent_dir'へ移動します．

このとき，同じファイル名が存在する場合は，ファイル名末尾に0, 1, 2...と，検出された順に自動で連番を付加して改名します．

そのため，ファイルが無くなる心配はありません．

フォルダツリーで現すと下記のような状態になります．

Example: "ParentDir"を引数で指定した場合
```
(Before)
  ParentDir
   |-aaa.jpg
   |-bbb.jpg
   |-SubDir
   |  |-bbb.jpg
   |  |-ccc.jpg
   |-SubDir_2
      |-aaa.jpg
      |-bbb.jpg
(After)
  ParentDir
   |-aaa.jpg
   |-aaa_0.jpg
   |-bbb.jpg
   |-bbb_0.jpg
   |-bbb_1.jpg
   |-ccc.jpg
   ```
