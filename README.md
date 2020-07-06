## Environment

* WSL(Ubuntu 18.04.4 LTS)
* Python 3.8.1
  * numpy 1.15.0
  * scipy 1.5.0
  * pandas 1.0.5
  * scikit-learn 0.23.1
  * mecab-python3 1.0.0
  * neologdn 0.4
  * Keras 2.4.3
  * gensim 3.8.3

## 2. Reference

* [『15Stepで踏破 自然言語処理アプリケーション開発入門 (StepUp!選書)』](https://bookmeter.com/books/14438482)
* [NumPy v1.19 Manual](https://numpy.org/doc/stable/)
* [SciPy](https://www.scipy.org/docs.html)
* [pandas](https://pandas.pydata.org/docs/)
* [scikit-laern](https://scikit-learn.org/stable/user_guide.html)
* [mecab](https://taku910.github.io/mecab/)
* [neologd](https://github.com/neologd/mecab-ipadic-neologd)
* [Regexp.ja](https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja)
* [Keras](https://keras.io/guides/)
* [gensim](https://radimrehurek.com/gensim/auto_examples/index.html)

## 3. Setup

* Install all required liblaries

```bash
$ pip install -r requirements.txt
```

* Install mecab to execute command line
  * Debian / Ubuntu

  ```bash
  $ sudo apt install mecab libmecab-dev mecab-ipadic-utf8
  ```

  * MacOS

  ```bash
  $ brew install mecab mecab-ipadic-utf8
  ```
