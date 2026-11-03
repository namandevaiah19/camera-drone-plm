import streamlit as st
import pandas as pd

# ====================== DATA ======================
components = [
    {"Component_ID": "BAT-001", "Component_Name": "Flight Battery Pack", "System": "Energy", "Specification": "14.8V 6000mAh LiPo", "Supplier": "Supplier A", "Unit_Cost_INR": 4200, "Revision": "A", "Status": "Active"},
    {"Component_ID": "CAM-001", "Component_Name": "4K Camera Module", "System": "Imaging", "Specification": "1/1.3 inch CMOS, 4K/60fps", "Supplier": "Supplier B", "Unit_Cost_INR": 8900, "Revision": "B", "Status": "Active"},
    {"Component_ID": "GIM-001", "Component_Name": "3-Axis Gimbal", "System": "Stabilization", "Specification": "Brushless, high accuracy", "Supplier": "Supplier C", "Unit_Cost_INR": 6700, "Revision": "A", "Status": "Active"},
    {"Component_ID": "FC-001", "Component_Name": "Flight Controller", "System": "Avionics", "Specification": "Dual IMU + GPS + obstacle sensing", "Supplier": "Supplier D", "Unit_Cost_INR": 5800, "Revision": "A", "Status": "Active"},
    {"Component_ID": "MOT-001", "Component_Name": "Brushless Motors (set of 4)", "System": "Propulsion", "Specification": "2306 2400KV", "Supplier": "Supplier E", "Unit_Cost_INR": 3200, "Revision": "A", "Status": "Active"},
    {"Component_ID": "PROP-001", "Component_Name": "Carbon Propellers", "System": "Propulsion", "Specification": "8-inch low-noise", "Supplier": "Supplier F", "Unit_Cost_INR": 850, "Revision": "A", "Status": "Active"},
    {"Component_ID": "FRM-001", "Component_Name": "Carbon Fiber Airframe", "System": "Structure", "Specification": "Foldable arms", "Supplier": "Supplier G", "Unit_Cost_INR": 7500, "Revision": "B", "Status": "Active"},
    {"Component_ID": "GPS-001", "Component_Name": "GNSS Module", "System": "Navigation", "Specification": "Dual-band GPS + GLONASS", "Supplier": "Supplier H", "Unit_Cost_INR": 2100, "Revision": "A", "Status": "Active"},
    {"Component_ID": "RC-001", "Component_Name": "Remote Controller", "System": "Control", "Specification": "5.5 inch screen", "Supplier": "Supplier I", "Unit_Cost_INR": 9800, "Revision": "A", "Status": "Active"},
    {"Component_ID": "SEN-001", "Component_Name": "Obstacle Avoidance Sensors", "System": "Safety", "Specification": "Forward + downward vision", "Supplier": "Supplier J", "Unit_Cost_INR": 3400, "Revision": "A", "Status": "Active"},
    {"Component_ID": "ENC-001", "Component_Name": "Battery Enclosure", "System": "Energy", "Specification": "IP54 quick-release", "Supplier": "Supplier L", "Unit_Cost_INR": 1800, "Revision": "A", "Status": "Active"},
]

changes = [
    {"Change_ID": "ECR-001", "Change_Request": "Increase battery capacity to 7000mAh", "Reason": "Improve flight time", "Affected_System": "Energy", "Priority": "High", "Status": "Open", "Proposed_Revision": "B"},
    {"Change_ID": "ECR-002", "Change_Request": "Upgrade camera to 4K/120fps", "Reason": "Better slow-motion", "Affected_System": "Imaging", "Priority": "Medium", "Status": "In Review", "Proposed_Revision": "C"},
    {"Change_ID": "ECR-003", "Change_Request": "Improve gimbal vibration damping", "Reason": "Reduce video jitter", "Affected_System": "Stabilization", "Priority": "High", "Status": "Open", "Proposed_Revision": "B"},
    {"Change_ID": "ECR-004", "Change_Request": "Add side obstacle sensors", "Reason": "Better safety", "Affected_System": "Safety", "Priority": "Critical", "Status": "Approved", "Proposed_Revision": "B"},
    {"Change_ID": "ECR-005", "Change_Request": "Change propeller material", "Reason": "Reduce noise", "Affected_System": "Propulsion", "Priority": "Medium", "Status": "Closed", "Proposed_Revision": "B"},
    {"Change_ID": "ECR-006", "Change_Request": "Strengthen foldable arm hinges", "Reason": "Improve durability", "Affected_System": "Structure", "Priority": "High", "Status": "Open", "Proposed_Revision": "B"},
    {"Change_ID": "ECR-007", "Change_Request": "Update flight controller firmware", "Reason": "Better wind resistance", "Affected_System": "Avionics", "Priority": "High", "Status": "In Review", "Proposed_Revision": "B"},
    {"Change_ID": "ECR-008", "Change_Request": "Revise battery charging protocol", "Reason": "Faster safe charging", "Affected_System": "Energy", "Priority": "Medium", "Status": "Closed", "Proposed_Revision": "B"},
]

impacts = [
    {"Change_ID": "ECR-001", "Component_ID": "BAT-001", "Impact_Type": "Direct", "Explanation": "Battery capacity and size change", "Action": "Revise battery specification"},
    {"Change_ID": "ECR-001", "Component_ID": "ENC-001", "Impact_Type": "Mechanical", "Explanation": "Larger cells need enclosure check", "Action": "Check CAD packaging"},
    {"Change_ID": "ECR-001", "Component_ID": "FC-001", "Impact_Type": "Software", "Explanation": "Update power management", "Action": "Validate flight controller settings"},
    {"Change_ID": "ECR-003", "Component_ID": "GIM-001", "Impact_Type": "Direct", "Explanation": "Damping redesign", "Action": "Revise gimbal design"},
    {"Change_ID": "ECR-003", "Component_ID": "CAM-001", "Impact_Type": "Interface", "Explanation": "Check camera mounting", "Action": "Verify balance"},
    {"Change_ID": "ECR-006", "Component_ID": "FRM-001", "Impact_Type": "Structural", "Explanation": "Hinge geometry change", "Action": "Perform stress validation"},
]

tests = [
    {"Test_ID": "TST-001", "Change_ID": "ECR-001", "Component_ID": "BAT-001", "Test_Name": "Battery capacity test", "Acceptance_Criteria": "Meets 7000mAh target", "Test_Status": "Pending"},
    {"Test_ID": "TST-002", "Change_ID": "ECR-001", "Component_ID": "ENC-001", "Test_Name": "Enclosure fit check", "Acceptance_Criteria": "No interference", "Test_Status": "Pending"},
    {"Test_ID": "TST-003", "Change_ID": "ECR-003", "Component_ID": "GIM-001", "Test_Name": "Vibration damping test", "Acceptance_Criteria": "Jitter within limit", "Test_Status": "Pending"},
    {"Test_ID": "TST-004", "Change_ID": "ECR-006", "Component_ID": "FRM-001", "Test_Name": "Hinge stress test", "Acceptance_Criteria": "Passes load criteria", "Test_Status": "Pending"},
]

service = [
    {"Service_ID": "SRV-001", "Component_ID": "BAT-001", "Issue": "Reduced flight time", "Recommended_Action": "Check battery health and calibration", "Interval_or_Trigger": "When flight time drops", "Safety_Note": "Do not puncture battery"},
    {"Service_ID": "SRV-002", "Component_ID": "CAM-001", "Issue": "Blurry or shaky video", "Recommended_Action": "Calibrate gimbal and clean lens", "Interval_or_Trigger": "When video quality drops", "Safety_Note": "Power off before cleaning"},
    {"Service_ID": "SRV-003", "Component_ID": "PROP-001", "Issue": "Unusual noise or vibration", "Recommended_Action": "Inspect and replace damaged propellers", "Interval_or_Trigger": "Before every flight", "Safety_Note": "Never fly with cracked props"},
    {"Service_ID": "SRV-004", "Component_ID": "FRM-001", "Issue": "Loose or stiff folding arms", "Recommended_Action": "Inspect hinges and tighten fasteners", "Interval_or_Trigger": "During routine check", "Safety_Note": "Ensure arms lock properly"},
]

# Convert to DataFrames
comp_df = pd.DataFrame(components)
change_df = pd.DataFrame(changes)
impact_df = pd.DataFrame(impacts)
test_df = pd.DataFrame(tests)
service_df = pd.DataFrame(service)

# ====================== HELPER FUNCTIONS ======================
def find_component(query):
    query = query.lower()
    results = []
    for _, row in comp_df.iterrows():
        if (query in row["Component_ID"].lower() or 
            query in row["Component_Name"].lower() or 
            query in row["System"].lower() or
            "battery" in query and "bat" in row["Component_ID"].lower()):
            results.append(row)
    return results

def get_open_changes():
    return change_df[change_df["Status"].str.lower() == "open"]

def get_impacts(change_id):
    return impact_df[impact_df["Change_ID"].str.upper() == change_id.upper()]

def get_tests(change_id):
    return test_df[test_df["Change_ID"].str.upper() == change_id.upper()]

def get_service(query):
    query = query.lower()
    results = []
    for _, row in service_df.iterrows():
        if (query in row["Component_ID"].lower() or 
            query in row["Issue"].lower() or
            "brake" in query or "battery" in query or "camera" in query or "propeller" in query or "arm" in query or "frame" in query):
            results.append(row)
    return results

# ====================== STREAMLIT UI ======================
st.set_page_config(page_title="Cam Drone PLM Agent", page_icon="🛸", layout="wide")

st.title("🛸 Cam Drone X2 — PLM Agentic AI")
st.caption("Educational Product Lifecycle Management Assistant | Consumer Camera Drone")

st.markdown("### Ask me anything about the drone PLM data")
st.markdown("""
**Example questions you can try:**
- What is the battery capacity / specification?
- Which components are affected by ECR-001?
- What tests are needed for ECR-001?
- Which engineering changes are still open?
- What maintenance is recommended for the battery / camera / propellers?
""")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # ---------- Simple Agent Logic ----------
    prompt_lower = prompt.lower()
    response = ""

    # 1. Battery related
    if "battery" in prompt_lower or "capacity" in prompt_lower or "flight time" in prompt_lower:
        bat = comp_df[comp_df["Component_ID"] == "BAT-001"].iloc[0]
        response = f"""**Battery Information (BAT-001)**

- Name: {bat['Component_Name']}
- Specification: **{bat['Specification']}**
- Supplier: {bat['Supplier']}
- Cost: ₹{bat['Unit_Cost_INR']}
- Revision: {bat['Revision']}
- Status: {bat['Status']}
"""

    # 2. Open changes
    elif "open" in prompt_lower and ("change" in prompt_lower or "ecr" in prompt_lower):
        open_changes = get_open_changes()
        response = "**Currently Open Engineering Changes:**\n\n"
        for _, row in open_changes.iterrows():
            response += f"- **{row['Change_ID']}**: {row['Change_Request']} (Priority: {row['Priority']})\n"

    # 3. Impact of a change
    elif "affected" in prompt_lower or "impact" in prompt_lower:
        change_id = None
        for cid in ["ECR-001", "ECR-002", "ECR-003", "ECR-004", "ECR-005", "ECR-006", "ECR-007", "ECR-008"]:
            if cid.lower() in prompt_lower:
                change_id = cid
                break
        if change_id:
            imps = get_impacts(change_id)
            if not imps.empty:
                response = f"**Components affected by {change_id}:**\n\n"
                for _, row in imps.iterrows():
                    response += f"- **{row['Component_ID']}** ({row['Impact_Type']}): {row['Explanation']} → Action: {row['Action']}\n"
            else:
                response = f"No detailed impact records found for {change_id} in the current dataset."
        else:
            response = "Please mention the Change ID (example: ECR-001)"

    # 4. Tests
    elif "test" in prompt_lower:
        change_id = None
        for cid in ["ECR-001", "ECR-002", "ECR-003", "ECR-004", "ECR-005", "ECR-006"]:
            if cid.lower() in prompt_lower:
                change_id = cid
                break
        if change_id:
            tsts = get_tests(change_id)
            if not tsts.empty:
                response = f"**Tests required for {change_id}:**\n\n"
                for _, row in tsts.iterrows():
                    response += f"- **{row['Test_ID']}**: {row['Test_Name']} — Status: {row['Test_Status']}\n  Acceptance: {row['Acceptance_Criteria']}\n"
            else:
                response = f"No tests listed yet for {change_id}."
        else:
            response = "Please mention the Change ID (example: What tests are needed for ECR-001?)"

    # 5. Maintenance / Service
    elif "maintenance" in prompt_lower or "service" in prompt_lower or "recommended" in prompt_lower:
        results = get_service(prompt_lower)
        if results:
            response = "**Maintenance / Service Guidance:**\n\n"
            for row in results:
                response += f"- **{row['Component_ID']}** ({row['Issue']}):\n  Action: {row['Recommended_Action']}\n  When: {row['Interval_or_Trigger']}\n  Safety: {row['Safety_Note']}\n\n"
        else:
            response = "Try asking about battery, camera, propeller, or frame maintenance."

    # 6. General component search
    elif "component" in prompt_lower or "part" in prompt_lower:
        results = find_component(prompt_lower)
        if results:
            response = "**Matching Components:**\n\n"
            for row in results:
                response += f"- **{row['Component_ID']}**: {row['Component_Name']} | {row['Specification']}\n"
        else:
            response = "No matching component found. Try 'battery', 'camera', 'gimbal', etc."

    else:
        response = """I can help you with:
- Battery / component specifications
- Open engineering changes
- Impact of any ECR (e.g. ECR-001)
- Required tests for a change
- Maintenance recommendations

Try one of the example questions above!"""

    # Show response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})