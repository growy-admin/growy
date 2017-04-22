# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import re

def replaceIfPresent(item, from_key, to_key, transform=lambda x : x):
    x = item.pop(from_key, None)
    if x is not None:
        item[to_key] = transform(x)


def lifeCycleTranslator(val):
    if val == u'Ettårig':
        return u'Annual'
    elif val == u'Tvåårig':
        return u'Biennial'
    elif val == u'Flerårig':
        return u'Perennial'

def plantTypeTranslator(val):
    tr = {}
    tr[u'Grönsaker'] = 'TBD'
    tr[u'Bönor &amp; ärter'] = 'TBD'
    tr[u'Brytböna'] = 'TBD'
    tr[u'Purpurböna'] = 'TBD'
    tr[u'Vaxböna'] = 'TBD'
    tr[u'Skärböna'] = 'TBD'
    tr[u'Spritböna'] = 'TBD'
    tr[u'Bönmix'] = 'TBD'
    tr[u'Störböna'] = 'TBD'
    tr[u'Blomsterböna'] = 'TBD'
    tr[u'Bondböna'] = 'TBD'
    tr[u'Brytärt'] = 'TBD'
    tr[u'Märgärt'] = 'TBD'
    tr[u'Sockerärt'] = 'TBD'
    tr[u'Spritärt'] = 'TBD'
    tr[u'Sparrisärt'] = 'TBD'
    tr[u'Fruktgrönsaker'] = 'TBD'
    tr[u'Majs'] = 'TBD'
    tr[u'Gurka'] = 'TBD'
    tr[u'Kalebass'] = 'TBD'
    tr[u'Melon'] = 'TBD'
    tr[u'Sommarsquash'] = 'TBD'
    tr[u'Pumpa'] = 'TBD'
    tr[u'Vintersquash'] = 'TBD'
    tr[u'Paprika'] = 'TBD'
    tr[u'Chilipeppar'] = 'TBD'
    tr[u'Odla tomat'] = 'TBD'
    tr[u'Busktomat'] = 'TBD'
    tr[u'Högväxande tomat'] = 'TBD'
    tr[u'Körsbärstomater'] = 'TBD'
    tr[u'Pastatomater'] = 'TBD'
    tr[u'Gyllenbär'] = 'TBD'
    tr[u'Pastatomater'] = 'TBD'
    tr[u'Gyllenbär'] = 'TBD'
    tr[u'Tomatillo'] = 'TBD'
    tr[u'Äggplanta'] = 'TBD'
    tr[u'Kålväxter'] = 'TBD'
    tr[u'Odla kålväxter'] = 'TBD'
    tr[u'Blomkål'] = 'TBD'
    tr[u'Broccoli'] = 'TBD'
    tr[u'Broccolo'] = 'TBD'
    tr[u'Brysselkål'] = 'TBD'
    tr[u'Grönkål'] = 'TBD'
    tr[u'Rödkål'] = 'TBD'
    tr[u'Salladskål'] = 'TBD'
    tr[u'Savoykål'] = 'TBD'
    tr[u'Spetskål'] = 'TBD'
    tr[u'Vitkål'] = 'TBD'
    tr[u'Kålrabbi'] = 'TBD'
    tr[u'Sallad och bladväxter'] = 'TBD'
    tr[u'Asiatiska bladgrönsaker'] = 'TBD'
    tr[u'Stjälk-/Bladselleri'] = 'TBD'
    tr[u'Dill'] = 'TBD'
    tr[u'Persilja'] = 'TBD'
    tr[u'Sallats- och drivcikoria'] = 'TBD'
    tr[u'Radicchio'] = 'TBD'
    tr[u'Escarole- och friséesallat'] = 'TBD'
    tr[u'Sallat, Bataviasallat'] = 'TBD'
    tr[u'Cossallat'] = 'TBD'
    tr[u'Huvudsallat'] = 'TBD'
    tr[u'Isbergssallat'] = 'TBD'
    tr[u'Plocksallat'] = 'TBD'
    tr[u'Vintersallat, Mâche'] = 'TBD'
    tr[u'Rucola'] = 'TBD'
    tr[u'Portulak'] = 'TBD'
    tr[u'Kardon'] = 'TBD'
    tr[u'Mangold'] = 'TBD'
    tr[u'Målla'] = 'TBD'
    tr[u'Spenat'] = 'TBD'
    tr[u'Nyzeeländsk spenat'] = 'TBD'
    tr[u'Isört'] = 'TBD'
    tr[u'Rotfrukter'] = 'TBD'
    tr[u'Morot'] = 'TBD'
    tr[u'Palsternacka'] = 'TBD'
    tr[u'Rotpersilja'] = 'TBD'
    tr[u'Rotselleri'] = 'TBD'
    tr[u'Kardborrerot'] = 'TBD'
    tr[u'Svartrot'] = 'TBD'
    tr[u'Haverrot'] = 'TBD'
    tr[u'Kålrot'] = 'TBD'
    tr[u'Majrova'] = 'TBD'
    tr[u'Rova'] = 'TBD'
    tr[u'Rädisa'] = 'TBD'
    tr[u'Daikon'] = 'TBD'
    tr[u'Rättika'] = 'TBD'
    tr[u'Rödbeta'] = 'TBD'
    tr[u'Lökväxter'] = 'TBD'
    tr[u'Gul- &amp; rödlök'] = 'TBD'
    tr[u'Purjolök'] = 'TBD'
    tr[u'Salladslök'] = 'TBD'
    tr[u'Purjolök'] = 'TBD'
    tr[u'Salladslök'] = 'TBD'
    tr[u'Övriga'] = 'TBD'
    tr[u'Comfrey'] = 'TBD'
    tr[u'Knölfänkål'] = 'TBD'
    tr[u'Kronärtskocka'] = 'TBD'
    tr[u'Rabarber'] = 'TBD'
    tr[u'Rankspenat'] = 'TBD'
    tr[u'Smultron'] = 'TBD'
    tr[u'Sparris'] = 'TBD'
    tr[u'Strandkål'] = 'TBD'
    tr[u'Kryddor'] = 'TBD'
    tr[u'Ettåriga'] = 'TBD'
    tr[u'Anis'] = 'TBD'
    tr[u'Basilika'] = 'TBD'
    tr[u'Epazote'] = 'TBD'
    tr[u'Gurkört'] = 'TBD'
    tr[u'Kamomill'] = 'TBD'
    tr[u'Kardbenedikt'] = 'TBD'
    tr[u'Koriander'] = 'TBD'
    tr[u'Kryddkrasse'] = 'TBD'
    tr[u'Kyndel'] = 'TBD'
    tr[u'Körvel'] = 'TBD'
    tr[u'Shiso - perilla'] = 'TBD'
    tr[u'Tagetes, krydd-'] = 'TBD'
    tr[u'Vattenkrasse'] = 'TBD'
    tr[u'Vinterportulak'] = 'TBD'
    tr[u'Tvååriga'] = 'TBD'
    tr[u'Fänkål'] = 'TBD'
    tr[u'Kvanne'] = 'TBD'
    tr[u'Kummin'] = 'TBD'
    tr[u'Nattljus'] = 'TBD'
    tr[u'Vinterkrasse - vårgyllen'] = 'TBD'
    tr[u'Fleråriga'] = 'TBD'
    tr[u'Anisisop'] = 'TBD'
    tr[u'Citronmeliss'] = 'TBD'
    tr[u'Dragon'] = 'TBD'
    tr[u'Gräslök'] = 'TBD'
    tr[u'Isop'] = 'TBD'
    tr[u'Johannesört'] = 'TBD'
    tr[u'Kamomill, romersk'] = 'TBD'
    tr[u'Lavendel'] = 'TBD'
    tr[u'Libsticka'] = 'TBD'
    tr[u'Läkemalva'] = 'TBD'
    tr[u'Malört'] = 'TBD'
    tr[u'Mejram'] = 'TBD'
    tr[u'Mexikansk dragon'] = 'TBD'
    tr[u'Mynta'] = 'TBD'
    tr[u'Oregano'] = 'TBD'
    tr[u'Pimpinell'] = 'TBD'
    tr[u'Ramslök'] = 'TBD'
    tr[u'Rosmarin'] = 'TBD'
    tr[u'Salvia'] = 'TBD'
    tr[u'Spansk körvel'] = 'TBD'
    tr[u'Stevia, Sötflockel'] = 'TBD'
    tr[u'Syra'] = 'TBD'
    tr[u'Temynta'] = 'TBD'
    tr[u'Timjan'] = 'TBD'
    tr[u'Temynta'] = 'TBD'
    tr[u'Timjan'] = 'TBD'
    tr[u'Valeriana-Vänderot'] = 'TBD'
    tr[u'Vinruta'] = 'TBD'
    tr[u'Blommor'] = 'TBD'
    tr[u'Ettåriga, annueller A-N'] = 'TBD'
    tr[u'Amarant'] = 'TBD'
    tr[u'Aster'] = 'TBD'
    tr[u'Atlasblomma'] = 'TBD'
    tr[u'Ballongblomma'] = 'TBD'
    tr[u'Blomman för dagen'] = 'TBD'
    tr[u'Blomsterlin'] = 'TBD'
    tr[u'Clarkia'] = 'TBD'
    tr[u'Doroteablomma'] = 'TBD'
    tr[u'Gullskära'] = 'TBD'
    tr[u'Heliotrop'] = 'TBD'
    tr[u'Hänglobelia'] = 'TBD'
    tr[u'Inkakrage'] = 'TBD'
    tr[u'Jungfrun i det gröna'] = 'TBD'
    tr[u'Jätteeternell'] = 'TBD'
    tr[u'Klint'] = 'TBD'
    tr[u'Klockranka'] = 'TBD'
    tr[u'Klätt'] = 'TBD'
    tr[u'Krasse'] = 'TBD'
    tr[u'Lejongap'] = 'TBD'
    tr[u'Luktärt'] = 'TBD'
    tr[u'Lövkoja, grekisk'] = 'TBD'
    tr[u'Mariatistel'] = 'TBD'
    tr[u'Nemesia'] = 'TBD'
    tr[u'Ettåriga, annueller O-Ö'] = 'TBD'
    tr[u'Paradisblomster'] = 'TBD'
    tr[u'Praktmalva'] = 'TBD'
    tr[u'Praktvädd'] = 'TBD'
    tr[u'Prins Gustavs Öga'] = 'TBD'
    tr[u'Prydnadsmajs'] = 'TBD'
    tr[u'Prydnadskål'] = 'TBD'
    tr[u'Reseda'] = 'TBD'
    tr[u'Ricin'] = 'TBD'
    tr[u'Riddarsporre'] = 'TBD'
    tr[u'Ringblomma'] = 'TBD'
    tr[u'Risp'] = 'TBD'
    tr[u'Rosenskära'] = 'TBD'
    tr[u'Rudbeckia'] = 'TBD'
    tr[u'Solros'] = 'TBD'
    tr[u'Snokört'] = 'TBD'
    tr[u'Sommardahlia'] = 'TBD'
    tr[u'Sommarlövkoja'] = 'TBD'
    tr[u'Sommarmalva'] = 'TBD'
    tr[u'Sommarslöja'] = 'TBD'
    tr[u'Sömntuta'] = 'TBD'
    tr[u'Tagetes'] = 'TBD'
    tr[u'Vallmo, ettåriga'] = 'TBD'
    tr[u'Zinnia'] = 'TBD'
    tr[u'Ängsväxter; se under fleråriga blommor'] = 'TBD'
    tr[u'Tvååriga blommor, bienner'] = 'TBD'
    tr[u'Borstnejlika'] = 'TBD'
    tr[u'Fingerborgsblomma'] = 'TBD'
    tr[u'Gyllenlack'] = 'TBD'
    tr[u'Fingerborgsblomma'] = 'TBD'
    tr[u'Gyllenlack'] = 'TBD'
    tr[u'Kungsljus'] = 'TBD'
    tr[u'Nattviol'] = 'TBD'
    tr[u'Stockros'] = 'TBD'
    tr[u'Vävarkarda'] = 'TBD'
    tr[u'Fleråriga blommor, perenner'] = 'TBD'
    tr[u'Akleja'] = 'TBD'
    tr[u'Berglin'] = 'TBD'
    tr[u'Blågull'] = 'TBD'
    tr[u'Humle'] = 'TBD'
    tr[u'Japansk Lykta'] = 'TBD'
    tr[u'Jätteverbena'] = 'TBD'
    tr[u'Karpaterklocka'] = 'TBD'
    tr[u'Kungsljus'] = 'TBD'
    tr[u'Lupin'] = 'TBD'
    tr[u'Moses brinnande buske'] = 'TBD'
    tr[u'Myskmalva'] = 'TBD'
    tr[u'Praktriddarsporre'] = 'TBD'
    tr[u'Prästkrage'] = 'TBD'
    tr[u'Rosenmalva'] = 'TBD'
    tr[u'Rosenvial'] = 'TBD'
    tr[u'Rödmalva'] = 'TBD'
    tr[u'Röd rudbeckia /Solhatt'] = 'TBD'
    tr[u'Studentnejlika'] = 'TBD'
    tr[u'Såpnejlika'] = 'TBD'
    tr[u'Vallmo, fleråriga'] = 'TBD'
    tr[u'Ängsväxter'] = 'TBD'

    if val in tr:
        return tr[val]
    else:
        return 'Unknown'

def plantSubTypeTranslator(val):
    tr = {}
    tr[u'Grönsaker'] = 'TBD'
    tr[u'Bönor &amp; ärter'] = 'TBD'
    tr[u'Brytböna'] = 'TBD'
    tr[u'Purpurböna'] = 'TBD'
    tr[u'Vaxböna'] = 'TBD'
    tr[u'Skärböna'] = 'TBD'
    tr[u'Spritböna'] = 'TBD'
    tr[u'Bönmix'] = 'TBD'
    tr[u'Störböna'] = 'TBD'
    tr[u'Blomsterböna'] = 'TBD'
    tr[u'Bondböna'] = 'TBD'
    tr[u'Brytärt'] = 'TBD'
    tr[u'Märgärt'] = 'TBD'
    tr[u'Sockerärt'] = 'TBD'
    tr[u'Spritärt'] = 'TBD'
    tr[u'Sparrisärt'] = 'TBD'
    tr[u'Fruktgrönsaker'] = 'TBD'
    tr[u'Majs'] = 'TBD'
    tr[u'Gurka'] = 'TBD'
    tr[u'Kalebass'] = 'TBD'
    tr[u'Melon'] = 'TBD'
    tr[u'Sommarsquash'] = 'TBD'
    tr[u'Pumpa'] = 'TBD'
    tr[u'Vintersquash'] = 'TBD'
    tr[u'Paprika'] = 'TBD'
    tr[u'Chilipeppar'] = 'TBD'
    tr[u'Odla tomat'] = 'TBD'
    tr[u'Busktomat'] = 'TBD'
    tr[u'Högväxande tomat'] = 'TBD'
    tr[u'Körsbärstomater'] = 'TBD'
    tr[u'Pastatomater'] = 'TBD'
    tr[u'Gyllenbär'] = 'TBD'
    tr[u'Pastatomater'] = 'TBD'
    tr[u'Gyllenbär'] = 'TBD'
    tr[u'Tomatillo'] = 'TBD'
    tr[u'Äggplanta'] = 'TBD'
    tr[u'Kålväxter'] = 'TBD'
    tr[u'Odla kålväxter'] = 'TBD'
    tr[u'Blomkål'] = 'TBD'
    tr[u'Broccoli'] = 'TBD'
    tr[u'Broccolo'] = 'TBD'
    tr[u'Brysselkål'] = 'TBD'
    tr[u'Grönkål'] = 'TBD'
    tr[u'Rödkål'] = 'TBD'
    tr[u'Salladskål'] = 'TBD'
    tr[u'Savoykål'] = 'TBD'
    tr[u'Spetskål'] = 'TBD'
    tr[u'Vitkål'] = 'TBD'
    tr[u'Kålrabbi'] = 'TBD'
    tr[u'Sallad och bladväxter'] = 'TBD'
    tr[u'Asiatiska bladgrönsaker'] = 'TBD'
    tr[u'Stjälk-/Bladselleri'] = 'TBD'
    tr[u'Dill'] = 'TBD'
    tr[u'Persilja'] = 'TBD'
    tr[u'Sallats- och drivcikoria'] = 'TBD'
    tr[u'Radicchio'] = 'TBD'
    tr[u'Escarole- och friséesallat'] = 'TBD'
    tr[u'Sallat, Bataviasallat'] = 'TBD'
    tr[u'Cossallat'] = 'TBD'
    tr[u'Huvudsallat'] = 'TBD'
    tr[u'Isbergssallat'] = 'TBD'
    tr[u'Plocksallat'] = 'TBD'
    tr[u'Vintersallat, Mâche'] = 'TBD'
    tr[u'Rucola'] = 'TBD'
    tr[u'Portulak'] = 'TBD'
    tr[u'Kardon'] = 'TBD'
    tr[u'Mangold'] = 'TBD'
    tr[u'Målla'] = 'TBD'
    tr[u'Spenat'] = 'TBD'
    tr[u'Nyzeeländsk spenat'] = 'TBD'
    tr[u'Isört'] = 'TBD'
    tr[u'Rotfrukter'] = 'TBD'
    tr[u'Morot'] = 'TBD'
    tr[u'Palsternacka'] = 'TBD'
    tr[u'Rotpersilja'] = 'TBD'
    tr[u'Rotselleri'] = 'TBD'
    tr[u'Kardborrerot'] = 'TBD'
    tr[u'Svartrot'] = 'TBD'
    tr[u'Haverrot'] = 'TBD'
    tr[u'Kålrot'] = 'TBD'
    tr[u'Majrova'] = 'TBD'
    tr[u'Rova'] = 'TBD'
    tr[u'Rädisa'] = 'TBD'
    tr[u'Daikon'] = 'TBD'
    tr[u'Rättika'] = 'TBD'
    tr[u'Rödbeta'] = 'TBD'
    tr[u'Lökväxter'] = 'TBD'
    tr[u'Gul- &amp; rödlök'] = 'TBD'
    tr[u'Purjolök'] = 'TBD'
    tr[u'Salladslök'] = 'TBD'
    tr[u'Purjolök'] = 'TBD'
    tr[u'Salladslök'] = 'TBD'
    tr[u'Övriga'] = 'TBD'
    tr[u'Comfrey'] = 'TBD'
    tr[u'Knölfänkål'] = 'TBD'
    tr[u'Kronärtskocka'] = 'TBD'
    tr[u'Rabarber'] = 'TBD'
    tr[u'Rankspenat'] = 'TBD'
    tr[u'Smultron'] = 'TBD'
    tr[u'Sparris'] = 'TBD'
    tr[u'Strandkål'] = 'TBD'
    tr[u'Kryddor'] = 'TBD'
    tr[u'Ettåriga'] = 'TBD'
    tr[u'Anis'] = 'TBD'
    tr[u'Basilika'] = 'TBD'
    tr[u'Epazote'] = 'TBD'
    tr[u'Gurkört'] = 'TBD'
    tr[u'Kamomill'] = 'TBD'
    tr[u'Kardbenedikt'] = 'TBD'
    tr[u'Koriander'] = 'TBD'
    tr[u'Kryddkrasse'] = 'TBD'
    tr[u'Kyndel'] = 'TBD'
    tr[u'Körvel'] = 'TBD'
    tr[u'Shiso - perilla'] = 'TBD'
    tr[u'Tagetes, krydd-'] = 'TBD'
    tr[u'Vattenkrasse'] = 'TBD'
    tr[u'Vinterportulak'] = 'TBD'
    tr[u'Tvååriga'] = 'TBD'
    tr[u'Fänkål'] = 'TBD'
    tr[u'Kvanne'] = 'TBD'
    tr[u'Kummin'] = 'TBD'
    tr[u'Nattljus'] = 'TBD'
    tr[u'Vinterkrasse - vårgyllen'] = 'TBD'
    tr[u'Fleråriga'] = 'TBD'
    tr[u'Anisisop'] = 'TBD'
    tr[u'Citronmeliss'] = 'TBD'
    tr[u'Dragon'] = 'TBD'
    tr[u'Gräslök'] = 'TBD'
    tr[u'Isop'] = 'TBD'
    tr[u'Johannesört'] = 'TBD'
    tr[u'Kamomill, romersk'] = 'TBD'
    tr[u'Lavendel'] = 'TBD'
    tr[u'Libsticka'] = 'TBD'
    tr[u'Läkemalva'] = 'TBD'
    tr[u'Malört'] = 'TBD'
    tr[u'Mejram'] = 'TBD'
    tr[u'Mexikansk dragon'] = 'TBD'
    tr[u'Mynta'] = 'TBD'
    tr[u'Oregano'] = 'TBD'
    tr[u'Pimpinell'] = 'TBD'
    tr[u'Ramslök'] = 'TBD'
    tr[u'Rosmarin'] = 'TBD'
    tr[u'Salvia'] = 'TBD'
    tr[u'Spansk körvel'] = 'TBD'
    tr[u'Stevia, Sötflockel'] = 'TBD'
    tr[u'Syra'] = 'TBD'
    tr[u'Temynta'] = 'TBD'
    tr[u'Timjan'] = 'TBD'
    tr[u'Temynta'] = 'TBD'
    tr[u'Timjan'] = 'TBD'
    tr[u'Valeriana-Vänderot'] = 'TBD'
    tr[u'Vinruta'] = 'TBD'
    tr[u'Blommor'] = 'TBD'
    tr[u'Ettåriga, annueller A-N'] = 'TBD'
    tr[u'Amarant'] = 'TBD'
    tr[u'Aster'] = 'TBD'
    tr[u'Atlasblomma'] = 'TBD'
    tr[u'Ballongblomma'] = 'TBD'
    tr[u'Blomman för dagen'] = 'TBD'
    tr[u'Blomsterlin'] = 'TBD'
    tr[u'Clarkia'] = 'TBD'
    tr[u'Doroteablomma'] = 'TBD'
    tr[u'Gullskära'] = 'TBD'
    tr[u'Heliotrop'] = 'TBD'
    tr[u'Hänglobelia'] = 'TBD'
    tr[u'Inkakrage'] = 'TBD'
    tr[u'Jungfrun i det gröna'] = 'TBD'
    tr[u'Jätteeternell'] = 'TBD'
    tr[u'Klint'] = 'TBD'
    tr[u'Klockranka'] = 'TBD'
    tr[u'Klätt'] = 'TBD'
    tr[u'Krasse'] = 'TBD'
    tr[u'Lejongap'] = 'TBD'
    tr[u'Luktärt'] = 'TBD'
    tr[u'Lövkoja, grekisk'] = 'TBD'
    tr[u'Mariatistel'] = 'TBD'
    tr[u'Nemesia'] = 'TBD'
    tr[u'Ettåriga, annueller O-Ö'] = 'TBD'
    tr[u'Paradisblomster'] = 'TBD'
    tr[u'Praktmalva'] = 'TBD'
    tr[u'Praktvädd'] = 'TBD'
    tr[u'Prins Gustavs Öga'] = 'TBD'
    tr[u'Prydnadsmajs'] = 'TBD'
    tr[u'Prydnadskål'] = 'TBD'
    tr[u'Reseda'] = 'TBD'
    tr[u'Ricin'] = 'TBD'
    tr[u'Riddarsporre'] = 'TBD'
    tr[u'Ringblomma'] = 'TBD'
    tr[u'Risp'] = 'TBD'
    tr[u'Rosenskära'] = 'TBD'
    tr[u'Rudbeckia'] = 'TBD'
    tr[u'Solros'] = 'TBD'
    tr[u'Snokört'] = 'TBD'
    tr[u'Sommardahlia'] = 'TBD'
    tr[u'Sommarlövkoja'] = 'TBD'
    tr[u'Sommarmalva'] = 'TBD'
    tr[u'Sommarslöja'] = 'TBD'
    tr[u'Sömntuta'] = 'TBD'
    tr[u'Tagetes'] = 'TBD'
    tr[u'Vallmo, ettåriga'] = 'TBD'
    tr[u'Zinnia'] = 'TBD'
    tr[u'Ängsväxter; se under fleråriga blommor'] = 'TBD'
    tr[u'Tvååriga blommor, bienner'] = 'TBD'
    tr[u'Borstnejlika'] = 'TBD'
    tr[u'Fingerborgsblomma'] = 'TBD'
    tr[u'Gyllenlack'] = 'TBD'
    tr[u'Fingerborgsblomma'] = 'TBD'
    tr[u'Gyllenlack'] = 'TBD'
    tr[u'Kungsljus'] = 'TBD'
    tr[u'Nattviol'] = 'TBD'
    tr[u'Stockros'] = 'TBD'
    tr[u'Vävarkarda'] = 'TBD'
    tr[u'Fleråriga blommor, perenner'] = 'TBD'
    tr[u'Akleja'] = 'TBD'
    tr[u'Berglin'] = 'TBD'
    tr[u'Blågull'] = 'TBD'
    tr[u'Humle'] = 'TBD'
    tr[u'Japansk Lykta'] = 'TBD'
    tr[u'Jätteverbena'] = 'TBD'
    tr[u'Karpaterklocka'] = 'TBD'
    tr[u'Kungsljus'] = 'TBD'
    tr[u'Lupin'] = 'TBD'
    tr[u'Moses brinnande buske'] = 'TBD'
    tr[u'Myskmalva'] = 'TBD'
    tr[u'Praktriddarsporre'] = 'TBD'
    tr[u'Prästkrage'] = 'TBD'
    tr[u'Rosenmalva'] = 'TBD'
    tr[u'Rosenvial'] = 'TBD'
    tr[u'Rödmalva'] = 'TBD'
    tr[u'Röd rudbeckia /Solhatt'] = 'TBD'
    tr[u'Studentnejlika'] = 'TBD'
    tr[u'Såpnejlika'] = 'TBD'
    tr[u'Vallmo, fleråriga'] = 'TBD'
    tr[u'Ängsväxter'] = 'TBD'

    if val in tr:
        return tr[val]
    else:
        return 'Unknown'


def heightTranslator(val):
    return val.rstrip('.').rstrip('cm').strip()


def descriptionTranslator(val):
    p= re.compile(u' En portion innehåller (ca\\. )?[0-9\\-]+ frön\\.')
    return p.sub(u'', val)


class RunabergsScraperPipeline(object):
    def process_item(self, item, spider):
        item.pop(u'Storlekssorterat', None)
        item.pop(u'Ekologiskt', None)
        item.pop(u'Nyhet', None)
        item.pop(u'Latinskt namn', None)

        replaceIfPresent(item, u'Höjd', 'height')
        replaceIfPresent(item, u'Utvecklingstid, dagar', 'daysToMaturity')
        replaceIfPresent(item, u'F1 Hybrid', 'f1Hybrid')
        replaceIfPresent(item, u'Artikelnummer', 'runabergsArtNo')
        replaceIfPresent(item, u'Årighet', u'lifeCycle', lifeCycleTranslator)
        replaceIfPresent(item, u'Botanisk familj', u'botanicalFamily')
        replaceIfPresent(item, u'plantType', u'plantType', plantTypeTranslator)
        replaceIfPresent(item, u'plantSubType', u'plantSubType', plantSubTypeTranslator)
        replaceIfPresent(item, u'description', u'description', descriptionTranslator)

        return item

class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('runabergs_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        d = dict(item)
        line = json.dumps(d, ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
