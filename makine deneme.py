import json
import os
import difflib

HAFIZA_DOSYA = "hafiza.json"  

def load_hafiza(dosya=HAFIZA_DOSYA):
    try:
        if os.path.exists(dosya):
            with open(dosya, "r", encoding="utf-8") as file:
                return json.load(file)
        # Dosya yoksa, boş JSON başlat
        return {"isim": None, "sevdiği şeyler": {}, "konuşmalar": {}}
    except json.JSONDecodeError:
        print("JSON bozuk, yeni dosya oluşturuluyor!")
        return {"isim": None, "sevdiği şeyler": {}, "konuşmalar": {}}

def save_hafiza(hafiza, dosya=HAFIZA_DOSYA):
    with open(dosya, "w", encoding="utf-8") as file:
        json.dump(hafiza, file, indent=4, ensure_ascii=False)

def en_yakin_cevap(soru, hafiza):
    benzer = difflib.get_close_matches(soru, hafiza["konuşmalar"].keys(), n=1, cutoff=0.7)
    return hafiza["konuşmalar"][benzer[0]] if benzer else None

def sohbet(soru):
    global hafiza
    hafiza = load_hafiza()
    isim = hafiza["isim"] or "Bilmediğim kişi"

    # İsim öğrenme
    if "benim adım" in soru:
        isim = soru.replace("benim adım", "").strip().capitalize()
        hafiza["isim"] = isim
        save_hafiza(hafiza)
        return f"Memnun oldum {isim}!"

    # Benzer cevap bul
    yanit = en_yakin_cevap(soru, hafiza)
    if yanit:
        return yanit

    # Bilmiyorsa öğren
    cevap = input(f"{isim}, bunu bilmiyorum. Ne diyeyim? ")
    hafiza["konuşmalar"][soru] = cevap
    save_hafiza(hafiza)
    return "Tamam, öğrendim!"

# Test
if __name__ == "__main__":
    while True:
        mesaj = input("efendim: ").strip().lower()
        if mesaj == "q":
            print("Görüşmek üzere!")
            break
        print(f"soly: {sohbet(mesaj)}")
