from math import log
from typing import List

def get_characters_list() -> List[str]: 
    return      ["'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4',
                '5', '6','7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E',
                'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', ' ', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z', 'p', '\n', '…', '!', '’', '→', '‘', '“', '”', '{', '}', '"', '&', '—', '×',
                '–', '%', '#', 'ض', 'ص', 'ث', 'ق',
                'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'د', 'ط', 'ك', 'م', 'ن', 'ت', 'ا', 'ل'
                ,'ب', 'ي', 'س', 'ش', 'ئ', 'ء', 'ؤ', 'ر', 'ﻻ', 'ى', 'ة', 'و', 'ز', 'ظ','|',"ˈ","ɪ",'ɛ','ʁ',
                'ʔ', 'ʃ', 'ü', 'ö', 'ć', '\t', 'ô', 'é', 'ä', 'ó', 'Ă', '$', 'İ', 'á', 'ï', 'î', 'Ü'
                ,'ø', 'ß', 'æ', 'Ö', 'í', 'à', 'Б', 'е', 'л', 'а', 'р', 'у', 'с', 'к', 'я', 'ی', 'ç', 'Հ', 'ա',
                'յ', 'ե', 'ր', 'ն', '®','Χ', 'Ψ', 'Ω', 'Ϊ', 'Ϋ', 'ά', 'έ', 'ή', 'ί', 'ΰ', 'α', 'β', 'γ',
                'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'ς',
                'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω', 'ϊ', 'ϋ', 'ό', 'ύ', 'ώ', 'Ϗ', 'ϐ', 'ϑ',
                'ϒ', 'ϓ', 'ϔ', 'ϕ', 'ϖ', 'ϗ', 'Ϙ', 'ϙ', 'Ϛ', 'ϛ', 'Ϝ', 'ϝ', 'Ϟ', 'ϟ', 'Ϡ','Ĥ'
                , 'ϡ', 'Ϣ', 'ϣ', 'Ϥ', 'ϥ', 'Ϧ', 'ϧ','Ɗ', 'Ƌ', 'ƌ', 'ƍ', 'Ǝ', 'Ə', 'Ɛ', 'Ɠ', '~', "¡","¢","£","¤","¥","¦","§","¨","©","ª","«","¬","­","¯","°","±","²","³","´","µ","¶","·","¸","¹","º","»","¼","½","¾","¿","À","Á","Â","Ã","Ä","Å","Æ","Ç","È","É","Ê","Ë","Ì","Í","Î","Ï","Ð","Ñ","Ò","Ó","Ô","Õ","Ø","Ù","Ú","Û","Ý","Þ","â","ã","å","è","ê","ë","ì","ð","ñ","ò","õ","÷","ù","ú","û","ý","þ","ÿ","Ā","ā","ă","Ą","ą","Ć","Ĉ","ĉ","Ċ","ċ","Č","č","Ď","ď","Đ","đ","Ē","ē","Ĕ","ĕ","Ė","ė","Ę","ę","Ě","ě","Ĝ","ĝ","Ğ","ğ","Ġ","ġ","Ģ","ģ","ĥ","Ħ","ħ","Ĩ","ĩ","Ī","ī","Ĭ","ĭ","Į","į","ı","Ĳ","ĳ","Ĵ","ĵ","Ķ","ķ","ĸ","Ĺ","ĺ","Ļ","ļ","Ľ","ľ","Ŀ","ŀ","Ł","ł","Ń","ń","Ņ","ņ","Ň","ň","ŉ","Ŋ","ŋ","Ō","ō","Ŏ","ŏ","Ő","ő","Œ","œ","Ŕ","ŕ","Ŗ","ŗ","Ř","ř","Ś","ś","Ŝ","ŝ","Ş","ş","Š","š","Ţ","ţ","Ť","ť","Ŧ","ŧ","Ũ","ũ","Ū","ū","Ŭ","ŭ","Ů","ů","Ű","ű","Ų","ų","Ŵ","ŵ","Ŷ","ŷ","Ÿ","Ź","ź","Ż","ż","Ž","ž","ſ","ƀ","Ɓ","Ƃ","ƃ","Ƅ","ƅ","Ɔ","Ƈ","ƈ","Ɖ","Ƒ","ƒ","Ɣ","ƕ","Ɩ","Ɨ","Ƙ","ƙ","ƚ","ƛ","Ɯ","Ɲ","ƞ","Ɵ","Ơ","ơ","Ƣ","ƣ","Ƥ","ƥ","Ʀ","Ƨ","ƨ","Ʃ","ƪ","ƫ","Ƭ","ƭ","Ʈ","Ư","ư","Ʊ","Ʋ","Ƴ","ƴ","Ƶ","ƶ","Ʒ","Ƹ","ƹ","ƺ","ƻ","Ƽ","ƽ","ƾ","ƿ","ǀ","ǁ","ǂ","ǃ","Ǆ","ǅ","ǆ","Ǉ","ǈ","ǉ","Ǌ","ǋ","ǌ","Ǎ","ǎ","Ǐ","ǐ","Ǒ","ǒ","Ǔ","ǔ","Ǖ","ǖ","Ǘ","ǘ","Ǚ","ǚ","Ǜ","ǜ","ǝ","Ǟ","ǟ","Ǡ","ǡ","Ǣ","ǣ","Ǥ","ǥ","Ǧ","ǧ","Ǩ","ǩ","Ǫ","ǫ","Ǭ","ǭ","Ǯ","ǯ","ǰ","Ǳ","ǲ","ǳ","Ǵ","ǵ","Ƕ","Ƿ","Ǹ","ǹ","Ǻ","ǻ","Ǽ","ǽ","Ǿ","ǿ","Ȁ","ȁ","Ȃ","ȃ","Ȅ","ȅ","Ȇ","ȇ","Ȉ","ȉ","Ȋ","ȋ","Ȍ","ȍ","Ȏ","ȏ","Ȑ","ȑ","Ȓ","ȓ","Ȕ","ȕ","Ȗ","ȗ","Ș","ș","Ț","ț","Ȝ","ȝ","Ȟ","ȟ","Ƞ","ȡ","Ȣ","ȣ","Ȥ","ȥ","Ȧ","ȧ","Ȩ","ȩ","Ȫ","ȫ","Ȭ","ȭ","Ȯ","ȯ","Ȱ","ȱ","Ȳ","ȳ","ȴ","ȵ","ȶ","ȷ","ȸ","ȹ","Ⱥ","Ȼ","ȼ","Ƚ","Ⱦ","ȿ","ɀ","Ɂ","ɂ","Ƀ","Ʉ","Ʌ","Ɇ","ɇ","Ɉ","ɉ","Ɋ","ɋ","Ɍ","ɍ","Ɏ","ɏ","ɐ","ɑ","ɒ","ɓ","ɔ","ɕ","ɖ","ɗ","ɘ","ə","ɚ","ɜ","ɝ","ɞ","ɟ","ɠ","ɡ","ɢ","ɣ","ɤ","ɥ","ɦ","ɧ","ɨ","ɩ","ɫ","ɬ","ɭ","ɮ","ɯ","ɰ","ɱ","ɲ","ɳ","ɴ","ɵ","ɶ","ɷ","ɸ","ɹ","ɺ","ɻ","ɼ","ɽ","ɾ","ɿ","ʀ","ʂ","ʄ","ʅ","ʆ","ʇ","ʈ","ʉ","ʊ","ʋ","ʌ","ʍ","ʎ","ʏ","ʐ","ʑ","ʒ","ʓ","ʕ","ʖ","ʗ","ʘ","ʙ","ʚ","ʛ","ʜ","ʝ","ʞ","ʟ","ʠ","ʡ","ʢ","ʣ","ʤ","ʥ","ʦ","ʧ","ʨ","ʩ","ʪ","ʫ","ʬ","ʭ","ʮ","ʯ","ʰ","ʱ","ʲ","ʳ","ʴ","ʵ","ʶ","ʷ","ʸ","ʹ","ʺ","ʻ","ʼ","ʽ","ʾ","ʿ","ˀ","ˁ","˂","˃","˄","˅","ˆ","ˇ","ˉ","ˊ","ˋ","ˌ","ˍ","ˎ","ˏ","ː","ˑ","˒","˓","˔","˕","˖","˗","˘","˙","˚","˛","˜","˝","˞","˟","ˠ","ˡ","ˢ","ˣ","ˤ","˥","˦","˧","˨","˩","˪","˫","ˬ","˭","ˮ","˯","˰","˱","˲","˳","˴","˵","˶","˷","˸","˹","˺","˻","˼","˽","˾","˿","̀","́","̂","̃","̄","̅","̆","̇","̈","̉","̊","̋","̌","̍","̎","̏","̐","̑","̒","̓","̔","̕","̖","̗","̘","̙","̚","̛","̜","̝","̞","̟","̠","̡","̢","̣","̤","̥","̦","̧","̨","̩","̪","̫","̬","̭","̮","̯","̰","̱","̲","̳","̴","̵","̶","̷","̸","̹","̺","̻","̼","̽","̾","̿","̀","́","͂","̓","̈́","ͅ","͆","͇","͈","͉","͊","͋","͌","͍","͎","͏","͐","͑","͒","͓","͔","͕","͖","͗","͘","͙","͚","͛","͜","͝","͞","͟","͠","͡","͢","ͣ","ͤ","ͥ","ͦ","ͧ","ͨ","ͩ","ͪ","ͫ","ͬ","ͭ","ͮ","ͯ","Ͱ","ͱ","Ͳ","ͳ","ʹ","͵","Ͷ","ͷ","͸","͹","ͺ","ͻ","ͼ","ͽ",";","Ϳ","΀","΁","΂","΃","΄","΅","Ά","·","Έ","Ή","Ί","΋","Ό","΍","Ύ","Ώ","ΐ","Α","Β","Γ","Δ","Ε","Ζ","Η","Θ","Ι","Κ","Λ","Μ","Ν","Ξ","Ο","Π","Ρ","΢","Σ","Τ","Υ","Φ", 'Ϩ', 'ϩ', 'Ϫ', 'ϫ', 'Ϭ', 'ϭ', 'Ϯ', 'ϯ', 'ϰ', 'ϱ', 'ϲ', 'ϳ', 'ϴ', 'ϵ', '϶', 'Ϸ', 'ϸ', 'Ϲ', 'Ϻ', 'ϻ', 'ϼ', 'Ͻ', 'Ͼ', 'Ͽ', 'Ѐ', 'Ё', 'Ђ', 'Ѓ', 'Є', 'Ѕ', 'І']

    

BITS_SIZE = int(log(len(get_characters_list()), 2))
