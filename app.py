import streamlit as st
import sqlite3
from datetime import datetime
from agent.reflection_agent import generate_reflection

# ✅ Page config
st.set_page_config(page_title="ConsciousDay Agent", layout="centered")
st.title("ConsciousDay Agent")
st.write("Reflect inward. Act with clarity.")

# ✅ Database connection
conn = sqlite3.connect('entries.db', check_same_thread=False)
c = conn.cursor()

# 🔧 Create table if not exists (safety check)
c.execute('''
CREATE TABLE IF NOT EXISTS entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    journal TEXT,
    intention TEXT,
    dream TEXT,
    priorities TEXT,
    reflection TEXT,
    strategy TEXT
)
''')
conn.commit()

# ✅ Form inputs
with st.form("journal_form"):
    st.subheader("Morning Journal")
    journal = st.text_area("Write your morning journal here")

    st.subheader("Dream")
    dream = st.text_area("Describe your dream")

    st.subheader("Intention of the Day")
    intention = st.text_input("What's your intention for today?")

    st.subheader("Top 3 Priorities")
    priorities = st.text_area("List your top 3 priorities for today")

    submitted = st.form_submit_button("Submit")

if submitted:
    with st.spinner("Processing your reflection..."):
        try:
            reflection_output = generate_reflection(journal, intention, dream, priorities)
            st.success("Reflection generated successfully!")
        except Exception as e:
            st.error(f"Error generating reflection: {e}")
            reflection_output = "Error generating reflection."

    # ✅ Save to DB
    c.execute('''
        INSERT INTO entries (date, journal, intention, dream, priorities, reflection, strategy)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        datetime.now().strftime("%Y-%m-%d"),
        journal,
        intention,
        dream,
        priorities,
        reflection_output,
        reflection_output  # Using same output for both columns as per current schema
    ))
    conn.commit()

    st.write("### ✨ AI Generated Reflection & Strategy")
    st.write(reflection_output)

# ✅ View previous entries
st.subheader("📅 View Previous Reflections")
selected_date = st.date_input("Select date to view entries")

if st.button("Load Entries"):
    c.execute('SELECT * FROM entries WHERE date=?', (selected_date.strftime("%Y-%m-%d"),))
    data = c.fetchall()
    if data:
        for entry in data:
            st.markdown(f"""
            **Date:** {entry[1]}  
            **Journal:** {entry[2]}  
            **Intention:** {entry[3]}  
            **Dream:** {entry[4]}  
            **Priorities:** {entry[5]}  
            **Reflection & Strategy:** {entry[6]}
            """)
            st.markdown("---")
    else:
        st.info("No entries found for this date.")

# ✅ Close DB connection
conn.close()
