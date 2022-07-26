# paseri

## Installation

先に[MeCab本体](https://taku910.github.io/mecab/)をインストールしてください。

次に下記の通りpaseriをインストールすると、自動的に以下がインストールされます。
- [mecab-python3](https://pypi.org/project/mecab-python3/)
- [pandas](https://pypi.org/project/pandas/)

```python
pip install git+https://github.com/suzuna/paseri.git
# or
pip install git+git://github.com/suzuna/paseri.git
```

## Usage

```python
from paseri import Paseri

# MeCab.Tagger()の引数であるrawargsにおいて"-Ochasen"以外のargsを渡さない場合は、かっこ内に何も書かない
pas = Paseri()
pas.parse("国境の長いトンネルを抜けると雪国であった。")
```

| |surface|pos|pos1|pos2|pos3|form1|form2|base|yomi|hatsuon|
|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
|0|国境|名詞|一般|\*|\*|\*|\*|国境|コッキョウ|コッキョー|
|1|の|助詞|格助詞|一般|\*|\*|\*|の|ノ|ノ|
|2|長い|形容詞|自立|\*|\*|形容詞・アウオ段|基本形|長い|ナガイ|ナガイ|
|3|トンネル|名詞|一般|\*|\*|\*|\*|トンネル|トンネル|トンネル|
|4|を|助詞|格助詞|一般|\*|\*|\*|を|ヲ|ヲ|
|5|抜ける|動詞|自立|\*|\*|一段|基本形|抜ける|ヌケル|ヌケル|
|6|と|助詞|接続助詞|\*|\*|\*|\*|と|ト|ト|
|7|雪国|名詞|一般|\*|\*|\*|\*|雪国|ユキグニ|ユキグニ|
|8|で|助動詞|\*|\*|\*|特殊・ダ|連用形|だ|デ|デ|
|9|あっ|助動詞|\*|\*|\*|五段・ラ行アル|連用タ接続|ある|アッ|アッ|
|10|た|助動詞|\*|\*|\*|特殊・タ|基本形|た|タ|タ|
|11|。|記号|句点|\*|\*|\*|\*|。|。|。|


```python
# MeCab.Tagger()の引数であるrawargsにおいて"-Ochasen"以外のargsを渡す場合はMeCab.Tagger("-Ochasen ...")の...と同じ記法で記載する
pas = Paseri("-r /hoge/fuga/.mecabrc")
# 以下同様
```
