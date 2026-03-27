import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CineScope",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&family=DM+Serif+Display:ital@0;1&display=swap');

:root {
    --blue:       #2563EB;
    --blue-light: #EFF6FF;
    --blue-mid:   #BFDBFE;
    --blue-dark:  #1E40AF;
    --white:      #FFFFFF;
    --gray-50:    #F8FAFC;
    --gray-100:   #F1F5F9;
    --gray-300:   #CBD5E1;
    --gray-500:   #64748B;
    --gray-800:   #1E293B;
    --text:       #0F172A;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--gray-50) !important;
}
[data-testid="stAppViewContainer"] {
    background-image: radial-gradient(ellipse 100% 40% at 50% 0%, #DBEAFE 0%, transparent 65%);
}
[data-testid="stToolbar"], header[data-testid="stHeader"] { display:none !important; }
.block-container { padding: 0 3rem 4rem !important; max-width: 1300px; }

/* ── Hero ── */
.hero {
    text-align: center;
    padding: 3rem 0 2.5rem;
}
.hero-badge {
    display: inline-block;
    background: var(--blue-light);
    color: var(--blue);
    font-family: 'DM Sans', sans-serif;
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    padding: 0.3rem 0.9rem;
    border-radius: 100px;
    border: 1px solid var(--blue-mid);
    margin-bottom: 1rem;
}
.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(2.8rem, 6vw, 5rem);
    color: var(--text);
    line-height: 1.05;
    margin: 0 0 0.5rem;
}
.hero-title span { color: var(--blue); }
.hero-sub {
    font-family: 'DM Sans', sans-serif;
    font-size: 1rem;
    color: var(--gray-500);
    font-weight: 300;
}

/* ── Search card ── */
.search-card {
    background: var(--white);
    border: 1px solid var(--gray-300);
    border-radius: 16px;
    padding: 2rem 2.5rem 1.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04), 0 8px 24px rgba(37,99,235,0.06);
    margin-bottom: 2rem;
}
.field-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--gray-500);
    margin-bottom: 0.35rem;
}

/* Input fields */
div[data-baseweb="input"] input {
    background: var(--gray-50) !important;
    border: 1.5px solid var(--gray-300) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 0.6rem 0.9rem !important;
    box-shadow: none !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}
div[data-baseweb="input"] input:focus {
    border-color: var(--blue) !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.1) !important;
    background: var(--white) !important;
}
div[data-baseweb="input"] input::placeholder { color: var(--gray-300) !important; }

/* Multiselect & selectbox */
div[data-baseweb="select"] > div {
    background: var(--gray-50) !important;
    border: 1.5px solid var(--gray-300) !important;
    border-radius: 8px !important;
    box-shadow: none !important;
    font-family: 'DM Sans', sans-serif !important;
    color: var(--text) !important;
}
[data-baseweb="tag"] {
    background: var(--blue-light) !important;
    border: 1px solid var(--blue-mid) !important;
    border-radius: 6px !important;
}
[data-baseweb="tag"] span { color: var(--blue-dark) !important; font-family:'DM Sans',sans-serif; font-size:0.82rem; }
[data-baseweb="menu"] {
    background: var(--white) !important;
    border: 1px solid var(--gray-300) !important;
    border-radius: 10px !important;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08) !important;
}
[data-baseweb="menu"] li { color: var(--text) !important; font-family:'DM Sans',sans-serif !important; font-size:0.9rem !important; }
[data-baseweb="menu"] li:hover { background: var(--blue-light) !important; color: var(--blue) !important; }

label, .stTextInput label, .stSelectbox label, .stMultiSelect label { display:none !important; }

/* ── Button ── */
.stButton button {
    width: 100% !important;
    background: var(--blue) !important;
    border: none !important;
    color: white !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.04em !important;
    padding: 0.75rem 2rem !important;
    border-radius: 10px !important;
    margin-top: 0.5rem !important;
    box-shadow: 0 2px 8px rgba(37,99,235,0.25) !important;
    transition: background 0.2s, box-shadow 0.2s, transform 0.1s !important;
}
.stButton button:hover {
    background: var(--blue-dark) !important;
    box-shadow: 0 4px 16px rgba(37,99,235,0.35) !important;
    transform: translateY(-1px) !important;
}
.stButton button:active { transform: translateY(0) !important; }

/* ── Stat cards ── */
.stat-row { display:flex; gap:1rem; margin-bottom:1.5rem; flex-wrap:wrap; }
.stat-card {
    flex:1; min-width:130px;
    background: var(--white);
    border: 1px solid var(--gray-300);
    border-radius: 12px;
    padding: 1.1rem 1.4rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
.stat-value {
    font-family: 'DM Serif Display', serif;
    font-size: 2rem;
    color: var(--blue);
    line-height: 1;
}
.stat-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--gray-500);
    margin-top: 0.3rem;
}

/* ── Results header ── */
.results-header {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.9rem;
    color: var(--gray-500);
    margin-bottom: 0.75rem;
}
.results-header strong { color: var(--text); }

/* ── Dataframe ── */
[data-testid="stDataFrame"] {
    border: 1px solid var(--gray-300) !important;
    border-radius: 12px !important;
    overflow: hidden !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
}
[data-testid="stDataFrame"] table { background: var(--white) !important; font-family:'DM Sans',sans-serif !important; }
[data-testid="stDataFrame"] th {
    background: var(--gray-50) !important;
    color: var(--gray-500) !important;
    font-size: 0.72rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    border-bottom: 1px solid var(--gray-300) !important;
    padding: 0.85rem 1rem !important;
}
[data-testid="stDataFrame"] td {
    color: var(--text) !important;
    border-bottom: 1px solid var(--gray-100) !important;
    padding: 0.7rem 1rem !important;
    font-size: 0.9rem !important;
}
[data-testid="stDataFrame"] tr:hover td { background: var(--blue-light) !important; }

/* ── No results ── */
.no-results {
    text-align:center; padding:4rem 2rem;
    background: var(--white);
    border: 1px solid var(--gray-300);
    border-radius: 16px;
    color: var(--gray-500);
    font-family:'DM Sans',sans-serif;
    font-size:1rem;
}
.no-results .icon { font-size:2.5rem; margin-bottom:0.75rem; }
</style>
""", unsafe_allow_html=True)

# ── Load data ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    return pd.read_csv('IMDB-Movie-Data.csv')

df = load_data()

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero">
    <div class="hero-badge">🎬 IMDB · {len(df)} Film</div>
    <h1 class="hero-title">Cine<span>Scope</span></h1>
    <p class="hero-sub">Sevdiyiniz filmi tapın — rejissor, janr, aktyor və ya il üzrə</p>
</div>
""", unsafe_allow_html=True)

# ── Search card ───────────────────────────────────────────────────────────────
st.markdown('<div class="search-card">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="field-label">Film Adı</div>', unsafe_allow_html=True)
    title = st.text_input("Title", placeholder="məs. Inception", label_visibility="collapsed")
with col2:
    st.markdown('<div class="field-label">Rejissor</div>', unsafe_allow_html=True)
    director = st.text_input("Director", placeholder="məs. Christopher Nolan", label_visibility="collapsed")
with col3:
    st.markdown('<div class="field-label">Aktyor</div>', unsafe_allow_html=True)
    actor = st.text_input("Actor", placeholder="məs. Leonardo DiCaprio", label_visibility="collapsed")

col4, col5, col6 = st.columns([2, 1, 1])
with col4:
    st.markdown('<div class="field-label">Janr</div>', unsafe_allow_html=True)
    genre = st.multiselect("Genre",
        options=df['Genre'].str.split(',').explode().str.strip().unique(),
        label_visibility="collapsed")
with col5:
    st.markdown('<div class="field-label">İl</div>', unsafe_allow_html=True)
    year = st.selectbox("Year",
        options=[None] + list(df['Year'].sort_values().unique()),
        label_visibility="collapsed")
with col6:
    st.markdown('<div class="field-label">&nbsp;</div>', unsafe_allow_html=True)
    search_clicked = st.button("🔍  Axtar")

st.markdown('</div>', unsafe_allow_html=True)

# ── Search ────────────────────────────────────────────────────────────────────
if search_clicked:
    filtered_df = df.copy()

    if title:
        filtered_df = filtered_df[filtered_df['Title'].str.contains(title, case=False, na=False)]
    if genre:
        for g in genre:
            filtered_df = filtered_df[filtered_df['Genre'].str.contains(g.strip(), case=False, na=False)]
    if director:
        filtered_df = filtered_df[filtered_df['Director'].str.contains(director, case=False, na=False)]
    if actor:
        actor_cols = [c for c in filtered_df.columns if 'Actor' in c or 'actor' in c]
        mask = pd.Series([False] * len(filtered_df), index=filtered_df.index)
        for col in actor_cols:
            mask |= filtered_df[col].astype(str).str.contains(actor, case=False, na=False)
        filtered_df = filtered_df[mask]
    if year:
        filtered_df = filtered_df[filtered_df['Year'] == year]

    n = len(filtered_df)

    if n > 0:
        avg_rating = f"{filtered_df['Rating'].mean():.1f}" if 'Rating' in filtered_df.columns else "—"
        avg_rev    = f"${filtered_df['Revenue (Millions)'].mean():.0f}M" if 'Revenue (Millions)' in filtered_df.columns else "—"

        st.markdown(f"""
        <div class="stat-row">
            <div class="stat-card"><div class="stat-value">{n}</div><div class="stat-label">Film tapıldı</div></div>
            <div class="stat-card"><div class="stat-value">{avg_rating}</div><div class="stat-label">Orta reytinq</div></div>
            <div class="stat-card"><div class="stat-value">{avg_rev}</div><div class="stat-label">Orta gəlir</div></div>
        </div>
        <div class="results-header">Göstərilir: <strong>{n} nəticə</strong></div>
        """, unsafe_allow_html=True)
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    else:
        st.markdown("""
        <div class="no-results">
            <div class="icon">🔍</div>
            <strong>Heç bir film tapılmadı</strong><br>
            <span style="font-size:0.85rem;opacity:0.7">Axtarış parametrlərini dəyişdirməyə çalışın</span>
        </div>
        """, unsafe_allow_html=True) 