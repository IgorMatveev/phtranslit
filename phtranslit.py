import sys
sys.path.append('./English-to-IPA')
import eng_to_ipa as ipa

d = {
	"ə":"э",
	"e":"эй",
	"ɑ":"а",
	"æ":"э",
	"ʌ":"а",
	"ɔ":"о",
	"aʊ":"ау",
	"aɪ":"ай",
	"ʧ":"ч",
	"ð":"з",
	"ɛ":"э",
	"ər":"э",
	"h":"х",
	"ɪ":"и",
	"ʤ":"дж",
	"ŋ":"нг",
	"oʊ":"оу",
	"ɔɪ":"ой",
	"ʃ":"ш",
	"θ":"с",
	"ʊ":"у",
	"u":"у",
	"ʒ":"ж",
	"i":"и",
	"j":"й",
	"b":"б",
	"d":"д",
	"f":"ф",
	"g":"г",
	"k":"к",
	"l":"л",
	"m":"м",
	"n":"н",
	"p":"п",
	"r":"р",
	"s":"с",
	"t":"т",
	"v":"в",
	"w":"в",
	"z":"з"
}

def eng_to_rus(eng_str):
	return ipa_to_rus(ipa.convert(eng_str))

def ipa_to_rus(ipa_str):
	if ipa_str[-1] == "*":
		return None
	punct_str = 'ˌˈ!"#$%&\'()*+,-./:;<=>/?@[\\]^_`{|}~«»'
	keys = d.keys()
	res = ""
	i = 0
	while i < len(ipa_str):
		# print(ipa_str[i:i+2], ipa_str[i:i+1])
		if ipa_str[i:i+2] in keys:
			res += d[ipa_str[i:i+2]]
			i += 2
		elif ipa_str[i:i+1] in punct_str:
			i += 1
		elif ipa_str[i:i+1] == ' ':
			res += ipa_str[i:i+1]
			i += 1
		else:
			res += d[ipa_str[i:i+1]]
			i += 1
	return res