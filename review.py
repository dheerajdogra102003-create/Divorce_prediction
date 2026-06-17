
# from langchain_google_genai import ChatGoogleGenerativeAI


# model = ChatGoogleGenerativeAI(
#     model="gemini-flash-latest", # Changed model name to gemini-flash-latest based on available models
#     temperature=0,
#     # timeout=15
# )


# def review(probability,columns):

#     prompt = f"""
#         You are an experienced marriage counselor.

#         Based on the divorce probability and relationship features provided:

#         1. Explain the relationship status in simple language.
#         2. Identify strengths of the marriage.
#         3. Identify possible risk factors.
#         4. Give practical suggestions for improvement.
#         5. If divorce probability is low, encourage the couple.
#         6. Keep the tone supportive and professional.
#         7. Do not claim certainty. This is only a prediction.

#         ***NOTE: IT should be not be very long so that the reader can be engaged in the review reading do not feel bored. u can also use poetry hinif or english from from any book or poem book by any renounded poet or writer and also can use ethe emoji .
#                  And IT SHOULD BE NOT MOE THAN 150 WORDS.
#         Divorce Probability:
#         {probability}

#         Relationship Features:
#         {columns}

#     """

#     review=model.invoke(prompt).content
#     return review


# if __name__ == "__main__":
#     new_data = [
#         "Age Gap",
#         "Common Interests",
#         "Divorce in the Family of Grade 1",
#         "Compatibility_Score",
#         "Relationship_Strength",
#         "Family_Support",
#         "Economic_Stability",
#         "Marriage_Quality",
#         "Partner_Attractiveness_Score",
#     ]

#     response = review([74, 26], new_data)
#     print(response[0]["text"] if isinstance(response, list) else response)



from langchain_google_genai import ChatGoogleGenerativeAI

# ----------------------------------------
# GEMINI MODEL
# ----------------------------------------

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.4
)


# ----------------------------------------
# AI REVIEW
# ----------------------------------------

def review(
    divorce_probability,
    stable_probability,
    harmony_score,
    strength_score,
    risk_score,
    user_data
):
    

  

    prompt = f"""

You are Harmony AI, an experienced and empathetic marriage counselor.

Analyze the relationship using the prediction results and user inputs.

Relationship Statistics

• Divorce Risk: {divorce_probability}%
• Relationship Stability: {stable_probability}%
• Harmony Score: {harmony_score}%
• Relationship Strength: {strength_score}%
• Risk Index: {risk_score}%

Relationship Features

{user_data}

Instructions

Write a friendly report in LESS THAN 150 WORDS.

Use Markdown.

Your response must follow this structure:

## ❤️ Relationship Summary

(2-3 lines)

## 💚 Strengths

• Bullet Points

## ⚠ Possible Challenges

• Bullet Points

## 🌱 Suggestion

Give 2 practical suggestions.

Finish with one inspirational quote (English or Hindi) from a famous author/poet if appropriate.

Use a few emojis naturally.

Do NOT:
- Mention machine learning.
- Mention AI prediction accuracy.
- Guarantee divorce or marriage success.
- Sound robotic.


DOES: 
-ADD a beautful poem in the end depending on the context and overall report
- use beautifull emoji depending on the overall report


pls make the importent things bold and heghlighted.
"""

    try:

        response = model.invoke(prompt)

        return response.content

    except Exception as e:

        return f"""
## ❌ AI Review Unavailable

Unable to generate the AI review.

**Reason:** {e}

The prediction has been completed successfully, but the AI explanation could not be generated.
"""


# ----------------------------------------
# TEST
# ----------------------------------------

if __name__ == "__main__":

    sample_data = {

        "Age Gap":5,
        "Common Interests":8,
        "Compatibility":88,
        "Relationship Strength":90,
        "Family Support":80,
        "Economic Stability":75,
        "Marriage Quality":85

    }

    print(

        review(

            divorce_probability=18,

            stable_probability=82,

            harmony_score=90,

            strength_score=88,

            risk_score=20,

            user_data=sample_data

        )

    )


