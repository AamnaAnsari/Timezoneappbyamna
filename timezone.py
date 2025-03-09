
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
    "Africa/Cairo",
    "America/Chicago",
    "America/Toronto",
    "Asia/Singapore",
    "Asia/Hong_Kong",
    "Asia/Shanghai",
    "Europe/Madrid",
    "Europe/Paris",
    "Europe/Rome",
    "Pacific/Auckland",
    "America/Mexico_City"
]

# Create app title with styling
st.title("🕰️ Time Zone Converter")
st.markdown("An easy-to-use app for checking and converting time zones. 🌎")

# Create a multi-select dropdown for choosing time zones
st.sidebar.header("🌍 Select Timezones")
selected_timezone = st.sidebar.multiselect(
    "Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

# Display current time for selected time zones
st.subheader("📌 Current Time in Selected Timezones")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")

# Create section for time conversion
st.subheader("🔄 Convert Time Between Timezones")
current_time = st.time_input("🕒 Enter Time", value=datetime.now().time())
from_tz = st.selectbox("🌐 From Timezone", TIME_ZONES, index=0)
to_tz = st.selectbox("🌏 To Timezone", TIME_ZONES, index=1)


if st.button("🔄 Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"✅ Converted Time in {to_tz}: {converted_time}")

# Footer 
st.markdown("---")
st.markdown("### 🛠️ Design by Aamna Ansari")
