# 📊 Satış Veri Analiz Platformu

Python pandas ve Plotly kullanarak geliştirilmiş interaktif satış veri analiz platformu.

## 🚀 Özellikler

- **📈 Görsel Analiz**: Plotly ile interaktif grafikler ve dashboard
- **🔍 Detaylı Filtreleme**: Tarih, kategori ve şehir bazında filtreleme
- **📊 Zaman Serisi Analizi**: Günlük, aylık ve yıllık satış trendleri
- **🎯 Performans Metrikleri**: Kategori, ürün ve şehir bazında performans analizi
- **💰 İndirim Analizi**: İndirim oranlarının satışlara etkisi
- **📋 Veri Tablosu**: Detaylı veri görüntüleme ve filtreleme

## 📋 Kurulum

### 1. Gerekli Kütüphaneler

```bash
pip install -r requirements.txt
```

veya manuel olarak:

```bash
pip install pandas plotly dash dash-bootstrap-components openpyxl
```

### 2. Veri Oluşturma

Örnek satış verisi oluşturmak için:

```bash
python data_generator.py
```

Bu komut:
- `satis_verileri.csv` dosyasını oluşturur
- `satis_verileri.xlsx` dosyasını oluşturur
- 5000 adet örnek satış kaydı üretir

### 3. Platformu Başlatma

```bash
python main.py
```

veya doğrudan dashboard:

```bash
python dashboard.py
```

Platform başlatıldığında otomatik olarak tarayıcıda `http://127.0.0.1:8050` adresi açılacaktır.

## 📁 Proje Yapısı

```
veri_bilimi/
├── main.py                 # Ana başlatma dosyası
├── dashboard.py            # Dash uygulaması
├── data_analysis.py        # Pandas analiz modülü
├── data_generator.py       # Örnek veri üretici
├── requirements.txt        # Gerekli kütüphaneler
├── satis_verileri.csv      # Satış verisi
├── satis_verileri.xlsx     # Excel formatında veri
└── README.md              # Proje dokümantasyonu
```

## 📊 Analiz Özellikleri

### 📈 Dashboard Bileşenleri

1. **Özet Kartları**
   - Toplam Satış
   - Toplam İşlem Sayısı
   - Ortalama Sepet Tutarı
   - Toplam Kar

2. **Filtreler**
   - Tarih aralığı seçimi
   - Kategori filtresi (çoklu seçim)
   - Şehir filtresi (çoklu seçim)

3. **Grafikler**
   - Aylık satış trendi
   - Kategori performans analizi
   - Şehir bazında satış dağılımı
   - En çok satan ürünler
   - İndirim etkisi analizi
   - Zaman serisi ve hareketli ortalamalar

4. **Veri Tablosu**
   - Filtrelenmiş verilerin detaylı görüntülenmesi

### 🎯 Analiz Metrikleri

- **Satış Performansı**: Toplam ve ortalama satış değerleri
- **Kategori Analizi**: Kategori bazında satış ve kar dağılımı
- **Coğrafi Analiz**: Şehir bazında satış performansı
- **Ürün Analizi**: En çok satan ürünler ve performansları
- **İndirim Analizi**: İndirim oranlarının satışlara etkisi
- **Trend Analizi**: Zaman içindeki satış değişimleri

## 🔧 Veri Formatı

Platform şu veri alanlarını destekler:

- `Tarih`: Satış tarihi
- `Kategori`: Ürün kategorisi
- `Ürün`: Ürün adı
- `Şehir`: Satış şehri
- `Miktar`: Satış adedi
- `Birim Fiyat`: Birim fiyat
- `Toplam Tutar`: Toplam tutar
- `İndirim (%)`: İndirim oranı
- `Net Tutar`: İndirim sonrası net tutar

## 🎨 Kullanılan Teknolojiler

- **Python 3.7+**: Ana programlama dili
- **Pandas**: Veri analizi ve manipülasyonu
- **Plotly**: İnteraktif görselleştirme
- **Dash**: Web uygulama framework'ü
- **Dash Bootstrap Components**: UI bileşenleri
- **OpenPyXL**: Excel dosya okuma/yazma

## 📝 Notlar

- Platform 5000 satırlık veriyle optimize edilmiştir
- Daha büyük veri setleri için performans iyileştirmesi yapılabilir
- Tarayıcıda Chrome veya Firefox kullanılması önerilir
- Dashboard otomatik olarak tarayıcıda açılır

## 🤝 Katkı

Projeye katkıda bulunmak için:
1. Fork yapın
2. Feature branch oluşturun
3. Değişikliklerinizi yapın
4. Pull request gönderin

## 📄 Lisans

Bu proje MIT lisansı altında dağıtılmaktadır.
