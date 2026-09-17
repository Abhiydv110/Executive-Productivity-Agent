import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Executive Productivity Agent",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("📊 Executive Productivity Agent")

st.write(
    "AI-powered productivity dashboard for Arjun Malhotra, VP Sales"
)

# -----------------------------
# Executive Information
# -----------------------------
st.subheader("Executive Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Executive", "Arjun Malhotra")

with col2:
    st.metric("Role", "VP Sales")

with col3:
    st.metric("Week", "21–25 Sep 2026")

# -----------------------------
# Navigation
# -----------------------------
st.divider()

st.subheader("Agent Modules")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🎯 Priorities\n\nIdentify urgent tasks")

with col2:
    st.info("📌 Commitments\n\nTrack open commitments")

with col3:
    st.info("📅 Calendar\n\nCheck schedule conflicts")

with col4:
    st.info("🔎 Evidence\n\nTrace information to sources")

# -----------------------------
# Executive Task Data
# -----------------------------

tasks = [
    {
        "Task": "Send updated vendor list",
        "Owner": "Arjun Malhotra",
        "Related Person": "Raghav Sethi",
        "Deadline": "2026-09-23 09:00",
        "Status": "Pending",
        "Priority": "High",
        "Category": "Commitment",
        "Source": "Leadership Sync + Vendor List emails"
    },
    {
        "Task": "Review Q3 campaign deck",
        "Owner": "Arjun Malhotra",
        "Related Person": "Neha Kapoor",
        "Deadline": "2026-09-24 09:30",
        "Status": "Ready for review",
        "Priority": "High",
        "Category": "Review",
        "Source": "Q3 Campaign Deck emails"
    },
    {
        "Task": "Attend Meridian Logistics call",
        "Owner": "Arjun Malhotra",
        "Related Person": "Priya Nair",
        "Deadline": "2026-09-23 15:00",
        "Status": "Confirmed",
        "Priority": "High",
        "Category": "Client",
        "Source": "Call Reschedule emails + Calendar"
    },
    {
        "Task": "Review July expense variance report",
        "Owner": "Arjun Malhotra",
        "Related Person": "Divya Rao",
        "Deadline": "2026-09-24 09:00",
        "Status": "Report received",
        "Priority": "High",
        "Category": "Finance",
        "Source": "Expense Variance Report emails"
    },
    {
        "Task": "Identify owner for Mumbai office lease renewal",
        "Owner": "Unassigned",
        "Related Person": "Facilities / Raghav Sethi / Divya Rao",
        "Deadline": "2026-09-25 17:00",
        "Status": "Unassigned",
        "Priority": "Critical",
        "Category": "Escalation",
        "Source": "Mumbai Office Lease Renewal emails"
    }
]

tasks_df = pd.DataFrame(tasks)

# Convert deadline into datetime
tasks_df["Deadline"] = pd.to_datetime(tasks_df["Deadline"])

# -----------------------------
# Priority Dashboard
# -----------------------------

st.divider()

st.header("🎯 Executive Priorities")

st.dataframe(
    tasks_df[
        [
            "Task",
            "Owner",
            "Deadline",
            "Status",
            "Priority",
            "Category"
        ]
    ],
    use_container_width=True,
    hide_index=True
)
# -----------------------------
# Priority Summary
# -----------------------------

st.subheader("🚨 What Needs Attention")

critical_tasks = tasks_df[
    tasks_df["Priority"] == "Critical"
]

high_tasks = tasks_df[
    tasks_df["Priority"] == "High"
]

unassigned_tasks = tasks_df[
    tasks_df["Owner"] == "Unassigned"
]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Critical",
        len(critical_tasks)
    )

with col2:
    st.metric(
        "High Priority",
        len(high_tasks)
    )

with col3:
    st.metric(
        "Unassigned",
        len(unassigned_tasks)
    )

# -----------------------------
# Critical Items
# -----------------------------

if len(critical_tasks) > 0:

    st.warning("⚠️ Critical item requiring attention")

    for _, task in critical_tasks.iterrows():

        st.markdown(
            f"""
            **{task['Task']}**

            - Owner: {task['Owner']}
            - Deadline: {task['Deadline'].strftime('%d %b %Y, %I:%M %p')}
            - Status: {task['Status']}
            - Source: {task['Source']}
            """
        )

# -----------------------------
# Open Commitments
# -----------------------------

st.divider()

st.header("📌 Open Commitments")

open_commitments = tasks_df[
    (tasks_df["Owner"] == "Arjun Malhotra") &
    (~tasks_df["Status"].isin(["Confirmed", "Report received"]))
]

if len(open_commitments) == 0:

    st.success("No open commitments.")

else:

    for _, task in open_commitments.iterrows():

        st.info(
            f"""
            **{task['Task']}**

            **Deadline:** {task['Deadline'].strftime('%d %b %Y, %I:%M %p')}

            **Related to:** {task['Related Person']}

            **Current status:** {task['Status']}

            **Source:** {task['Source']}
            """
        )

# -----------------------------
# Calendar Monitor
# -----------------------------

st.divider()

st.header("📅 Calendar Monitor")

calendar_events = [
    {
        "Date": "21 Sep 2026",
        "Time": "09:00–09:35",
        "Event": "Leadership Sync",
        "Type": "Meeting"
    },
    {
        "Date": "21 Sep 2026",
        "Time": "14:00–14:30",
        "Event": "1:1 with Neha",
        "Type": "Meeting"
    },
    {
        "Date": "21 Sep 2026",
        "Time": "16:00–17:00",
        "Event": "Blocked",
        "Type": "Blocked"
    },
    {
        "Date": "22 Sep 2026",
        "Time": "11:00–12:00",
        "Event": "Internal Budget Review",
        "Type": "Meeting"
    },
    {
        "Date": "22 Sep 2026",
        "Time": "15:00–15:30",
        "Event": "Blocked",
        "Type": "Blocked"
    },
    {
        "Date": "23 Sep 2026",
        "Time": "15:00–15:30",
        "Event": "Call — Meridian Logistics",
        "Type": "Client"
    },
    {
        "Date": "23 Sep 2026",
        "Time": "18:00–18:15",
        "Event": "Blocked",
        "Type": "Blocked"
    },
    {
        "Date": "24 Sep 2026",
        "Time": "09:00–10:00",
        "Event": "Board Prep Session",
        "Type": "Meeting"
    },
    {
        "Date": "24 Sep 2026",
        "Time": "16:00–17:00",
        "Event": "Hiring Panel — Sales Associate",
        "Type": "Meeting"
    },
    {
        "Date": "25 Sep 2026",
        "Time": "10:00–10:30",
        "Event": "Facilities Check-in",
        "Type": "Meeting"
    },
    {
        "Date": "25 Sep 2026",
        "Time": "13:00–14:00",
        "Event": "Blocked",
        "Type": "Blocked"
    }
]

calendar_df = pd.DataFrame(calendar_events)

st.dataframe(
    calendar_df,
    use_container_width=True,
    hide_index=True
)
# -----------------------------
# Source Evidence
# -----------------------------

st.divider()

st.header("🔎 Source Evidence")

selected_task = st.selectbox(
    "Select a task to view its source evidence:",
    tasks_df["Task"].tolist()
)

selected_row = tasks_df[
    tasks_df["Task"] == selected_task
].iloc[0]

st.markdown("### Task Details")

st.write(f"**Task:** {selected_row['Task']}")
st.write(f"**Owner:** {selected_row['Owner']}")
st.write(f"**Related Person:** {selected_row['Related Person']}")
st.write(f"**Status:** {selected_row['Status']}")
st.write(f"**Priority:** {selected_row['Priority']}")

st.markdown("### 📚 Source")

st.info(
    selected_row["Source"]
)

st.caption(
    "The agent uses the provided assignment data as its source material."
)
# -----------------------------
# Ask the Executive Agent
# -----------------------------

st.divider()

st.header("🤖 Ask the Executive Agent")

st.write(
    "Ask questions about Arjun's priorities, commitments, meetings, "
    "deadlines, and source evidence."
)

question = st.text_input(
    "Ask your question:",
    placeholder="Example: What needs my attention?"
)

if question:

    question_lower = question.lower()

    # --------------------------------
    # Question: What needs attention?
    # --------------------------------
    if (
        "attention" in question_lower
        or "priority" in question_lower
        or "urgent" in question_lower
        or "important" in question_lower
    ):

        st.subheader("Agent Response")

        for _, task in tasks_df.iterrows():

            if (
                task["Priority"] in ["Critical", "High"]
                or task["Owner"] == "Unassigned"
            ):

                st.warning(
                    f"""
                    **{task['Task']}**

                    Priority: {task['Priority']}  
                    Deadline: {task['Deadline'].strftime('%d %b %Y, %I:%M %p')}  
                    Status: {task['Status']}
                    """
                )

    # --------------------------------
    # Question: Commitments
    # --------------------------------
    elif "commitment" in question_lower or "promised" in question_lower:

        st.subheader("Agent Response")

        commitments = tasks_df[
            tasks_df["Owner"] == "Arjun Malhotra"
        ]

        for _, task in commitments.iterrows():

            st.info(
                f"""
                **{task['Task']}**

                Deadline: {task['Deadline'].strftime('%d %b %Y, %I:%M %p')}  
                Status: {task['Status']}  
                Related to: {task['Related Person']}
                """
            )

    # --------------------------------
    # Question: Calendar
    # --------------------------------
    elif (
        "calendar" in question_lower
        or "meeting" in question_lower
        or "schedule" in question_lower
    ):

        st.subheader("Agent Response")

        st.dataframe(
            calendar_df,
            use_container_width=True,
            hide_index=True
        )

    # --------------------------------
    # Question: Lease / Mumbai
    # --------------------------------
    elif (
        "lease" in question_lower
        or "mumbai" in question_lower
        or "office" in question_lower
    ):

        st.subheader("Agent Response")

        lease = tasks_df[
            tasks_df["Task"].str.contains(
                "Mumbai office lease",
                case=False
            )
        ]

        for _, task in lease.iterrows():

            st.warning(
                f"""
                **{task['Task']}**

                Owner: {task['Owner']}  
                Deadline: {task['Deadline'].strftime('%d %b %Y, %I:%M %p')}  
                Status: {task['Status']}  

                **Source:** {task['Source']}
                """
            )

    # --------------------------------
    # Question: Vendor
    # --------------------------------
    elif "vendor" in question_lower:

        st.subheader("Agent Response")

        vendor = tasks_df[
            tasks_df["Task"].str.contains(
                "vendor list",
                case=False
            )
        ]

        for _, task in vendor.iterrows():

            st.warning(
                f"""
                **{task['Task']}**

                Owner: {task['Owner']}  
                Deadline: {task['Deadline'].strftime('%d %b %Y, %I:%M %p')}  
                Status: {task['Status']}  

                **Source:** {task['Source']}
                """
            )

    # --------------------------------
    # Question: Campaign
    # --------------------------------
    elif (
        "campaign" in question_lower
        or "deck" in question_lower
    ):

        st.subheader("Agent Response")

        campaign = tasks_df[
            tasks_df["Task"].str.contains(
                "campaign deck",
                case=False
            )
        ]

        for _, task in campaign.iterrows():

            st.info(
                f"""
                **{task['Task']}**

                Deadline: {task['Deadline'].strftime('%d %b %Y, %I:%M %p')}  
                Status: {task['Status']}  
                Related to: {task['Related Person']}  

                **Source:** {task['Source']}
                """
            )

    # --------------------------------
    # Question: Finance / Expense
    # --------------------------------
    elif (
        "expense" in question_lower
        or "finance" in question_lower
        or "variance" in question_lower
    ):

        st.subheader("Agent Response")

        finance = tasks_df[
            tasks_df["Task"].str.contains(
                "expense variance",
                case=False
            )
        ]

        for _, task in finance.iterrows():

            st.success(
                f"""
                **{task['Task']}**

                Deadline: {task['Deadline'].strftime('%d %b %Y, %I:%M %p')}  
                Status: {task['Status']}  
                Related to: {task['Related Person']}  

                **Source:** {task['Source']}
                """
            )

    # --------------------------------
    # Unknown Question
    # --------------------------------
    else:

        st.info(
            "I can answer questions about priorities, commitments, "
            "calendar, vendor list, campaign deck, expense report, "
            "and Mumbai office lease renewal using the provided source data."
        )

# -----------------------------
# Data & Assumptions
# -----------------------------

st.divider()

with st.expander("📚 Data Sources & Assumptions"):

    st.markdown("""
    ### Input Sources

    - Leadership Sync meeting transcript
    - Arjun Malhotra's calendar
    - Email threads
    - Personal voice notes
    - People/contact information

    ### Agent User

    **Arjun Malhotra — VP Sales**

    ### Information Sources

    - Neha Kapoor — Marketing Lead
    - Raghav Sethi — Ops Manager
    - Divya Rao — Finance
    - Priya Nair — Meridian Logistics
    - Facilities — Internal distribution list

    ### Assumptions

    - The agent only uses information provided in the assignment.
    - Deadlines are taken from explicit commitments or confirmed meetings.
    - "Unassigned" tasks are flagged for executive attention.
    - Source evidence is displayed with task information.
    - The agent does not invent missing information.
    """)

# -----------------------------
# Day-wise Executive View
# -----------------------------

st.divider()

st.header("📅 Day-wise Executive View")

day_options = [
    "Monday — 21 Sep 2026",
    "Tuesday — 22 Sep 2026",
    "Wednesday — 23 Sep 2026",
    "Thursday — 24 Sep 2026",
    "Friday — 25 Sep 2026"
]

selected_day = st.selectbox(
    "Select a day:",
    day_options
)

selected_date = selected_day.split(" — ")[1]

# -----------------------------
# Day-wise Calendar
# -----------------------------

st.subheader(f"🗓️ Calendar — {selected_day}")

day_calendar = calendar_df[
    calendar_df["Date"] == selected_date
]

if len(day_calendar) > 0:
    st.dataframe(
        day_calendar,
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("No calendar events found for this day.")

# -----------------------------
# Day-wise Tasks
# -----------------------------

st.subheader(f"🎯 Tasks & Priorities — {selected_day}")

day_tasks = tasks_df[
    tasks_df["Deadline"].dt.strftime("%d %b %Y") == selected_date
]

if len(day_tasks) > 0:

    st.dataframe(
        day_tasks[
            [
                "Task",
                "Owner",
                "Deadline",
                "Status",
                "Priority",
                "Category"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("No task deadlines recorded for this day.")

# -----------------------------
# Day-wise Attention
# -----------------------------

st.subheader("🚨 Attention for This Day")

if len(day_tasks) > 0:

    for _, task in day_tasks.iterrows():

        if task["Priority"] == "Critical":
            st.error(
                f"🔴 **{task['Task']}** — Critical"
            )

        elif task["Priority"] == "High":
            st.warning(
                f"🟠 **{task['Task']}** — High Priority"
            )

        else:
            st.info(
                f"🔵 **{task['Task']}** — {task['Priority']}"
            )

else:
    st.success("No tracked task deadline for this day.")