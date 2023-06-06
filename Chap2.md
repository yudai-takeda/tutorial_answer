# Checkpoint1


## Q1. pyenvとpoetryを使用して、python3.11を使用したプロジェクトを作ってみましょう！
```
pyenv install 3.11.0
(pyenv global 3.11.0)
poetry new hoge-project
cd hoge-project
poetry install
poetry env use 3.11.0
(poetry add hoge-package)
```


## Q2. なぜpyenvのような仮想環境ツールが必要なのでしょうか？
pipではライブラリ全体が同じバージョン(例えばpython3.11.0)になる。

pyenvはディレクトリごとに異なるバージョン(このディレクトリではpython3.2.1、こっちはpython3.11.0、など)を設定できる。


## Q3. pyproject.tomlに記載されているtool.poetry.dependenciesとtool.poetry.group.dev.dependenciesにそれぞれ含まれるライブラリの違いは何でしょうか?
tool.poetry.dependenciesにはプロジェクトの依存関係が示される。

tool.poetry.dependencies -> 暗黙的な main のグループの依存関係を示す。

tool.poetry.group.dev.dependencies -> 依存パッケージをグループ化したもの。devというグループにおける依存関係を示す。おそらく`poetry install --with dev`とか書くと、devに記載されたパッケージを選択的にインストールしたpython環境が構築される。


https://ts223.hatenablog.com/entry/poetry-group

https://qiita.com/nassy20/items/fbfa851e167f2fe7eefe

https://python-poetry.org/docs/master/managing-dependencies/

https://note.com/tatsuyashirakawa/n/nb3a6fb881e94


## Q4. poetry.lockファイルはgitで管理すべきでしょうか？しないべきでしょうか？
管理すべき。mainのブランチで管理・最新状態に保ち、各開発者が最新版をpullして、開発環境を統一して作業すべき。なお、githubのpoetry.lockは（基本的に）コミットされないようにしておくべき。

・pyproject.toml ・・・ 使っている Python やライブラリのバージョンを管理

・poetry.lock ・・・ 各ライブラリの実際のバージョンや依存関係を管理

https://qiita.com/ksato9700/items/b893cf1db83605898d8a


## Q5. poetry.lockファイルが存在せずに、pyproject.tomlのみが存在する場合に、どのような問題が起こるでしょうか？
開発者ごとに開発環境(pythonのバージョン)が異なる状態で作業してしまう可能性が生じる。

poetry.lockには、いま仮想環境にインストールされているパッケージのリストとそのバージョンが書いてある。pyproject.tomlで指定されているものだけでなく、それらが依存しているパッケージも含まれる。poetry.lockがある場合には、poetry installはそちらを先に見に行く。したがって、例えば pyproject.tomlに`^2.26.0`と書いてあって、poetry.lockに `version="2.27.0"`と書いてあれば、`2.27.0`がインストールされる。チーム開発している場合は、poetry.lockをバージョン管理化に置き、リポジトリにコミットすれば、チームメンバー全員が同じバージョンのパッケージを使って開発をすることが出来る。


## Q6. poetry.lockファイルに存在する、hashという項目はなぜ必要なのでしょうか？
hashはライブラリのハッシュ値。

➀セキュリティ観点。ファイルが何者かに編集・改変されていないか、hash値で答え合わせする。編集されたファイルをhash関数に通すと、元のファイルとは異なるhash値が出力されるため、異変に気づける。

➁hash値があることで、poetry installの際、ライブラリを探索する時間を短く、高速にできる。

https://qiita.com/ijufumi/items/367a4a0286b341e29b1b



# Checkpoint2


## Q1. Checkpoint1で作成したプロジェクトに、fizzbuzz.pyというファイルを作成して、以下の仕様を満たすプログラムを書いてみてください。

~~~
import sys
x=sys.argv[1]

#pattern 1
if x.isdigit()==True:
    n = int(x)
    if n % 15==0:
        print('FizzBuzz')
    elif n % 3==0:
        print('Fizz')
    elif n % 5==0:
        print('Buzz')
    else:
        print(x)
else:
    raise ValueError('This is invalid input!')



#pattern 2
x=sys.argv[1]
try:
    x.isdigit()==True
    n = int(x)
    if n % 15==0:
        print('FizzBuzz')
    elif n % 3==0:
        print('Fizz')
    elif n % 5==0:
        print('Buzz')
    else:
        print(x)
except ValueError:
    print('This is invalid input!')
except:
    pass    
~~~



# Checkpoint3


## Q1. DBにIndexを張るメリットとデメリットとは何でしょうか？
メリット：少ない判定回数で検索ができる。完全一致検索、前方検索、範囲検索などが高速になる。

デメリット：➀容量が大きく、インデックスを増やすほど動作が重くなる。➁1つのインデックスで1つの検索しかできない。OR検索などが困難。


## Q2. デッドロックになる場合はどのような場合でしょうか？
以下のような4つのデータを含むテーブルがあったとする。

➀id=1  |  name=test4  |  email=test4@jp  |  status=N

➁id=2  |  name=test3  |  email=test3@jp  |  status=N

➂id=3  |  name=test2  |  email=test2@jp  |  status=Y

➃id=4  |  name=test1  |  email=test1@jp  |  status=Y

次に、2つのインデックスを作成した。➀id：プライマリーキー、➁username：セカンダリインデックス

ここで、以下の2つのアクションがしたい。

    TransactionA : idが1, 2のメールアドレスを更新

    TransactionB : 名称がtest3,test4且つstatusがYのものを更新用で抽出（抽出の結果は0行）

TransactionAの実行時、➀id=1のプライマリーインデックスにロック。➁id=2のプライマリーインデックスにロック。

TransactionBの実行時、➀セカンダリインデックスusername_indexにて、test3のものにロック。➁test3がid=2のため、さらに、id=2のプライマリーインデックスにロック。➂セカンダリインデックスusername_indexにて、test4のものにロック。➃test4がid=1のため、さらに、id=1プライマリーインデックスにロック。 ※statusにインデックスを張っていないため、YとNを無視して全部ロックしてしまう。（今回のDeadLock原因はここ）

TransactionAとTransactionBが同時に実行されている場合、

    A➀が完了　　　　→ Aがid=1のプライマリーインデックスをロックしている

    B➀, ➁が完了　　→ Bがusername=test3のセカンダリーインデックス、id=2のプライマリーインデックスをロックしている

    A➁を実行　　　　→ id=2がBによってロックされているため、ロック待ち状態になる

    B➃を実行　　　　→ id=1がAによってロックされているため、ロック待ち状態になる

となり、DeadLockが発生。


https://engineering.cocone.io/2022/12/02/mysqlinnodb_index_deadlock/








