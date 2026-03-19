🛒 Supermarket Sales Analysis & AI Prediction Dashboard
Bu proje, bir süpermarketin satış verilerini analiz etmek, interaktif bir dashboard üzerinden görselleştirmek ve Makine Öğrenmesi kullanarak gelecek dönem satışlarını tahmin etmek amacıyla geliştirilmiştir.

🚀 Öne Çıkan Özellikler
Dinamik Veri Analizi: Satış verileri; kategori, şehir ve tarih bazlı olarak anlık filtrelenebilir.

İnteraktif Görselleştirme: Plotly ve Dash kütüphaneleri kullanılarak oluşturulmuş grafikler (Trend Analizi, Pasta Grafikleri, Bar Grafikleri).

Yapay Zeka Destekli Tahmin: scikit-learn kütüphanesi ve Linear Regression algoritması kullanılarak gelecek 30 günlük satış tahmini.

Demografik İçgörüler: Müşteri cinsiyetine göre harcama alışkanlıklarının analizi.

Veri Ön İşleme (Preprocessing): Ham verilerin temizlenmesi, eksik tarihlerin sentetik olarak üretilmesi ve analize uygun hale getirilmesi.

🛠️ Kullanılan Teknolojiler
Dil: Python 3.x

Veri Analizi: Pandas, Numpy

Görselleştirme: Plotly, Dash

Makine Öğrenmesi: Scikit-Learn (Linear Regression)

Arayüz: Dash HTML & Core Components

📂 Proje Yapısı
main.py: Uygulamanın giriş noktası.

dashboard.py: Arayüz tasarımı ve callback fonksiyonları.

data_analysis.py: Veri işleme, istatistiksel hesaplamalar ve ML modelinin bulunduğu çekirdek dosya.

sales.csv: Analiz edilen ham veri seti.

🔧 Kurulum ve Çalıştırma
Depoyu klonlayın

Gerekli kütüphaneleri yükleyin

Uygulamayı çalıştırın

Tarayıcınızda http://127.0.0.1:8050/ adresine gidin.

📈 Makine Öğrenmesi Notu
Projeye dahil edilen Lineer Regresyon modeli, geçmiş satış trendlerini baz alarak doğrusal bir tahminleme yapar. Veri seti büyüdükçe modelin doğruluğu (Accuracy) artırılabilecek şekilde modüler bir yapıda tasarlanmıştır.
