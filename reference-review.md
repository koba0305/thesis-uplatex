# 未登録だった7件の照合結果

確認日：2026-10-29。編集対象は `thesis-uplatex`。元の `thesis` は変更していません。

7件に対応する原典が見つかったため、似た別文献を割り当てるのではなく、書誌情報を追加し、本文の引用キーを整理しました。著者名・機能・研究結果の食い違いは下記のとおりです。今回は該当する主張と書誌情報の照合であり、論文全体の査読や、既存文献すべての妥当性確認ではありません。
こ
[全参考文献と引用箇所の一覧](reference-index.md) では、本文の行・書誌の定義・原典へ移動できます。

| 旧キー | 新キー | 判断 |
| --- | --- | --- |
| `morgan2019` | `morgan2019calculated` | 圧縮アーティファクトの記述と一致する2019年論文を登録 |
| `appleLivePhotoWallpaper` | `apple_live_photo_wallpaper` | AppleのLive Photos壁紙の公式資料を登録 |
| `appleSpatialScene` | `apple_ios26_spatial_scenes` | iOS 26の空間シーンの公式資料を登録 |
| `parikh2020preferences` | `parikh2020generative` | 著者・311名・選好の内容が一致する論文を登録 |
| `interactiveArtEngagement` | `krzyzaniak2022engaging` | パラメータ追加と滞在時間を検証した論文を登録。一般化を弱めた |
| `bewellplus` | `lin2012bewellplus` | システムは実在。著者をMunsonからLinへ訂正 |
| `whoiszuki` | `murnane2020narrative` | WhoIsZukiを提案したCHI 2020論文を登録 |

## 1. Morgan：グリッチの外観と計算機構造

- [原典・要旨・PDF入口](https://aprja.net/article/view/115426)
- Carleigh Morgan, *Calculated Error: Glitch Art, Compression Artefacts, and Digital Materiality*, 2019, DOI: 10.7146/aprja.v8i1.115426。
- まず読む箇所：掲載ページの Abstract。圧縮アーティファクト、とくに macroblock の外観がハードウェア・ソフトウェアによって制約されるという記述。
- 本文第2章の「Morganは…圧縮方式によってその外観が規定…」に対応。本文の著者・主張は維持。
- 大学の登録情報には別タイトル表記があるため、書誌は出版社ページのタイトルを採用。未確認のページ範囲は登録していない。

## 2. Apple：Live Photos

- [公式資料](https://support.apple.com/ja-jp/120734)
- まず読む箇所：ページ冒頭。iOS 17以降で、ロック画面を起動するとLive Photosの画像が再生される説明。
- 本文第2章の「Live Photosを利用したロック画面のアニメーション」に対応。
- この資料は、第三者アプリ向け描画APIの有無まで説明する資料ではない。

## 3. Apple：空間シーン

- [iOS 26の新機能](https://support.apple.com/ja-jp/guide/iphone/iphfed2c4091/26/ios/26)
- [補助資料：壁紙の設定と対応条件](https://support.apple.com/ja-jp/102638)
- まず読む箇所：新機能の「ロック画面」、補助資料の「ロック画面用に3D写真の壁紙を作成する」。
- 端末を動かした際のロック画面写真の3D効果に対応。補助資料ではiPhone 12以降・iOS 26、対応写真、3D効果はロック画面のみという制約を確認できる。
- 要確認：本文でAndroidとのAPIの違いを厳密に論証する場合、Appleの機能紹介だけで「APIがない」という断定を支えないこと。

## 4. Parikh：生成アートの選好

- [会議公開PDF（4ページ）](https://computationalcreativity.net/iccc20/papers/096-iccc20.pdf)
- Devi Parikh, *Predicting a Creator's Preferences In, and From, Interactive Generative Art*, ICCC 2020, pp.484–487。
- まず読む箇所：PDF 1ページの Abstract / Introduction、評価・結論。
- 311名の選好データを使い、同じ生成アート内の選好の予測可能性を検討。食事や音楽など別領域の選好は偶然以上には予測できなかった。
- 訂正：本文を「制作時に選択した特徴の分析」から「調査で収集した選好の分析」へ修正。自由制作の行動ログそのものの研究と読まないこと。質問紙での自己申告の選好が含まれる。パーソナライズ一般の有効性を証明したとまでは言えない。

## 5. Krzyzaniakほか：インタラクティブアートへの関与

- [論文全文](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2022.859496/full)
- Michael Krzyzaniak, Çağri Erdem, Kyrre Glette, 2022。
- まず読む箇所：Study 1、2.4 Results、2.5 Discussion。
- 調整用スライダーのある条件とない条件を比較。分析対象は22名で、スライダーあり条件の能動的な滞在時間が長かった。
- 本文の「パラメータが多いほど」を、実際の比較条件と滞在時間の結果に合わせて修正。パラメータを無制限に増やせばよいとは原典も述べていない。

## 6. Linほか：BeWell+

- [著者側公開PDF（8ページ）](https://pac.cs.cornell.edu/pubs/wirelesshealth2012_BeWell.pdf)
- [DOI・書誌確認用の大学リポジトリ](https://cris.unibo.it/handle/11585/136035)
- まず読む箇所：PDF 1ページの著者・要旨、3ページの Figure 2 と aquatic ecosystem の説明。
- 身体活動は魚の動き、社会的交流は魚群、睡眠は海中の明るさで表す。
- 訂正：著者「Munsonら」→「Linら」。今回確認した原典はスマートフォンの壁紙を説明しているため、本文の「ロック画面および」は削除。

## 7. Murnaneほか：WhoIsZuki

- [著者側公開PDF（14ページ）](https://stanfordhci.github.io/zuki/chi2020/files/zuki_chi2020_ACM.pdf)
- Elizabeth L. Murnaneほか, *Designing Ambient Narrative-Based Interfaces to Reflect and Motivate Physical Activity*, CHI 2020, DOI: 10.1145/3313831.3376478。
- まず読む箇所：PDF 1ページの Figure 1 / Abstract、2ページのIntroduction。
- 身体活動・目標達成と物語の進行が結び付くスマートフォンシステム。ホーム画面・ロック画面への表示を原典で確認。本文のシステム説明を維持。

## 追加で確認してほしい箇所

- 第2章の Chai Wallpaper の「121名・2週間・カスタマイズ評価」は、現在引用する2023年の6ページの会議論文と同じ出典かを要確認。121名という数値は [著者の学位論文](https://dalspaceb.library.dal.ca/server/api/core/bitstreams/77b4e97a-defa-4124-b200-7d2fc502e2d5/content) の第5章・冊子p.69にある。今回の7件以外のため本文・引用は変更していない。2週間などの詳細も、採用する原典で照合すること。
- 「インタラクティブな対象に対する美的評価には個人差が存在することも示されている」の一文には、直接の引用が付いていない。前後の引用から自動的に証明されたと扱わないこと。

## PDFでの確認方法

- 本文の引用番号から参考文献へ移動できる。
- 参考文献末尾の `cit. on p.` / `cit. on pp.` に続くページ番号から、引用している本文ページへ戻れる（PDFビューアのリンク対応が必要）。
- DOI・URLから原典を開ける。
- 細かい本文行や `.bib` の編集位置は [reference-index.md](reference-index.md) が便利。文章を編集した後は生成スクリプトで一覧を更新する。
