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

poetry.lockには、いま仮想環境にインストールされているパッケージのリストとそのバージョンが書いてある。pyproject.tomlで指定されているものだけでなく、それらが依存しているパッケージも含まれる。poetry.lockがある場合には、poetry installはそちらを先に見に行く。したがって、例えば pyproject.tomlに^2.26.0と書いてあって、poetry.lockに version="2.27.0"と書いてあれば、2.27.0がインストールされる。チーム開発している場合は、poetry.lockをバージョン管理化に置き、リポジトリにコミットすれば、チームメンバー全員が同じバージョンのパッケージを使って開発をすることが出来る。


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










