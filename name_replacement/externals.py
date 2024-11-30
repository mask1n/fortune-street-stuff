import locale
import platform
import langcodes
import pycountry

languages = ['en','ja','dk','de','es','fr','it']

def map_windows_locale_to_standard(locale_name):
    parts = locale_name.split('_')
    if len(parts) == 2:
        language_name, country_name = parts

        # Get the ISO 639-1 language code
        language_code = langcodes.find(language_name).language

        # Get the ISO 3166-1 alpha-2 country code
        country = pycountry.countries.get(name=country_name)
        country_code = country.alpha_2 if country else ''

        if language_code and country_code:
            return f"{language_code}_{country_code}"

    return None  # Return None if mapping is not possible

lng = locale.getlocale()[0]

match platform.system():
    case 'Windows':
        user_lang = map_windows_locale_to_standard(lng)[:2]
    case 'Darwin':
        user_lang = lng[:2]
    case 'Linux':
        user_lang = lng[:2]

## Used to sanity check user input
## Incompatible names will be rejected, and user will be asked to re-input
character_set = set(r""" !"#$%&'()*+,-./0123456789:;<=>?@
ABCDEFGHIJKLMNOPQRSTUVWXYZ
[\]^_`
abcdefghijklmnopqrstuvwxyz
{|}~¡¢£¥¦§¨©ª«®°±²³´µ·¹º»¿
ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÑÒÓÔÕÖ×ØÙÚÛÜÝß
àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýÿ
ŒœŸ
ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ
αβγδεζηθικλμνξοπρστυφχψω
–—―‘’,“”„•…※€™⬅⬆➡⬇∞∴■□▲△▼▽◆◇○◎●★☆♪♭
　、。々「」〒
ぁあぃいぅうぇえぉお
かがきぎくぐけげこご
さざしじすずせぜそぞ
ただちぢっつづてでとど
なにぬねの
はばぱひびぴふぶぷへべぺほぼぽ
まみむめも
ゃやゅゆょよ
らりるれろ
ゎわをん
ァアィイゥウェエォオ
カガキギクグケゲコゴ
サザシジスズセゼソゾ
タダチヂッツヅテデトド
ナニヌネノ
ハバパヒビピフブプヘベペホボポ
マミムメモ
ャヤュユョヨ
ラリルレロ
ヮワヲンヴヵヶ・ー
一万三上下不世並中主乗乙事二交人今仕
他以件伊伏会伝位体何作使価侶便信倍値
備像僧優元兄先児入全公内冒凡刀分切初
制券前力加勇動務勝匹占原去参友収取受
合名向君吟呪品員商回団固国圧地城域報
場増士変夢大天奉女好妨姉始姫婦子孤学
宇守安宙定実客害家容対専将小少屋履山
島工帝師平年幸幽店庭庶式弓引張強弾当
形彩待後心忍志快念性悪情慎成戦所手投
択押拳持指掛探接揚換撃攻数敵文料断新
方旅族日星暴曲更替最月服本朴条来柄柱
校株格検業構様標横機正武歩死殿母民気
水汁決法派流海消淑深済渉渡満潔潜火無
焼爆父版物特狙独狼玉王球理生産用由男
界番癖登白的皇盗目直相真着研破確社神
税究空突立笑算米粋純級素紫紳紺結続緑
編縞縦績署羊羽習老者肉育胆脚腕自般船
色花芸茶草菜蓄薄虹行術覇見視覧解計記
設証試詩誠論謎警豪負貢貯貴買資賊賞賢
赤超足跡踊軍転迷追逆通速連遊運道達選
遺配重野金鉄録鍋長開間関闘除険隊階隣
集雲雷霊青項順頑額風飛食飼騎高魔魚鳴
鶴麺黄黒
！％＆（）＋，／
０１２３４５６７８９？
ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ
ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ
～￥
""")

if __name__ == '__main__':
    print(user_lang)