### phtranslit

Phonetic transliteration from English to Russian.

Based on the lib [English-to-IPA](https://github.com/mphilli/English-to-IPA) by [mphilli](https://github.com/mphilli) with some changes

#### Usage

```Python
from phtranslit import eng_to_rus
eng_to_rus("The quick brown fox jumped over the lazy dog.")
'за квик браун факс джампт оувэ за лэйзи дог'
```

Method works only on 130K words in list `English-to-IPA/eng_to_ipa/resoutces/CMU_source_files/cmudict-0.7b.txt`. If a word isn't in the list, method returns None

```Python
eng_to_rus("ozon")
# None
```
