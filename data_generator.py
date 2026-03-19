import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_sales_data(num_records=1000):
    """Generate sample sales data"""
    
    # Product categories
    categories = ['Elektronik', 'Giyim', 'Gıda', 'Ev Dekorasyon', 'Spor', 'Kitap']
    products = {
        'Elektronik': ['Laptop', 'Telefon', 'Tablet', 'Kulaklık', 'Akıllı Saat'],
        'Giyim': ['Tişört', 'Pantolon', 'Ceket', 'Ayakkabı', 'Çanta'],
        'Gıda': ['Kahve', 'Çay', 'Atıştırmalık', 'Meyve', 'Sebze'],
        'Ev Dekorasyon': ['Lamba', 'Tablo', 'Halı', 'Yastık', 'Vazo'],
        'Spor': ['Spor Ayakkabı', 'Dambıl', 'Yoga Matı', 'Su Şişesi', 'Spor Çantası'],
        'Kitap': ['Roman', 'Bilim Kitabı', 'Tarih Kitabı', 'Kişisel Gelişim', 'Çocuk Kitabı']
    }
    
    # Cities in Turkey
    cities = ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya', 'Adana', 'Konya', 'Gaziantep']
    
    # Generate dates
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    
    data = []
    for _ in range(num_records):
        category = random.choice(categories)
        product = random.choice(products[category])
        city = random.choice(cities)
        
        # Random date between start and end
        random_days = random.randint(0, (end_date - start_date).days)
        date = start_date + timedelta(days=random_days)
        
        # Random quantity and price
        quantity = random.randint(1, 10)
        base_price = random.uniform(50, 5000)
        price = round(base_price * quantity, 2)
        
        # Random discount
        discount = random.choice([0, 5, 10, 15, 20, 25])
        
        data.append({
            'Tarih': date.strftime('%Y-%m-%d'),
            'Kategori': category,
            'Ürün': product,
            'Şehir': city,
            'Miktar': quantity,
            'Birim Fiyat': round(base_price, 2),
            'Toplam Tutar': price,
            'İndirim (%)': discount,
            'Net Tutar': round(price * (1 - discount/100), 2)
        })
    
    df = pd.DataFrame(data)
    df['Tarih'] = pd.to_datetime(df['Tarih'])
    
    return df

if __name__ == "__main__":
    # Generate and save sample data
    sales_data = generate_sales_data(5000)
    sales_data.to_excel('satis_verileri.xlsx', index=False)
    sales_data.to_csv('satis_verileri.csv', index=False)
    
    print(f"Örnek satış verisi oluşturuldu: {len(sales_data)} kayıt")
    print("Dosyalar kaydedildi: satis_verileri.xlsx, satis_verileri.csv")
    
    # Display first few rows
    print("\nİlk 5 kayıt:")
    print(sales_data.head())
