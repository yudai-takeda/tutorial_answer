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
複数のタスク間で、ロック待ちの状態になった場合。

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



## Q3. N+1問題とは何でしょうか？
・N件のデータ行を持つテーブルをごそっと読みだすのに1回

・別のテーブルから、先述のテーブルの各行に紐づくデータを（1件ずつ）読み出すのに計N回

合計でN+1回のクエリを実行している状態。Nが大きいと処理に時間がかかる。



https://qiita.com/muroya2355/items/d4eecbe722a8ddb2568b



# Checkpoint4


## Q1. 以下の単語はどのような意味か説明してください。

### 1.RestAPI, エンドポイント, URI
#### ●RestAPI:RESTの4原則に則ったAPIのこと。　　※FastAPIはRestAPIを作成するためのツールのようなもの

REST:REpresentational State Transfer(具体的に状態を定義した情報のやり取り)

~~~
RESTの4原則
➀統一インターフェース：あらかじめ定義・共有された方法でやり取りされること。
　　ex) 「HTTP通信で,JSON形式でやりとりしますよ」
➁アドレス可能性：全ての情報が一意なURI（識別子）を持っていて、提供する情報をURIで表現できること。
➂接続性：やりとりされる情報にはハイパーリンクを含めることができる、というもの。
➃ステートレス性：やりとりが１回ごとに完結する、ということ。
~~~

API:Application Programing Interface(プログラムの情報をやり取りする蛇口のようなもの)

https://tech.012grp.co.jp/entry/rest_api_basics


#### ●エンドポイント：ネットワークの末端に接続された端末やコンピュータなどのこと。　　（"エッジデバイス"とほぼ同義かな）


#### ●URI：URLとURNの総称

URL（Uniform Resource Locator）：Web上にあるあらゆるファイルがWeb上のどの位置にあるのかを表したもの。住所的な。

URN（Uniform Resource Name）：住所ではなくWeb上での「名前」を指す。Web上で対象を特定するための固有のシリアルナンバーのようなイメージ。

ex) Amazon等のネットショップで書籍を検索すると、「ISBN」から始まる英数字の羅列があるが、これが書籍に割り振られたWeb上での識別番号であり、意味合い的にはURNとほぼ同じ。



### 2.HTTPリクエスト、レスポンス

#### ●HTTPリクエスト：ローカル/ブラウザからサーバに送る要求。
#### ●HTTPレスポンス：リクエストを受け取ったサーバが、ローカルに対して送る返答（例えばテキストファイルとか画像とかを送信する）。


### 3.Session

#### ●Session：ユーザーによる一連の動作(サイトにログイン・サイトにアクセス・買い物かごに商品を入れる・購入する・ログアウト)のこと。

### 4.Cookie

#### ●HTTP Cookie：Session ID（およびSession IDに紐付けられたサーバの情報など）を記録したデータ（テキストファイル）。

~~~
➀サーバはHTTPリクエストに対し、ブラウザ（ローカル）に向けて、webページの情報などと一緒にSession IDを送る（HTTPレスポンス）。
➁ブラウザは送られてきたSession IDを、送ってきたサーバの情報と一緒にCookieに保存する。
➂ブラウザが再度同じサイト/サーバにアクセスする際、Cookieの記録情報を元に先ほどのSession IDを見つけ出し、HTTPリクエストと一緒にSession IDも送る。
➃Session IDを受け取ったサーバは、「さっきもアクセスしてきたブラウザだ！！」と認識する。
→→→「ログイン状態の維持」や、「カートに入れた商品の保存」などができる。
~~~

※HTTPのステートレス性により、Cookieがないと、過去の状態を保存できない。

### 5.HTTPステータスコード 例えば(404)


### 6.HTTPリクエストメソッド
### 7.CSRFトークン
### 8.HTTPとHTTPSの違い
### 9.リクエストボディとリクエストヘッダ


