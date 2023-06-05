# check point


## `linux`コマンド
## Q1. homeディレクトリ(cd ~とコマンドを打つと移動できる)に、tutorialという名前のディレクトリを作りましょう。

## Q2. (Q1に続いて) tutorialディレクトリの中に、git-command.txtという空のファイルを作成してください。

## Q3. (Q2に続いて) Shellでgitとコマンドを打つと以下のように表示されると思います。この内、repositoryという文言が含まれている行のみをgit-command.txtに記載しましょう。この際に、手動でコピーアンドペーストするのではなく、1行のコマンドで打てるようにしましょう。
git | grep 'repository'  -a > git-command.txt

## Q4. hogeというソフトをインストールしたはずなのに、Shellでhogeと入力しても`command not found: hoge`というエラーがでしまって使えないということがよくあります。このエラーはインストールしたソフトウェアにPATHが正しく通されていないことが原因です。 では、どうすればPATHを正しく通すことができるのでしょうか？
`echo export PATH='home/..../..../....:$PATH' >> ~/.bashrc`

と入力。PATHという環境変数に新しいパスを追加。`.bashrc`ファイル(home/ユーザー名/.bashrc)にexport PATH=home/..../..../....:$PATHという文章を追加している。これにより、環境変数が永続化される。ただし、追加されただけではすぐに読み込まれないので、

`source ~/.bashrc`

として`.bashrc`を再読み込みする



