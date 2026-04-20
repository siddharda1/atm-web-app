import streamlit as st

st.set_page_config(page_title="ATM App", page_icon="🏦", layout="wide")

st.title("🏦 ATM Web App")

# DATA
if "accounts" not in st.session_state:
    st.session_state.accounts = {
        "1234567890123456": {"name": "N Siddharda ", "pin": "1234", "balance": 50500}
    }

if "logged_in" not in st.session_state:
    st.session_state.logged_in = True
    st.session_state.user = "1234567890123456"

user = st.session_state.accounts[st.session_state.user]

# SIDEBAR (CLEAN)
with st.sidebar:
    st.header("👤 Account")
    st.write(user["name"])
    st.write(f"💰 ₹{user['balance']}")

    st.markdown("---")

    st.header("🔐 Change PIN")
    old = st.text_input("Current PIN", type="password")
    new = st.text_input("New PIN", type="password")

    if st.button("Update PIN"):
        if old == user["pin"]:
            user["pin"] = new
            st.success("PIN updated")
        else:
            st.error("Wrong PIN")

    st.markdown("---")

    if st.button("Logout"):
        st.session_state.logged_in = False

# MAIN AREA
st.subheader("🏧 Select Operation")

col1, col2, col3 = st.columns(3)

if col1.button("💰 Balance"):
    st.success(f"Your Balance: ₹{user['balance']}")

if col2.button("➕ Deposit"):
    st.session_state.action = "deposit"

if col3.button("➖ Withdraw"):
    st.session_state.action = "withdraw"

# ACTION AREA
if st.session_state.get("action") == "deposit":
    with st.expander("➕ Deposit Money"):
        amt = st.number_input("Enter amount", min_value=0)
        pin = st.text_input("Enter PIN", type="password")

        if st.button("Confirm Deposit"):
            if pin == user["pin"]:
                user["balance"] += amt
                st.success("Deposited successfully")
            else:
                st.error("Wrong PIN")

if st.session_state.get("action") == "withdraw":
    with st.expander("➖ Withdraw Money"):
        amt = st.number_input("Enter amount", min_value=0)
        pin = st.text_input("Enter PIN", type="password")

        if st.button("Confirm Withdraw"):
            if pin == user["pin"]:
                if amt > user["balance"]:
                    st.error("Insufficient balance")
                else:
                    user["balance"] -= amt
                    st.success("Withdraw successful")
            else:
                st.error("Wrong PIN")