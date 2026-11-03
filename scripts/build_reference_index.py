"""参考文献の書誌情報と本文の使用箇所を reference-index.md に出力する。"""
from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
bib = (root / 'references.bib').read_text(encoding='utf-8')
entries = {}
starts = list(re.finditer(r'^@\w+\{([^,]+),', bib, re.M))
for i, m in enumerate(starts):
    block = bib[m.end():starts[i+1].start() if i+1 < len(starts) else len(bib)]
    fields = dict(re.findall(r'^\s*(\w+)\s*=\s*\{(.*)\},?\s*$', block, re.M))
    entries[m[1]] = (fields, bib[:m.start()].count('\n') + 1)
uses = {}
for p in sorted((root / 'chapters').glob('*.tex')):
    for line, text in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
        text = re.split(r'(?<!\\)%', text)[0]
        for m in re.finditer(r'\\(?:cite|parencite|textcite|autocite)(?:\[[^]]*\])*\{([^}]+)\}', text):
            for key in m[1].split(','):
                item = (p, line, text)
                if item not in uses.setdefault(key.strip(), []):
                    uses[key.strip()].append(item)
missing = set(uses) - set(entries)
if missing:
    raise SystemExit('未登録引用: ' + ', '.join(sorted(missing)))

def plain(s):
    return s.replace('{', '').replace('}', '').replace('\\&', '&')

out = ['# 参考文献・引用箇所の一覧', '',
       '本文の引用箇所と `references.bib` から生成した一覧です。文献の内容がすべて検証済みという意味ではありません。今回の7件の照合結果は [reference-review.md](reference-review.md) を参照してください。', '',
       '文献名・キー・本文の言葉は検索で探せます。各「本文」リンクで引用箇所、「書誌」リンクで `.bib` の定義、「原典」で論文・公式資料を開けます。', '',
       f'登録 {len(entries)} 件／本文で引用 {len(uses)} 件／未登録 {len(missing)} 件。', '',
       '更新コマンド: `python3 scripts/build_reference_index.py`（thesis-uplatex 内から実行）。', '']
for cited, heading in [(True, '本文で引用している文献'), (False, '登録済みだが本文では未引用')]:
    out += ['## ' + heading, '']
    for key, (fields, line) in entries.items():
        if (key in uses) != cited:
            continue
        out += [f'### {key}', '', '**' + plain(fields.get('title', key)) + '**', '',
                plain(fields.get('author', '')) + ' / ' + fields.get('year', '年記載なし'), '',
                f'[書誌の定義]({root / "references.bib"}:{line})']
        if fields.get('url'): out[-1] += f' · [原典]({fields["url"]})'
        if fields.get('doi'): out[-1] += f' · [DOI](https://doi.org/{fields["doi"]})'
        out += ['']
        for p, number, text in uses.get(key, []):
            out += [f'- [本文：{p.name}:{number}]({p}:{number})', '', '  ' + text, '']
(root / 'reference-index.md').write_text('\n'.join(out), encoding='utf-8')
print(f'Index: {len(entries)} entries, {len(uses)} cited keys, no missing keys')
