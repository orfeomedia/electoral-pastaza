import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import gzip
import shutil
import os

# Configuración
st.set_page_config(
    page_title="Electoral Pastaza",
    page_icon="🗳️",
    layout="wide"
)

# CSS
st.markdown("""
<style>
    .winner-card {
        background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
        padding: 2rem;
        border-radius: 10px;
        border: 3px solid #ffa500;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Función para descomprimir archivos .gz automáticamente
def descomprimir_si_necesario(archivo):
    """Descomprime archivo .gz si existe, sino usa el original"""
    archivo_gz = f"{archivo}.gz"
    
    # Si existe el .gz y no existe el descomprimido
    if os.path.exists(archivo_gz) and not os.path.exists(archivo):
        with gzip.open(archivo_gz, 'rb') as f_in:
            with open(archivo, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    
    return archivo

# Cargar datos
@st.cache_data
def cargar_seccionales():
    archivo = descomprimir_si_necesario('Resultados-electorales-2023.csv')
    df = pd.read_csv(archivo, sep=';', header=None, encoding='utf-8', low_memory=False, on_bad_lines='skip')
    df.columns = ['a','b','cod_prov','d','cod_cant','f','g','h','i','j','sexo','num_lista','org','siglas','num_cand','candidato','v1','v2','v3','votos']
    return df[df['cod_prov'] == 16].copy()

@st.cache_data
def cargar_asambleistas():
    archivo23 = descomprimir_si_necesario('Primera-vuelta_2023.csv')
    archivo25 = descomprimir_si_necesario('Primera-vuelta_2025.csv')
    
    df23 = pd.read_csv(archivo23, sep=';', header=None, encoding='utf-8', low_memory=False)
    df25 = pd.read_csv(archivo25, sep=';', header=None, encoding='utf-8', low_memory=False)
    
    excluir = ['FERNANDO VILLAVICENCIO','LUISA GONZALEZ','DANIEL NOBOA AZIN','YAKU PEREZ','OTTO SONNENHOLZNER',
               'JAN TOPIC','BOLIVAR ARMIJOS','XAVIER HERVAS','LEONIDAS IZA','HENRY CUCALON','ANDREA GONZALEZ',
               'PEDRO GRANJA','SI','NO']
    
    asam23 = df23[df23[2] == 16]
    asam25 = df25[df25[2] == 16]
    
    asam23 = asam23[~asam23[12].isin(excluir)]
    asam25 = asam25[~asam25[12].isin(excluir)]
    
    return asam23, asam25

with st.spinner('🔄 Cargando datos electorales...'):
    seccionales = cargar_seccionales()
    asam23, asam25 = cargar_asambleistas()

# Header
st.title("🗳️ Electoral Pastaza 2023-2025")
st.markdown("### Análisis Completo - Datos Oficiales CNE")

# Tabs principales
tab1, tab2, tab3 = st.tabs(["🏛️ Seccionales 2023", "📊 Asambleístas", "📈 Comparación"])

with tab1:
    st.header("Prefecto de Pastaza 2023")
    
    # Leer candidatos para obtener listas correctas
    try:
        archivo_cand = descomprimir_si_necesario('Candidatos-2023.csv')
        cand = pd.read_csv(archivo_cand, sep=';', header=None, encoding='utf-8')
        cand_pastaza = cand[cand[3] == 'PASTAZA']
        listas_pref = cand_pastaza[cand_pastaza[1] == 'PREFECTO Y VICEPREFECTO'][10].unique()
        prefecto = seccionales[seccionales['num_lista'].isin(listas_pref)]
    except:
        st.warning("Usando rango de listas alternativo")
        prefecto = seccionales[seccionales['num_lista'].between(1, 2000)]
    
    if len(prefecto) > 0:
        res = prefecto.groupby(['candidato','org'])['votos'].sum().reset_index()
        res = res.sort_values('votos', ascending=False)
        total = res['votos'].sum()
        res['pct'] = (res['votos']/total*100).round(2)
        
        # Ganador
        if len(res) > 0:
            g = res.iloc[0]
            st.markdown(f"""
            <div class="winner-card">
                <h2>🏆 GANADOR</h2>
                <h3>{g['candidato']}</h3>
                <p><strong>{g['org']}</strong></p>
                <h1 style="color:#ff6600;">{int(g['votos']):,} votos</h1>
                <p style="font-size:1.3em;">{g['pct']:.2f}%</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.subheader("Resultados Completos")
        
        for idx, row in res.iterrows():
            col1, col2, col3 = st.columns([3,2,2])
            with col1:
                st.markdown(f"**{row['candidato']}**")
                st.caption(str(row['org'])[:50])
            with col2:
                st.metric("Votos", f"{int(row['votos']):,}")
            with col3:
                st.metric("%", f"{row['pct']:.2f}%")
            st.progress(row['pct']/100)
        
        # Gráfico
        fig = px.bar(res.head(8), x='candidato', y='votos', title='Top Candidatos', color='votos')
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Asambleístas Provinciales")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("2023")
        if len(asam23) > 0:
            res23 = asam23.groupby(12)[16].sum().sort_values(ascending=False).head(10)
            for i, (p, v) in enumerate(res23.items(), 1):
                st.write(f"{i}. **{str(p)[:40]}** - {int(v):,} votos")
            
            fig = px.bar(x=res23.values, y=[str(x)[:30] for x in res23.index], orientation='h', title='Top 10 - 2023')
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("2025")
        if len(asam25) > 0:
            res25 = asam25.groupby(12)[16].sum().sort_values(ascending=False).head(10)
            for i, (p, v) in enumerate(res25.items(), 1):
                st.write(f"{i}. **{str(p)[:40]}** - {int(v):,} votos")
            
            fig = px.bar(x=res25.values, y=[str(x)[:30] for x in res25.index], orientation='h', title='Top 10 - 2025')
            st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("Comparación 2023 vs 2025")
    
    if len(asam23) > 0 and len(asam25) > 0:
        r23 = asam23.groupby(12)[16].sum()
        r25 = asam25.groupby(12)[16].sum()
        
        comp = pd.DataFrame({'2023': r23, '2025': r25}).fillna(0)
        comp['Var'] = comp['2025'] - comp['2023']
        comp['Var%'] = ((comp['2025']-comp['2023'])/comp['2023']*100).fillna(0)
        comp = comp.sort_values('2025', ascending=False).head(15)
        
        st.dataframe(
            comp.style.format({'2023':'{:,.0f}','2025':'{:,.0f}','Var':'{:+,.0f}','Var%':'{:+.1f}%'})
                .background_gradient(subset=['Var%'], cmap='RdYlGn', vmin=-100, vmax=100),
            use_container_width=True
        )
        
        # Gráfico
        top8 = comp.head(8).index
        fig = go.Figure()
        fig.add_trace(go.Bar(name='2023', x=[str(p)[:25] for p in top8], y=[comp.loc[p,'2023'] for p in top8]))
        fig.add_trace(go.Bar(name='2025', x=[str(p)[:25] for p in top8], y=[comp.loc[p,'2025'] for p in top8]))
        fig.update_layout(title='Comparación Top 8 Partidos', barmode='group', height=500)
        st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#666;'>
    <p><strong>Electoral Pastaza 2023-2025</strong></p>
    <p>Datos: CNE Ecuador | Provincia: Pastaza</p>
</div>
""", unsafe_allow_html=True)
