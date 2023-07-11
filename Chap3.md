Voltaとは、Node.js、npm、およびYarnのバージョン管理をシンプルかつ効率的に行うためのツール

# Checkpoint

## Q1. async, await, Promiseについて説明してください。

「async / await」は、Promiseによる非同期処理をより簡潔に効率よく記述できる。

### async：関数がpromiseを返すようにする。

### await：Promise処理の結果が返ってくるまで一時停止させる。awaitはasyncで定義された関数の中だけでしか使えない。

```
<script>
async function myDisplay() {          //myDisplay()がpromiseを返すようになる。
  let myPromise = new Promise(function(resolve) {
    setTimeout(function() {resolve("I love You !!");}, 3000);
  });
  document.getElementById("demo").innerHTML = await myPromise;            //myPromiseの完了を待って実行される。
}

myDisplay();
</script>
```
https://www.sejuku.net/blog/69618

### Promise：非同期処理の完了もしくは失敗の結果を表すオブジェクト。
Promiseの状態は以下の3種類で、最終的には②か③のどちらかで終了となる。
```
➀待機 (pending): 初期状態。成功も失敗もしていません。
➁履行 (fulfilled): 処理が成功して完了したことを意味します。
➂拒否 (rejected): 処理が失敗したことを意味します。
```
なお、`then()`は`Promise`オブジェクトのメソッドであり、最大2つの引数を持ち、 Promiseが成功した場合と失敗した場合のコールバック関数を取る。`Promise.then()`は`Promise`の完了を待って実行される。

thenの引数が1つの時は履行した時の動作。引数が2つの時は、順に履行した時の動作、拒否した時の動作をそれぞれコードで記述する。

なお、「thenに引数を2つ書いて、rejectされた時の処理を2番目に記述する」パターンと、「thenの代わり（もしくはthenの次）にcatchメソッドを書いて、rejectされた時の処理をcatchに記述する」パターンは、実質的に同一である。

https://qiita.com/cheez921/items/41b744e4e002b966391a



## Q2. TypeScriptにおける、ジェネリクスとはどういうものでしょうか？
### ジェネリクス：言語機能。型の安全性とコードの共通化を両立できるようにするための機能。

ある関数に対して、異なる型の入力を与えて処理を行いたいとする。本来は、一つの関数は受け取れる引数の型（例えばstring）が決まっているため、入力の型ごとに同じような関数を定義する必要がある（string用の関数、number用の関数……など）。するとコードが無駄に長くなる。

これに対し、関数の型をanyにするという方法もある。しかし、これでは戻り値の型もanyになるため、型の安全性が損なわれる（バグの要因となり得る）。

そこでジェネリクスでは、「型も変数のようにして関数に与えられるようにする」ことで、この問題を解決している。


https://typescriptbook.jp/reference/generics





