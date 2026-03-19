#!/usr/bin/env python3
"""
Satış Veri Analiz Platformu
Ana başlatma dosyası
"""

import sys
import os
import webbrowser
import time
from threading import Timer

def open_browser():
    """Tarayıcıyı otomatik olarak aç"""
    time.sleep(2)  # Sunucunun başlaması için bekle
    webbrowser.open('http://127.0.0.1:8050')

def main():
    """Ana fonksiyon"""
    print("=" * 60)
    print("SATIS VERI ANALIZ PLATFORMU")
    print("=" * 60)
    
    # Gerekli dosyaların varlığını kontrol et
    required_files = ['sales.csv', 'data_analysis.py', 'dashboard.py']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"Eksik dosyalar: {', '.join(missing_files)}")
        print("Lutfen once data_generator.py calistirarak veri olusturun.")
        return
    
    print("Gerekli dosyalar bulundu.")
    print("Dashboard baslatiliyor...")
    print("Dashboard adresi: http://127.0.0.1:8050")
    print("Durdurmak icin CTRL+C tuslarina basin")
    print("-" * 60)
    
    try:
        # Tarayıcıyı otomatik aç
        Timer(3.0, open_browser).start()
        
        # Dashboard'u başlat
        from dashboard import app
        app.run(debug=False, host='0.0.0.0', port=8050)
        
    except KeyboardInterrupt:
        print("\nDashboard durduruldu.")
    except Exception as e:
        print(f"Hata olustu: {e}")

if __name__ == "__main__":
    main()
