# Chatbot Project 🤖

This project is a Python-based chatbot that learns from user interactions and stores responses in a JSON file. It supports both English and Turkish conversations. You can train it yourself, or use the sample JSON file provided.

---

## 📌 English

### Features

- Stores and retrieves responses using a JSON file (`hafiza_en.json`).
- Learns new responses based on user input.
- Creates an empty JSON file if none exists.
- English language support (see Turkish version below).

### Setup

1. Place `hafiza_en.json` in the project directory, or allow the application to create one.
2. Run the script:

```bash
python chatbot.py
```

3. Interact with the chatbot to provide or retrieve responses.

### Example

```text
Ask away: hi
soly: Hey there!

Ask away: naber
Unknown person, I don’t know this. What should I say? What's good?
soly: Got it, learned!
```

### Contributing

Contributions are welcome. To contribute:
- Update `hafiza_en.json` with new responses.
- Or improve the codebase and submit a pull request.

---

## 📌 Türkçe

Bu proje, kullanıcı etkileşimlerinden öğrenen ve cevapları JSON dosyasında saklayan Python tabanlı bir sohbet botudur. İngilizce ve Türkçe dillerini destekler. Bu, İngilizce versiyonudur. Eğer cevap vermezse, size verdiğim JSON dosyasını uygulamanın oluşturduğu dosyaya yapıştırabilirsiniz, bu şekilde çalışır. Ama kendiniz eğitirseniz daha eğlenceli olabilir. :)

### Özellikler

- Cevapları JSON dosyasında (`hafiza_en.json` veya `hafiza_tr.json`) saklar ve alır.
- Kullanıcıdan yeni cevaplar öğrenir.
- Dosya yoksa otomatik olarak boş bir JSON dosyası oluşturur.
- İngilizce ve Türkçe dil desteği vardır.

### Kurulum (Türkçe Versiyon)

1. `hafiza_tr.json` dosyasını proje dizinine yerleştirin veya uygulamanın otomatik oluşturmasına izin verin.
2. Türkçe konuşma için ayrı bir `chatbot_tr.py` dosyası oluşturun.
3. Aşağıdaki değişiklikleri yapın:
   - `MEMORY_FILE = "hafiza_tr.json"` olarak güncelleyin.
   - `chat()` fonksiyonunda dil kontrollerini Türkçe’ye uyarlayın:
     - `"my name is"` yerine `"benim adım"` kontrolü yapın.
     - Yanıt mesajlarını Türkçeye çevirin:
       - `Ask away:` → `Efendim:`
       - `Unknown person` → `Bilmediğim kişi`
       - `Nice to meet you, {name}!` → `Memnun oldum, {name}!`
       - `Got it, learned!` → `Tamam, öğrendim!`

4. Betiği çalıştırın:

```bash
python chatbot_tr.py
```

5. Türkçe konuşarak botla etkileşime geçin.

### Örnek (Türkçe Konuşma)

```text
Efendim: naber
Bilmediğim kişi, bunu bilmiyorum. Ne diyeyim? Nasılsın?
soly: Tamam, öğrendim!

Efendim: benim adım Ali
soly: Memnun oldum, Ali!
```

---

## ✨ Katkıda Bulunma

Katkılarınızı bekliyoruz. Yeni cevaplar eklemek için:
- `hafiza_en.json` veya `hafiza_tr.json` dosyalarına giriş yapabilirsiniz.
- Ya da kodu geliştirerek pull request gönderebilirsiniz.

---

## 📝 Notlar

- Yeni bir başlangıç için `hafiza_en.json` veya `hafiza_tr.json` dosyasını silin. Uygulama otomatik olarak yeni bir dosya oluşturacaktır.
- Geliştirdiğiniz botu sosyal medyada paylaşarak tanıtabilirsiniz. Eğlence olsun diye etiket: `#solybot`




