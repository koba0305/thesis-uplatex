# upLaTeX 版の卒業論文

## 📄 [ここを押すと論文PDFが読めます](main.pdf)

`thesis` から章本文・参考文献・図・表をコピーした独立した作業用プロジェクトです。今後はこちらの `chapters/` を編集してください。元の `thesis/` とは自動同期しません。

## ビルド

TeX Live の upLaTeX、latexmk、Biber、dvipdfmx を使います。

```sh
cd '/Users/yume/大学に持ってく/thesis-uplatex'
latexmk main.tex
```

出力は `main.pdf` です。`.latexmkrc` が upLaTeX → Biber → upLaTeX（必要回数）→ dvipdfmx を管理します。LuaLaTeX 用の補助ファイルはコピーしていません。

- `main.tex`: 文書設定、表紙、目次、章の読み込み、参考文献
- `frontmatter/titlepage.tex`: 表紙（指導教員・学修番号・提出日は未記入）
- `frontmatter/abstract-ja.tex`、`frontmatter/abstract-en.tex`: 和英要旨の記入場所
- `iathesis.sty`、`code_listings.tex`: 提供された IA テンプレートから変更せずコピーした書式
- `chapters/`: 第1章〜第9章の本文
- `references.bib`: 参考文献データ（biblatex + Biber）
- `figures/`、`tables/`: 図と表

文書クラスは IA テンプレートに合わせて `jsreport` にしています。テンプレート本文では50ページ程度以上の学士論文にも章立てを認めているため、元の9章を維持しています。表紙・和英要旨・目次・本文の順序と書式は `iathesis.sty` に従います。章見出しの目次ページ番号が省略されるのも提供スタイルの仕様です。日本語 PDF しおりには `pxjahyper`、欧文アクセント文字には T1 フォントを使用します。

`thesis-template/` は参照用の原本です。サンプルの参考文献・説明本文・謝辞は取り込んでいません。英文題目・和英要旨と表紙の未記入項目は、提出前に記入してください。所属は提供テンプレートの学部の表記です。年度はテンプレートと同じくビルド日の年度になります。

日本語フォントは `pxchfon` の `ipaex,unicode` 設定で IPAex 明朝・ゴシックを PDF に埋め込みます。日本語 CMap を持たないビューアでも扱えるよう、文字の対応表も PDF に含む構成です。今回の確認では Codex 内蔵コンパイラは失敗したため、上記のローカル `latexmk` コマンドでビルドしてください。

本文のコードブロックは `lstlisting` を使い、`code_listings.tex` の `mystyle`（背景色・行番号・折り返し）を適用しています。JSON 用の言語定義は `main.tex` に追加しています。

補助ファイルのみを削除するには `latexmk -c` を実行します。

## 参考文献の確認

未登録だった7件は原典を照合して登録しました。修正理由・読むべき箇所・残る確認事項は [reference-review.md](reference-review.md)、全文献と本文の引用位置は [reference-index.md](reference-index.md) にまとめています。

PDFでは引用番号から文献へ移動でき、参考文献末尾の引用ページ番号から本文へ戻れます（`backref=true`）。一覧の更新は `python3 scripts/build_reference_index.py` で行います。
