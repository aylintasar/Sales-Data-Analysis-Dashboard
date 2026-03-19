import pandas as pd
import numpy as np

class SalesAnalyzer:
    def __init__(self, file='sales.csv'):
        self.df = pd.read_csv(file)
        
        # SÜTUN EŞLEME (Senin gönderdiğin yeni isimlere göre)
        mapping = {
            'city': 'Şehir',
            'product_category': 'Kategori',
            'total_price': 'Net Tutar'
        }
        self.df.rename(columns=mapping, inplace=True)
        
        # KRİTİK ADIM: Dosyada tarih yok, o yüzden uydurma tarihler ekliyoruz
        # 2024 başından itibaren bugüne kadar rastgele tarihler atayalım
        if 'Tarih' not in self.df.columns:
            print("Uyarı: Dosyada tarih bulunamadı, rastgele tarihler oluşturuluyor...")
            dates = pd.date_range(start='2024-01-01', periods=len(self.df), freq='h')
            self.df['Tarih'] = dates
            
        # Kar sütunu
        self.df['Kar'] = self.df['Net Tutar'] * 0.15
        
        print("Veri seti uyarlandı ve çalışmaya hazır!")


    def get_summary_stats(self, start_date, end_date, categories, cities):
        mask = (self.df['Tarih'] >= start_date) & (self.df['Tarih'] <= end_date)
        
        if categories:
            mask &= (self.df['Kategori'].isin(categories))
        if cities:
            mask &= (self.df['Şehir'].isin(cities))
            
        filtered_df = self.df[mask]
        
        total_sales = filtered_df['Net Tutar'].sum()
        total_orders = len(filtered_df)
        avg_order_value = total_sales / total_orders if total_orders > 0 else 0
        
        return round(total_sales, 2), total_orders, round(avg_order_value, 2)

    def get_category_data(self, start_date, end_date, cities):
        mask = (self.df['Tarih'] >= start_date) & (self.df['Tarih'] <= end_date)
        if cities:
            mask &= (self.df['Şehir'].isin(cities))
            
        return self.df[mask].groupby('Kategori')['Net Tutar'].sum().reset_index()

    def get_daily_sales(self, start_date, end_date, categories, cities):
        mask = (self.df['Tarih'] >= start_date) & (self.df['Tarih'] <= end_date)
        if categories:
            mask &= (self.df['Kategori'].isin(categories))
        if cities:
            mask &= (self.df['Şehir'].isin(cities))
            
        return self.df[mask].groupby('Tarih')['Net Tutar'].sum().reset_index()

    def get_city_sales(self, start_date, end_date, categories):
        mask = (self.df['Tarih'] >= start_date) & (self.df['Tarih'] <= end_date)
        if categories:
            mask &= (self.df['Kategori'].isin(categories))
            
        return self.df[mask].groupby('Şehir')['Net Tutar'].sum().reset_index()

    def get_gender_sales(self, start_date, end_date, categories, cities):
        mask = (self.df['Tarih'] >= start_date) & (self.df['Tarih'] <= end_date)
        if categories:
            mask &= (self.df['Kategori'].isin(categories))
        if cities:
            mask &= (self.df['Şehir'].isin(cities))
            
        return self.df[mask].groupby('gender')['Net Tutar'].sum().reset_index()

    def predict_next_month(self):
        from sklearn.linear_model import LinearRegression
        import numpy as np
        
        # Günlük satışları topla
        daily_sales = self.df.groupby('Tarih')['Net Tutar'].sum().reset_index()
        daily_sales['gun_indeksi'] = range(len(daily_sales))
        
        # Modeli eğit
        X = daily_sales[['gun_indeksi']]
        y = daily_sales['Net Tutar']
        
        model = LinearRegression()
        model.fit(X, y)
        
        # Gelecek 30 günü tahmin et
        son_gun = daily_sales['gun_indeksi'].max()
        gelecek_gunler = np.array(range(son_gun + 1, son_gun + 31)).reshape(-1, 1)
        tahminler = model.predict(gelecek_gunler)
        
        return round(max(0, tahminler.sum()), 2)