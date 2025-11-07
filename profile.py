import streamlit as st

st.header('ABOUT INFO')

col1, col2 = st.columns(2)

with (col1):
    st.subheader('👤Tarek amin arik')
    st.image('https://scontent-bom5-1.xx.fbcdn.net/v/t1.15752-9/577110451_827647506755756_538703046407658389_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=0024fc&_nc_ohc=z57WWoi9Ey8Q7kNvwG6JBjc&_nc_oc=AdmR5GIA5YrMgjIlWj1jN7fCZxfVyngQZ-wRxgu7T5VREZQoGlBxsOAny-TGOpc91qOoq3zrL3H9_Ar_YHlYeVcu&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bom5-1.xx&oh=03_Q7cD3wGcDSaR7gzJOZzugeoN6e2E7mgU4V85_JDhqrk8qN9J_w&oe=69342F51',width=200)
    st.text('-arik')
with col2:
    st.text('Yooohh 👋😄\nI’m Arik 🌙✨ (AKA nothing… cuz I’m mysterious like that 👀)\nI made this lil web app so you can know me a tiny bit 💗\nFor now, my socials are here 📱💬\nMore cool stuff coming soon… maybe 😌💫\n🎉🎂10 oct ')
    s1 = '📸instagram'
    s2 = '📘facebook'
    s3 = '📞whatsapp'
    s4 = '✈️telegram'
    x = st.selectbox('my social media accounts', ('🖲️click👇', s1, s2, s3, s4))
    if s1:
        if x == s1:
            st.markdown("[📸instagram:tarek amin arik](https://www.instagram.com/mr.arik7/?hl=en)")
    if s2:
        if x == s2:
            st.text('currently i dont have an FB account:)')
    if s3:
        if x == s3:
            st.markdown('[📞whatsapp:01327329596(arik)](https://wa.me/01327329596)')
    if s4:
        if x == s4:
            st.markdown('[✈️telegram:tarek amin arik](http://t.me/mr_arik7)')











