# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# from datetime import datetime

# from review import review

# def load_css():

#     with open("assets/style.css") as f:

#         st.markdown(
#             f"<style>{f.read()}</style>",
#             unsafe_allow_html=True
#         )

# load_css()

# # -----------------------------------
# # PAGE CONFIG
# # -----------------------------------

# st.set_page_config(
#     page_title="Harmony",
#     page_icon="❤️",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # -----------------------------------
# # LOAD MODEL
# # -----------------------------------


# @st.cache_resource
# def load_model():
#     loaded = joblib.load("divorce_model.joblib")
#     return loaded["model"], loaded["feature_columns"]

# model, feature_columns = load_model()


# # -----------------------------------
# # SESSION STATE
# # -----------------------------------

# if "history" not in st.session_state:
#     st.session_state.history = []

# if "prediction" not in st.session_state:
#     st.session_state.prediction = None


# if "probability" not in st.session_state:
#     st.session_state.probability = None

# if st.session_state.get("review"):

#     st.markdown(
#         f"""
#         <div class='review-card'>
#         {st.session_state.review}
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# # -----------------------------------
# # HARMONY SCORE
# # -----------------------------------

# def calculate_harmony_score(
#     compatibility,
#     relationship,
#     family_support,
#     economic,
#     marriage_quality,
#     interests
# ):

#     score = (
#         compatibility * 0.22 +
#         relationship * 0.22 +
#         family_support * 0.18 +
#         economic * 0.14 +
#         marriage_quality * 0.14 +
#         (interests * 10) * 0.10
#     )

#     return round(score, 1)


# # -----------------------------------
# # HEALTH INDEX
# # -----------------------------------

# def healthy_factor(
#     compatibility,
#     relationship,
#     family_support,
#     economic,
#     marriage_quality,
#     interests,
#     attractiveness
# ):

#     values = [
#         compatibility,
#         relationship,
#         family_support,
#         economic,
#         marriage_quality,
#         interests * 10,
#         attractiveness
#     ]

#     return round(sum(values) / len(values), 1)


# # -----------------------------------
# # RISK INDEX
# # -----------------------------------

# def risk_factor(
#     age_gap,
#     divorce_family,
#     compatibility,
#     relationship,
#     family_support
# ):

#     risk = (
#         age_gap * 0.30 +
#         divorce_family * 20 +
#         (100 - compatibility) * 0.20 +
#         (100 - relationship) * 0.15 +
#         (100 - family_support) * 0.15
#     )

#     return min(round(risk, 1), 100)


# # -----------------------------------
# # HERO SECTION
# # -----------------------------------

# st.markdown("""
# <div class='hero-title'>
# ❤️ Harmony
# </div>
# """, unsafe_allow_html=True)


# st.markdown("""
# <div class="hero-desc">
# ❤️‍🩹💜 Predict relationship stability using
# <span class="gold-text">Various Relationship Features </span>
# and receive
# <span class="pink-text">AI-powered relationship insights</span>
# designed to uncover hidden compatibility patterns,
# relationship strengths, and future outlook.💜❤️‍🩹
# </div>
# """, unsafe_allow_html=True)


# st.divider()

# # -----------------------------------
# # DASHBOARD
# # -----------------------------------

# col1, col2, col3 = st.columns([1,1,1])

# # -----------------------------------
# # INPUTS
# # -----------------------------------

# with col1:

#     st.subheader("Relationship Inputs")

#     age_gap = st.slider(
#         "Age Gap",
#         0,
#         100,
#         10
#     )

#     common_interests = st.slider(
#         "Common Interests",
#         0,
#         10,
#         5
#     )

#     compatibility = st.slider(
#         "Compatibility Score",
#         0,
#         100,
#         75
#     )

#     relationship_strength = st.slider(
#         "Relationship Strength",
#         0,
#         100,
#         75
#     )

#     family_support = st.slider(
#         "Family Support",
#         0,
#         100,
#         75
#     )

# # -----------------------------------
# # SECOND COLUMN
# # -----------------------------------

# with col2:

#     st.subheader("Additional Metrics")

#     economic_stability = st.slider(
#         "Economic Stability",
#         0,
#         100,
#         75
#     )

#     marriage_quality = st.slider(
#         "Marriage Quality",
#         0,
#         100,
#         75
#     )

#     partner_attractiveness = st.slider(
#         "Partner Attractiveness",
#         0,
#         100,
#         75
#     )

#     divorce_family = st.toggle(
#         "Divorce in Family"
#     )


# # -----------------------------------
# # LIVE METRICS
# # -----------------------------------

# with col3:

#     st.subheader("Live Snapshot")

#     harmony_score = calculate_harmony_score(
#         compatibility,
#         relationship_strength,
#         family_support,
#         economic_stability,
#         marriage_quality,
#         common_interests
#     )

#     healthy = healthy_factor(
#         compatibility,
#         relationship_strength,
#         family_support,
#         economic_stability,
#         marriage_quality,
#         common_interests,
#         partner_attractiveness
#     )

#     risk = risk_factor(
#         age_gap,
#         int(divorce_family),
#         compatibility,
#         relationship_strength,
#         family_support
#     )

#     st.markdown(
#     f"""
#     <div class='metric-card'>
#     <h4>Harmony Score</h4>
#     <h1>{harmony_score}%</h1>
#     </div>
#     """,
#     unsafe_allow_html=True
#     )

#     st.markdown(
#     f"""
#     <div class='metric-card'>
#     <h4>Strength Index</h4>
#     <h1>{healthy}%</h1>
#     </div>
#     """,
#     unsafe_allow_html=True
#     )

#     st.markdown(
#     f"""
#     <div class='metric-card'>
#     <h4>Risk Index</h4>
#     <h1>{risk}%</h1>
#     </div>
#     """,
#     unsafe_allow_html=True
#     )

# # -----------------------------------
# # PREDICT BUTTON
# # -----------------------------------

# st.divider()


# analyze = st.button(
#     "✨ Analyze Relationship with Harmony AI",
#     use_container_width=True
# )
# # -----------------------------------
# # PREDICTION
# # -----------------------------------

# if analyze:

#     input_df = pd.DataFrame({
#         "Age Gap":[age_gap],
#         "Common Interests":[common_interests],
#         "Divorce in the Family of Grade 1":[int(divorce_family)],
#         "Compatibility_Score":[compatibility],
#         "Relationship_Strength":[relationship_strength],
#         "Family_Support":[family_support],
#         "Economic_Stability":[economic_stability],
#         "Marriage_Quality":[marriage_quality],
#         "Partner_Attractiveness_Score":[partner_attractiveness]
#     })


 
#     input_df = input_df.reindex(columns=feature_columns)

#     prediction = model.predict(input_df)
#     probability = model.predict_proba(input_df)[0]
#     divorce_probability = round(probability[1] * 100, 2)
#     stable_probability = round(probability[0] * 100, 2)

#     try:
#         ai_review = review(
#             probability.tolist(),
#             input_df.to_dict()
#         )
#     except Exception as e:
#         ai_review = f"Review Error: {e}"

#     # ✅ SAVE STATE HERE (IMPORTANT)
#     st.session_state.prediction = prediction[0]
#     st.session_state.probability = divorce_probability
#     st.session_state.review = ai_review

#     if model is None:
#         st.error("Model not loaded properly")
#         st.stop()

#     st.session_state.history.append({
#         "Time": datetime.now().strftime("%d-%m-%Y %H:%M"),
#         "Prediction": prediction,
#         "Divorce Probability": divorce_probability,
#         "Harmony Score": harmony_score
#     })

# # -----------------------------------
# # RESULT SECTION
# # -----------------------------------

# if st.session_state.prediction is not None:

#     st.divider()

#     st.markdown("""
#     <div class='section-title'>
#         📊 Prediction Analytics
#     </div>
#     """, unsafe_allow_html=True)

#     c1, c2, c3, c4 = st.columns(4)

#     # -----------------------------------
#     # RESULT CARD
#     # -----------------------------------

#     with c1:

#         if st.session_state.prediction == 1:
#             st.markdown("""
#             <div class='result-card danger-card'>
#                 <h3>🔴 Status</h3>
#                 <h2>High Divorce Risk</h2>
#             </div>
#             """, unsafe_allow_html=True)
#         else:
#             st.markdown("""
#             <div class='result-card success-card'>
#                 <h3>🟢 Status</h3>
#                 <h2>Stable Relationship</h2>
#             </div>
#             """, unsafe_allow_html=True)

#     # -----------------------------------
#     # DIVORCE PROBABILITY
#     # -----------------------------------

#     with c2:
#         st.markdown(f"""
#         <div class='metric-card'>
#             <h4>Divorce Probability</h4>
#             <h1>{st.session_state.divorce_probability}%</h1>
#         </div>
#         """, unsafe_allow_html=True)

#     # -----------------------------------
#     # STABLE PROBABILITY
#     # -----------------------------------

#     with c3:

#         st.markdown(f"""
#         <div class='metric-card'>
#             <h4>Stable Probability</h4>
#             <h1>{st.session_state.stable_probability}%</h1>
#         </div>
#         """, unsafe_allow_html=True)

#     # -----------------------------------
#     # HARMONY SCORE
#     # -----------------------------------

#     with c4:

#         st.markdown(f"""
#         <div class='metric-card'>
#             <h4>Harmony Score</h4>
#             <h1>{harmony_score}%</h1>
#         </div>
#         """, unsafe_allow_html=True)

#     st.divider()

#     st.markdown("""
#     <div class='section-title'>
#         🧠 Harmony AI Review
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown(
#         f"""
#         <div class='review-card'>
#         {st.session_state.review}
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# # -----------------------------------
# # HISTORY
# # -----------------------------------

# if st.session_state.history:

#     st.divider()

#     with st.expander(
#         "Prediction History"
#     ):

#         st.dataframe(
#             pd.DataFrame(
#                 st.session_state.history
#             ),
#             use_container_width=True
#         )





import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
from review import review

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="Divorce prediction dashboard",
    page_icon="❤️Harmony",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------
# LOAD CSS
# -------------------------------------------------------

def load_css():
    with open("assets/style.css", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# -------------------------------------------------------
# LOAD MODEL
# -------------------------------------------------------

@st.cache_resource
def load_model():
    try:
        data = joblib.load("divorce_model.joblib")
        return data["model"], data["feature_columns"]
    except Exception as e:
        st.error(f"Unable to load model.\n\n{e}")
        st.stop()

model, feature_columns = load_model()

# -------------------------------------------------------
# SESSION STATE
# -------------------------------------------------------

defaults = {
    "prediction": None,
    "divorce_probability": None,
    "stable_probability": None,
    "review": "",
    "history": [],
    "risk_score": None,
    "strength_score": None,
    "harmony_score": None
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -------------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------------

def harmony_score(
        compatibility,
        relationship,
        family,
        economic,
        marriage,
        interests):

    score = (
        compatibility*0.22 +
        relationship*0.22 +
        family*0.18 +
        economic*0.14 +
        marriage*0.14 +
        interests*10*0.10
    )

    return round(score,1)


def relationship_strength(
        compatibility,
        relationship,
        family,
        economic,
        marriage,
        attractiveness,
        interests):

    values = [
        compatibility,
        relationship,
        family,
        economic,
        marriage,
        attractiveness,
        interests*10
    ]

    return round(sum(values)/len(values),1)


def risk_index(
        age_gap,
        divorce_family,
        compatibility,
        relationship,
        family):

    risk = (
        age_gap*0.30 +
        divorce_family*20 +
        (100-compatibility)*0.20 +
        (100-relationship)*0.15 +
        (100-family)*0.
    )

    return min(round(risk,1),100)

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

st.markdown(
"""
<div class="hero-title">
❤️ Harmony
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="hero-desc">

AI Powered Relationship Prediction System

Analyze relationship health, compatibility,
future stability and divorce risk using
Machine Learning + Generative AI.

</div>
""",
unsafe_allow_html=True
)

st.divider()

# -------------------------------------------------------
# INPUT AREA
# -------------------------------------------------------

left, middle, right = st.columns([1,1,1])

# -------------------------------------------------------
# LEFT
# -------------------------------------------------------

with left:

    st.subheader("Relationship")

    age_gap = st.slider(
        "Age Gap",
        0,
        50,
        5
    )

    common_interests = st.slider(
        "Common Interests",
        0,
        10,
        5
    )

    compatibility = st.slider(
        "Compatibility",
        0,
        100,
        80
    )

    relationship = st.slider(
        "Relationship Strength",
        0,
        100,
        80
    )

    family_support = st.slider(
        "Family Support",
        0,
        100,
        80
    )

# -------------------------------------------------------
# MIDDLE
# -------------------------------------------------------

with middle:

    st.subheader("Additional Metrics")

    economic = st.slider(
        "Economic Stability",
        0,
        100,
        75
    )

    marriage = st.slider(
        "Marriage Quality",
        0,
        100,
        80
    )

    attractiveness = st.slider(
        "Partner Attractiveness",
        0,
        100,
        75
    )

    divorce_family = st.toggle(
        "Family Divorce History"
    )

# -------------------------------------------------------
# RIGHT DASHBOARD
# -------------------------------------------------------

with right:
    st.subheader("📊 Live Dashboard")

    harmony = harmony_score(
        compatibility,
        relationship,
        family_support,
        economic,
        marriage,
        common_interests
    )

    strength = relationship_strength(
        compatibility,
        relationship,
        family_support,
        economic,
        marriage,
        attractiveness,
        common_interests
    )

    risk = risk_index(
        age_gap,
        int(divorce_family),
        compatibility,
        relationship,
        family_support
    )

    st.session_state.harmony_score = harmony
    st.session_state.strength_score = strength
    st.session_state.risk_score = risk

    st.markdown("### ❤️ Harmony Score")
    st.progress(harmony / 100)
    st.caption(f"{harmony:.1f}%")

    st.markdown("### 🤝 Relationship Strength")
    st.progress(strength / 100)
    st.caption(f"{strength:.1f}%")

    st.markdown("### 💔 Risk Index")
    st.progress(risk / 100)
    st.caption(f"{risk:.1f}%")

# -------------------------------------------------------
# CALCULATE RISK
# -------------------------------------------------------

st.divider()
# -------------------------------------------------------
# AI PREDICTION
# -------------------------------------------------------
analyze = st.button("❤️ Click To Get The Percentage of Risk", use_container_width=True)

if analyze:
    try:

        # ----------------------------------------
        # Create Input DataFrame
        # ----------------------------------------

        input_df = pd.DataFrame({
            "Age Gap": [age_gap],
            "Common Interests": [common_interests],
            "Divorce in the Family of Grade 1": [int(divorce_family)],
            "Compatibility_Score": [compatibility],
            "Relationship_Strength": [relationship],
            "Family_Support": [family_support],
            "Economic_Stability": [economic],
            "Marriage_Quality": [marriage],
            "Partner_Attractiveness_Score": [attractiveness]
        })
        input_df = input_df.reindex(columns=feature_columns)

        # ----------------------------------------
        # Prediction
        # ----------------------------------------

        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0]
        stable_probability = round(probability[0] * 100, 2)
        divorce_probability = round(probability[1] * 100, 2)



        # ----------------------------------------
        # AI Context
        # ----------------------------------------

        context = f"""
        Age Gap: {age_gap} years
        Compatibility: {compatibility}/100
        Relationship Strength: {relationship}/100
        Family Support: {family_support}/100
        Economic Stability: {economic}/100
        Marriage Quality: {marriage}/100
        Common Interests: {common_interests}/10
        Partner Attractiveness: {attractiveness}/100
        Family Divorce History: {"Yes" if divorce_family else "No"}
"""

        # ----------------------------------------
        # AI Review
        # ----------------------------------------

        ai_review = review(
            divorce_probability=divorce_probability,
            stable_probability=stable_probability,
            harmony_score=harmony,
            strength_score=strength,
            risk_score=risk,
            user_data=context
        )

        # ----------------------------------------
        # Save Session State
        # ----------------------------------------

        st.session_state.prediction = prediction
        st.session_state.divorce_probability = divorce_probability
        st.session_state.stable_probability = stable_probability
        st.session_state.review = ai_review

        # ----------------------------------------
        # Save History
        # ----------------------------------------

        result = (
            "High Divorce Risk"
            if prediction == 1
            else
            "Stable Relationship"
        )

        st.session_state.history.append({
            "Time": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "Result": result,
            "Harmony": harmony,
            "Strength": strength,
            "Risk": risk,
            "Divorce Risk": divorce_probability,
            "Stable": stable_probability

        })
    except Exception as e:
        st.error(f"Prediction Error: {e}")



# -------------------------------------------------------
# RESULT DASHBOARD
# -------------------------------------------------------

if st.session_state.prediction is not None:

    st.divider()

    st.markdown(
    """
    ## 📊 Prediction Report
    """
    )

    card1,card2,card3 = st.columns(3)


    if st.session_state.divorce_probability >= 70:
        color = "#ef4444"
        status = "🔴 High Risk"

    elif st.session_state.divorce_probability >= 40:
        color = "#f59e0b"
        status = "🟠 Moderate Risk"

    else:
        color = "#22c55e"
        status = "🟢 Low Risk"

    st.markdown(
        f"""
    <div class="prediction-box">

    <h2>💔 Chance of Divorce</h2>

    <div class="prediction-value" style="color:{color};">
    {st.session_state.divorce_probability:.1f}%
    </div>

    <div class="prediction-status">
    {status}
    </div>

    <div class="prediction-bar">
    <div class="prediction-fill"
    style="width:{st.session_state.divorce_probability:.1f}%;
    background:{color};">
    </div>
    </div>

    </div>
    """,
        unsafe_allow_html=True
    )
    st.write("")

    

# -------------------------------------------------------
# AI REVIEW
# -------------------------------------------------------

    st.divider()
    st.markdown("🧠 Harmony AI Review")
    st.write(st.session_state.review)

# -------------------------------------------------------
# HISTORY
# -------------------------------------------------------

if len(st.session_state.history)>0:

    st.divider()

    st.markdown("## 📜 Prediction History")

    history_df = pd.DataFrame(

        st.session_state.history

    )

    st.dataframe(

        history_df,

        use_container_width=True,

        hide_index=True

    )

    csv = history_df.to_csv(index=False)

    st.download_button(

        "⬇ Download History",

        csv,

        "prediction_history.csv",

        "text/csv",

        use_container_width=True

    )




import random
import streamlit as st

# -------------------------------
# Floating Hearts
# -------------------------------

hearts = ""

for _ in range(60):   # Increase to 80 if you want

    hearts += f"""
    <span class="floating-heart"
        style="
            left:{random.randint(0,100)}%;
            animation-delay:{random.uniform(0,20):.2f}s;
            animation-duration:{random.uniform(10,20):.2f}s;
            font-size:{random.randint(18,42)}px;
            opacity:{random.uniform(0.08,0.18):.2f};">
        {random.choice(["❤️","💜","💕","💖","💗"])}
    </span>
    """

st.markdown(
    f"""
    <div class="heart-container">
        {hearts}
    </div>
    """,
    unsafe_allow_html=True
)


