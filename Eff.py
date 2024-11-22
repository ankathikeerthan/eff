import streamlit as st
st.title("2305A21L02-PS9")
st.write("Calculate the Efficiency of the DC Shunt motor at various loads")

def Gen_Eff(v,cl,il,k,rsh,ra):
    ish=v/rsh
    ia=k*il-ish
    cul=ish*2*rsh+ia*2*ra
    eff=(k*v*il-cl-cul)*100/(k*v*il)
    return eff,cul
col1,col2=st.columns(2)
with col1:
        v=st.number_input("Voltage(V):", value=5)
        il=st.number_input("Full Load current(A):", value=100)
        cl=st.number_input("Core Losses(W):", value=50)
        rsh=st.number_input("Shunt resistance(OHMS):")
        ra=st.number_input("Armature Resistance(ohms):")
        k=st.number_input("Loading on generator:",value=0.5)
        compute=st.button("compute")
        with col2:
          with st.container(border=True):
            if compute:
                eff,cul=Gen_Eff(v,cl,il,k,rsh,ra)
                st.write(f"Efficiency of Generator={eff:.2f} %")
                st.write(f"Copper losses of Generator={cul:.2f} Watts")