import dash
from dash import dcc, html, Input, Output
import plotly.express as px
from data_analysis import SalesAnalyzer

app = dash.Dash(__name__)
analyzer = SalesAnalyzer(file='sales.csv')

app.layout = html.Div([
    html.H1("Satış Analizi ve AI Tahmin Paneli", style={'textAlign': 'center', 'color': '#2c3e50'}),

    # Filtreler
    html.Div([
        dcc.DatePickerRange(
            id='date-range',
            start_date=analyzer.df['Tarih'].min().date(),
            end_date=analyzer.df['Tarih'].max().date(),
            display_format='YYYY-MM-DD'
        ),
        dcc.Dropdown(id='category-filter', options=[{'label': 'Tüm Kategoriler', 'value': 'all'}] + [{'label': k, 'value': k} for k in sorted(analyzer.df['Kategori'].unique())], value='all', style={'width': '48%', 'display': 'inline-block'}),
        dcc.Dropdown(id='city-filter', options=[{'label': 'Tüm Şehirler', 'value': 'all'}] + [{'label': s, 'value': s} for s in sorted(analyzer.df['Şehir'].unique())], value='all', style={'width': '48%', 'display': 'inline-block'}),
    ], style={'padding': '20px', 'backgroundColor': '#f8f9fa'}),

    # 5 Tane İstatistik Kartı
    html.Div([
        html.Div([html.H4("Toplam Ciro"), html.H2(id='total')], style={'width': '19%', 'display': 'inline-block', 'textAlign': 'center'}),
        html.Div([html.H4("İşlem"), html.H2(id='count')], style={'width': '19%', 'display': 'inline-block', 'textAlign': 'center'}),
        html.Div([html.H4("Ortalama"), html.H2(id='avg')], style={'width': '19%', 'display': 'inline-block', 'textAlign': 'center'}),
        html.Div([html.H4("En Popüler"), html.H2(id='top-cat')], style={'width': '19%', 'display': 'inline-block', 'textAlign': 'center'}),
        # YENİ: AI Tahmin Kartı
        html.Div([
            html.H4("Gelecek Ay Tahmini (AI)", style={'color': '#27ae60'}),
            html.H2(id='ai-prediction', style={'color': '#27ae60'})
        ], style={'width': '19%', 'display': 'inline-block', 'textAlign': 'center', 'border': '2px solid #27ae60', 'borderRadius': '10px', 'backgroundColor': '#f1fcf4'}),
    ], style={'margin': '20px', 'padding': '10px'}),

    html.Div([
        dcc.Graph(id='trend', style={'width': '48%', 'display': 'inline-block'}),
        dcc.Graph(id='pie', style={'width': '48%', 'display': 'inline-block'})
    ]),
    html.Div([
        dcc.Graph(id='gender-bar', style={'width': '48%', 'display': 'inline-block'}),
        dcc.Graph(id='city-bar', style={'width': '48%', 'display': 'inline-block'})
    ])
])

@app.callback(
    [Output('total', 'children'), Output('count', 'children'), Output('avg', 'children'), 
     Output('top-cat', 'children'), Output('ai-prediction', 'children'),
     Output('trend', 'figure'), Output('pie', 'figure'), Output('gender-bar', 'figure'), Output('city-bar', 'figure')],
    [Input('date-range', 'start_date'), Input('date-range', 'end_date'), Input('category-filter', 'value'), Input('city-filter', 'value')]
)
def update_dashboard(start, end, cat, city):
    cats = [] if cat == 'all' else [cat]
    cities = [] if city == 'all' else [city]
    
    total, count, avg = analyzer.get_summary_stats(start, end, cats, cities)
    cat_data = analyzer.get_category_data(start, end, cities)
    top_cat = cat_data.iloc[cat_data['Net Tutar'].idxmax()]['Kategori'] if not cat_data.empty else "-"
    
    # AI Tahminini Çağır
    prediction = analyzer.predict_next_month()
    
    fig_trend = px.line(analyzer.get_daily_sales(start, end, cats, cities), x='Tarih', y='Net Tutar', title="Satış Trendi")
    fig_pie = px.pie(cat_data, values='Net Tutar', names='Kategori', title="Kategori Cirosu")
    fig_gender = px.bar(analyzer.get_gender_sales(start, end, cats, cities), x='gender', y='Net Tutar', title="Cinsiyet Analizi", color='gender')
    fig_bar = px.bar(analyzer.get_city_sales(start, end, cats), x='Şehir', y='Net Tutar', title="Şehir Satışları")
    
    return f"${total:,.2f}", f"{count}", f"${avg:,.2f}", top_cat, f"${prediction:,.2f}", fig_trend, fig_pie, fig_gender, fig_bar

if __name__ == '__main__':
    app.run(debug=True, port=8050)