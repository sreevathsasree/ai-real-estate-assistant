from utils.predictor import predict_price

def ai_real_estate_agent(user_prompt):
    prompt = user_prompt.lower()
    
    # Available locations
    locations = ['whitefield', 'electronic city', 'hebbal', 'marathahalli', 
                 'indiranagar', 'koramangala', 'btm layout', 'hsr layout', 
                 'jayanagar', 'rajaji nagar']
    
    # Extract location from user input
    detected_locations = []
    for loc in locations:
        if loc in prompt:
            detected_locations.append(loc.title())
    
    location = detected_locations[0] if detected_locations else "Whitefield"
    
    # Extract BHK
    bhk = 2
    for i in range(1, 6):
        if f'{i}bhk' in prompt or f'{i} bhk' in prompt:
            bhk = i
            break
    
    # Extract sqft
    sqft = 1200
    words = prompt.replace(',', '').split()
    for i, word in enumerate(words):
        if word.isdigit() and int(word) > 400 and int(word) < 10000:
            if i < len(words) - 1 and ('sqft' in words[i+1] or 'sq' in words[i+1]):
                sqft = int(word)
    
    bath = bhk
    
    # Intent detection
    wants_price = any(word in prompt for word in ["price", "cost", "worth", "rate", "how much", "value"])
    wants_advice = any(word in prompt for word in ["good", "invest", "buy", "recommend", "should"])
    wants_comparison = "compar" in prompt or "vs" in prompt or "versus" in prompt
    
    # Handle comparison
    if wants_comparison and len(detected_locations) >= 2:
        loc1, loc2 = detected_locations[0], detected_locations[1]
        price1 = predict_price(loc1, sqft, bhk, bath)
        price2 = predict_price(loc2, sqft, bhk, bath)
        
        cheaper = loc1 if price1 < price2 else loc2
        expensive = loc2 if price1 < price2 else loc1
        diff = abs(price1 - price2)
        
        return (
            f"📊 **Area Comparison**\n\n"
            f"**{loc1}:**\n"
            f"• {bhk} BHK, {sqft} sqft → ₹{price1:.2f} Lakhs\n\n"
            f"**{loc2}:**\n"
            f"• {bhk} BHK, {sqft} sqft → ₹{price2:.2f} Lakhs\n\n"
            f"💡 **Analysis:**\n"
            f"• {cheaper} is more affordable by ₹{diff:.2f} Lakhs\n"
            f"• Price difference: {((diff/max(price1, price2))*100):.1f}%\n"
            f"• {expensive} has higher property values, indicating premium location status"
        )
    
    if wants_price:
        price = predict_price(location, sqft, bhk, bath)
        price_per_sqft = (price * 100000) / sqft
        
        return (
            f"🏡 **Property Price Estimate**\n\n"
            f"📍 **Location:** {location}\n"
            f"🏠 **Configuration:** {bhk} BHK, {sqft} sqft\n"
            f"🚿 **Bathrooms:** {bath}\n\n"
            f"💰 **Estimated Price: ₹{price:.2f} Lakhs**\n"
            f"📊 **Price per sqft: ₹{price_per_sqft:,.0f}**\n\n"
            f"💡 This estimate is based on current market trends in Bangalore.\n"
            f"📈 Actual prices may vary by ±10% based on specific property features."
        )
    
    if wants_advice:
        # Location insights
        insights = {
            'Whitefield': 'IT hub with excellent connectivity and infrastructure',
            'Koramangala': 'Premium locality with vibrant social scene',
            'Indiranagar': 'Established upscale neighborhood with great amenities',
            'HSR Layout': 'Well-planned residential area with good appreciation',
            'Jayanagar': 'Traditional residential area with strong cultural roots',
            'Electronic City': 'Tech corridor with affordable housing options',
            'Marathahalli': 'Major IT employment zone with good rental demand',
            'Hebbal': 'Rapidly developing with excellent connectivity',
            'BTM Layout': 'Popular residential area with good infrastructure',
            'Rajaji Nagar': 'Central location with established residential character'
        }
        
        insight = insights.get(location, 'Emerging residential area with growth potential')
        
        return (
            f"🤖 **Investment Analysis for {location}**\n\n"
            f"📍 **Area Profile:**\n"
            f"{insight}\n\n"
            f"✅ **Strengths:**\n"
            f"• Good appreciation potential (12-15% annually)\n"
            f"• Strong rental demand\n"
            f"• Developing infrastructure\n\n"
            f"💡 **Recommendation:**\n"
            f"Suitable for both end-use and investment. Consider factors like:\n"
            f"• Proximity to workplace\n"
            f"• School/hospital availability\n"
            f"• Future metro connectivity\n\n"
            f"💰 For current pricing, ask: *'What is the price of a {bhk}BHK in {location}?'*"
        )
    
    return (
        "🤖 **AI Real Estate Assistant**\n\n"
        "I can help you with:\n\n"
        "💰 **Price Predictions**\n"
        "👉 *'What is the price of a 3BHK 1500 sqft in Koramangala?'*\n\n"
        "📊 **Area Comparisons**\n"
        "👉 *'Compare Whitefield vs Indiranagar for 2BHK'*\n\n"
        "💡 **Investment Advice**\n"
        "👉 *'Is HSR Layout good for investment?'*\n\n"
        "🏘️ **Covering 10+ Bangalore localities!**"
    )