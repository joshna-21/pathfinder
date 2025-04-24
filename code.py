
import pandas as pd
import random

def get_recommendations(user_country, user_background_keywords):
    df = pd.read_csv("roles_and_skills_expanded.csv")
    df_filtered = df[df["Country"].str.lower() == user_country.lower()]
    matching_rows = []

    for _, row in df_filtered.iterrows():
        required_skills = row["Required_Skills"].lower()
        if any(skill.lower() in required_skills for skill in user_background_keywords):
            matching_rows.append(row)

    encouragements = [
        "Remember, every application is a step forward!",
        "Your background is valuable — keep building on it!",
        "Upskilling with a new course can open more doors!"
    ]
    encouragement = random.choice(encouragements)
    reply = ""

    # If exact matches found
    if matching_rows:
        reply += "🤖 Based on your background and target country, here are some suggestions:\n\n"
        for _, row in pd.DataFrame(matching_rows).iterrows():
            reply += f"✅ **Role**: {row['Role']}\n"
            reply += f"💷 **Avg Salary**: {row['Avg_Salary']}\n"
            reply += f"🛠️ **Skills Needed**: {row['Required_Skills']}\n"
            reply += f"🛂 **Visa Options**: {row['Visa_Type']}\n"
            reply += f"📚 **Recommended Course**: {row['Course_Recommendation']}\n"
            reply += f"🌍 **Migration Ease**: {row['Migration_Friendliness']}\n\n"
        reply += encouragement
    else:
        # Try partial matches for learning suggestions
        partial_matches = []
        for _, row in df_filtered.iterrows():
            required = [s.strip().lower() for s in row["Required_Skills"].split(",")]
            user = [s.lower() for s in user_background_keywords]
            missing = list(set(required) - set(user))
            if len(required) - len(missing) >= 1:
                partial_matches.append((row, missing))

        if partial_matches:
            best_match, missing_skills = partial_matches[0]
            reply += (
                f"🤖 You're close to qualifying for a **{best_match['Role']}** role!\n"
                f"🧱 You're missing these skills: {', '.join(missing_skills)}\n"
                f"📚 Suggested course: {best_match['Course_Recommendation']}\n"
                f"{encouragement}"
            )
        else:
            default_roles = df_filtered["Role"].unique()[:3]
            reply += (
                f"🤖 I couldn't find a perfect match, but here are general tech roles in {user_country}: "
                + ", ".join(default_roles)
                + f"\n{encouragement}"
            )

    # Add visa tips
    visa_df = pd.read_csv("visa_tips.csv")
    visa_row = visa_df[visa_df["Country"].str.lower() == user_country.lower()]
    if not visa_row.empty:
        visa_tip = visa_row.iloc[0]["Visa_Tips"]
        reply += f"\n\n💡 **Visa Tip**: {visa_tip}"

    return reply
