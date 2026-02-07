import streamlit as st
from utils.assistant import ai_real_estate_agent
from utils.predictor import predict_price
import pandas as pd

# Page config
st.set_page_config(
    page_title="AI Real Estate Assistant - Bangalore",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for DARK THEME
st.markdown("""
    <style>
    /* Main background */
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #1a1d29;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
        width: 100%;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* Info boxes - Dark theme */
    .info-box {
        background: linear-gradient(135deg, #1e2139 0%, #2a2d4a 100%);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        margin: 10px 0;
        color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    .success-box {
        background: linear-gradient(135deg, #1a2e1a 0%, #2d4a2d 100%);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #4CAF50;
        margin: 10px 0;
        color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    .warning-box {
        background: linear-gradient(135deg, #2e2a1a 0%, #4a3d2d 100%);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff9800;
        margin: 10px 0;
        color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    /* Headers */
    h1 {
        color: #667eea;
        text-align: center;
        padding: 20px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    
    h2, h3, h4 {
        color: #a8b2d1;
    }
    
    /* Text areas and inputs */
    .stTextArea textarea {
        background-color: #1a1d29;
        color: #ffffff;
        border: 1px solid #667eea;
        border-radius: 10px;
    }
    
    .stNumberInput input {
        background-color: #1a1d29;
        color: #ffffff;
        border: 1px solid #667eea;
    }
    
    .stSelectbox select {
        background-color: #1a1d29;
        color: #ffffff;
        border: 1px solid #667eea;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #667eea;
        font-size: 28px;
        font-weight: bold;
    }
    
    [data-testid="stMetricDelta"] {
        color: #4CAF50;
    }
    
    /* Radio buttons */
    .stRadio > label {
        color: #a8b2d1;
    }
    
    /* Slider */
    .stSlider > div > div > div {
        background-color: #667eea;
    }
    
    /* Divider */
    hr {
        border-color: #667eea;
        opacity: 0.3;
    }
    
    /* Cards effect */
    .card {
        background: linear-gradient(135deg, #1e2139 0%, #2a2d4a 100%);
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
        border: 1px solid #667eea33;
    }
    
    /* Glowing effect */
    .glow {
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from {
            box-shadow: 0 0 5px #667eea, 0 0 10px #667eea;
        }
        to {
            box-shadow: 0 0 10px #764ba2, 0 0 20px #764ba2;
        }
    }
    
    /* Footer */
    .footer {
        background: linear-gradient(135deg, #1a1d29 0%, #0e1117 100%);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; padding: 20px;'>
            <h1 style='color: #667eea; font-size: 48px;'>🏡</h1>
            <h2 style='color: #a8b2d1;'>Navigation</h2>
        </div>
    """, unsafe_allow_html=True)
    
    page = st.radio(
        "Choose a feature:",
        ["🤖 AI Chat Assistant", "💰 Price Predictor", "📊 Area Comparison", "🧮 EMI Calculator", "ℹ️ About"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### 📍 Popular Locations")
    locations = ['Whitefield', 'Electronic City', 'Hebbal', 'Marathahalli', 
                 'Indiranagar', 'Koramangala', 'BTM Layout', 'HSR Layout', 
                 'Jayanagar', 'Rajaji Nagar']
    
    for loc in locations[:5]:
        st.markdown(f"<p style='color: #a8b2d1;'>• {loc}</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 💡 Quick Tips")
    st.markdown("""
        <div class="info-box">
        <p style='font-size: 14px;'>Ask natural questions like:<br>
        • What's the price of 3BHK in Koramangala?<br>
        • Is Whitefield good for investment?<br>
        • Compare HSR Layout vs Jayanagar</p>
        </div>
    """, unsafe_allow_html=True)

# Main content
st.markdown("""
    <h1 style='font-size: 48px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
    background-clip: text;'>
    🏡 AI Real Estate Assistant
    </h1>
    <h3 style='text-align: center; color: #a8b2d1;'>Your Smart Property Advisor powered by Machine Learning</h3>
""", unsafe_allow_html=True)

# Page routing
if page == "🤖 AI Chat Assistant":
    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 💬 Chat with AI")
        
        # Example prompts
        st.markdown("**Try these examples:**")
        example_cols = st.columns(3)
        
        with example_cols[0]:
            if st.button("💰 Price of 2BHK in Whitefield"):
                st.session_state['prompt'] = "What is the price of 2BHK in Whitefield?"
        
        with example_cols[1]:
            if st.button("📈 Investment advice"):
                st.session_state['prompt'] = "Is it good to invest in Koramangala?"
        
        with example_cols[2]:
            if st.button("🏘️ Compare areas"):
                st.session_state['prompt'] = "Compare Indiranagar and HSR Layout"
        
        user_prompt = st.text_area(
            "💬 Your Question",
            value=st.session_state.get('prompt', ''),
            placeholder="Example: What is the price of a 3BHK 1500 sqft apartment in Jayanagar?",
            height=100
        )
        
        col_btn1, col_btn2 = st.columns([1, 4])
        with col_btn1:
            ask_button = st.button("🚀 Ask AI")
        with col_btn2:
            if st.button("🗑️ Clear"):
                st.session_state['prompt'] = ''
                st.rerun()
        
        if ask_button:
            if user_prompt.strip() == "":
                st.warning("⚠️ Please enter a question")
            else:
                with st.spinner("🤔 AI is thinking..."):
                    response = ai_real_estate_agent(user_prompt)
                    st.markdown("### 🤖 AI Response:")
                    st.markdown(f'<div class="success-box glow">{response}</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="card">
            <h3 style='color: #667eea;'>📊 Market Insights</h3>
            </div>
        """, unsafe_allow_html=True)
        
        st.metric("Average Price/sqft", "₹5,800", "+12%")
        st.metric("Properties Listed", "1,247", "+8%")
        st.metric("Avg. Growth Rate", "15% YoY", "+3%")
        
        st.markdown("""
            <div class="card">
            <h3 style='color: #667eea;'>🔥 Trending Areas</h3>
            <p style='color: #a8b2d1;'>
            1. 🏆 Whitefield<br>
            2. 🌟 Koramangala<br>
            3. 💎 Indiranagar
            </p>
            </div>
        """, unsafe_allow_html=True)

elif page == "💰 Price Predictor":
    st.markdown("---")
    st.markdown("### 🎯 Predict Property Prices")
    
    col1, col2 = st.columns(2)
    
    with col1:
        location = st.selectbox(
            "📍 Select Location",
            ['Whitefield', 'Electronic City', 'Hebbal', 'Marathahalli', 
             'Indiranagar', 'Koramangala', 'BTM Layout', 'HSR Layout', 
             'Jayanagar', 'Rajaji Nagar']
        )
        
        bhk = st.slider("🛏️ Number of Bedrooms (BHK)", 1, 5, 2)
    
    with col2:
        sqft = st.number_input("📐 Total Area (sqft)", 500, 5000, 1200, step=100)
        
        bath = st.slider("🚿 Number of Bathrooms", 1, 5, 2)
    
    if st.button("💰 Calculate Price"):
        with st.spinner("Calculating..."):
            price = predict_price(location, sqft, bhk, bath)
            
            st.markdown("---")
            st.markdown("### 🎉 Estimated Property Price")
            
            col_res1, col_res2, col_res3 = st.columns(3)
            
            with col_res1:
                st.metric("💵 Total Price", f"₹{price:.2f} Lakhs")
            
            with col_res2:
                price_per_sqft = (price * 100000) / sqft
                st.metric("📊 Price/sqft", f"₹{price_per_sqft:.0f}")
            
            with col_res3:
                emi = (price * 100000 * 0.008) / 100
                st.metric("💳 Est. EMI", f"₹{emi:.0f}/month")
            
            st.markdown(f"""
            <div class="info-box glow">
            <h4 style='color: #667eea;'>📋 Property Details</h4>
            <p style='color: #a8b2d1;'>
            • Location: <b style='color: #ffffff;'>{location}</b><br>
            • Configuration: <b style='color: #ffffff;'>{bhk} BHK</b><br>
            • Area: <b style='color: #ffffff;'>{sqft} sqft</b><br>
            • Bathrooms: <b style='color: #ffffff;'>{bath}</b><br>
            <br>
            💡 <i>This is an AI-estimated price based on market trends</i>
            </p>
            </div>
            """, unsafe_allow_html=True)

elif page == "📊 Area Comparison":
    st.markdown("---")
    st.markdown("### 📊 Compare Different Areas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        area1 = st.selectbox("First Area", 
                            ['Whitefield', 'Koramangala', 'Indiranagar', 'HSR Layout'])
    
    with col2:
        area2 = st.selectbox("Second Area", 
                            ['Jayanagar', 'BTM Layout', 'Marathahalli', 'Electronic City'])
    
    if st.button("🔍 Compare"):
        price1 = predict_price(area1, 1200, 2, 2)
        price2 = predict_price(area2, 1200, 2, 2)
        
        col_c1, col_c2 = st.columns(2)
        
        with col_c1:
            st.markdown(f"""
            <div class="card glow">
            <h3 style='color: #667eea;'>📍 {area1}</h3>
            <h2 style='color: #ffffff;'>₹{price1:.2f} Lakhs</h2>
            <p style='color: #a8b2d1;'>For 2 BHK, 1200 sqft</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_c2:
            st.markdown(f"""
            <div class="card glow">
            <h3 style='color: #667eea;'>📍 {area2}</h3>
            <h2 style='color: #ffffff;'>₹{price2:.2f} Lakhs</h2>
            <p style='color: #a8b2d1;'>For 2 BHK, 1200 sqft</p>
            </div>
            """, unsafe_allow_html=True)
        
        diff = abs(price1 - price2)
        cheaper = area1 if price1 < price2 else area2
        
        st.markdown(f"""
        <div class="success-box glow">
        <h4 style='color: #4CAF50;'>💡 Comparison Result</h4>
        <p style='color: #ffffff;'>
        • <b>{cheaper}</b> is more affordable by ₹{diff:.2f} Lakhs<br>
        • Price difference: {((diff/max(price1, price2))*100):.1f}%
        </p>
        </div>
        """, unsafe_allow_html=True)

elif page == "🧮 EMI Calculator":
    st.markdown("---")
    st.markdown("### 🧮 Home Loan EMI Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        loan_amount = st.number_input("💰 Loan Amount (₹ Lakhs)", 10, 500, 50, step=5)
        interest_rate = st.slider("📈 Interest Rate (%)", 6.0, 12.0, 8.5, 0.1)
    
    with col2:
        tenure = st.slider("⏰ Loan Tenure (Years)", 5, 30, 20)
    
    if st.button("Calculate EMI"):
        # EMI calculation
        P = loan_amount * 100000
        r = interest_rate / (12 * 100)
        n = tenure * 12
        
        emi = (P * r * (1 + r)**n) / ((1 + r)**n - 1)
        total_payment = emi * n
        total_interest = total_payment - P
        
        col_e1, col_e2, col_e3 = st.columns(3)
        
        with col_e1:
            st.metric("💳 Monthly EMI", f"₹{emi:,.0f}")
        
        with col_e2:
            st.metric("💵 Total Payment", f"₹{total_payment/100000:.2f} L")
        
        with col_e3:
            st.metric("💸 Total Interest", f"₹{total_interest/100000:.2f} L")
        
        st.markdown(f"""
        <div class="warning-box glow">
        <h4 style='color: #ff9800;'>📊 Loan Breakdown</h4>
        <p style='color: #ffffff;'>
        • Principal Amount: ₹{loan_amount} Lakhs<br>
        • Interest Amount: ₹{total_interest/100000:.2f} Lakhs<br>
        • Loan Tenure: {tenure} years ({n} months)<br>
        • Interest Rate: {interest_rate}% per annum
        </p>
        </div>
        """, unsafe_allow_html=True)

else:  # About page
    st.markdown("---")
    st.markdown("### ℹ️ About This Project")
    
    st.markdown("""
    <div class="info-box glow">
    <h3 style='color: #667eea;'>🏡 AI Real Estate Assistant</h3>
    <p style='color: #a8b2d1;'>This is an intelligent property advisor system built using Machine Learning and Natural Language Processing.</p>
    
    <h4 style='color: #667eea;'>✨ Features:</h4>
    <p style='color: #ffffff;'>
    • 🤖 AI-powered chat assistant for property queries<br>
    • 💰 Accurate price prediction using ML models<br>
    • 📊 Area comparison tools<br>
    • 🧮 EMI calculator for home loans<br>
    • 📈 Real-time market insights<br>
    </p>
    
    <h4 style='color: #667eea;'>🛠️ Technologies Used:</h4>
    <p style='color: #ffffff;'>
    • Python 3.10<br>
    • Streamlit (Web Framework)<br>
    • Scikit-learn (Machine Learning)<br>
    • Pandas & NumPy (Data Processing)<br>
    </p>
    
    <h4 style='color: #667eea;'>📍 Coverage:</h4>
    <p style='color: #ffffff;'>
    Currently covers 10+ major localities in Bangalore including Whitefield, Koramangala, Indiranagar, HSR Layout, and more.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🎯 How to Use")
    
    col_t1, col_t2, col_t3 = st.columns(3)
    
    with col_t1:
        st.markdown("""
        <div class="card">
        <h4 style='color: #667eea;'>1️⃣ Ask Questions</h4>
        <p style='color: #a8b2d1;'>
        Use natural language:<br>
        • "Price of 2BHK in Whitefield?"<br>
        • "Is Koramangala good for investment?"
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_t2:
        st.markdown("""
        <div class="card">
        <h4 style='color: #667eea;'>2️⃣ Get Predictions</h4>
        <p style='color: #a8b2d1;'>
        Select location, BHK, area:<br>
        • Instant price estimates<br>
        • Market comparisons
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_t3:
        st.markdown("""
        <div class="card">
        <h4 style='color: #667eea;'>3️⃣ Calculate EMI</h4>
        <p style='color: #a8b2d1;'>
        Plan your finances:<br>
        • Loan amount<br>
        • Interest rates<br>
        • Tenure options
        </p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p style='color: #667eea; font-size: 18px;'>🏡 AI Real Estate Assistant</p>
        <p style='color: #a8b2d1;'>Built with ❤️ using Streamlit & Python</p>
        <p style='color: #a8b2d1;'>💡 Data-driven insights for smarter property decisions</p>
    </div>
""", unsafe_allow_html=True)