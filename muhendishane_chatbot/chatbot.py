import streamlit as st
import model_file

st.header("🤖 Mühendishane Chatbot")

# Başlangıç mesajı
with st.chat_message(name="assistant"):
  st.write("Merhaba, Size nasıl yardımcı olabilirim?")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Önceki mesajları ekrana yazdırır
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcının girdiği soru
soru = st.chat_input("Haydi sor sor...")

# Kullanıcı soru girdiyse
if soru:
    # Kullanıcının mesajını ekrana yazdır
    with st.chat_message("user"):
        st.markdown(soru)

    # Kullanıcının mesajını session_state'e kaydet
    st.session_state.messages.append({"role": "user", "content": soru})

    # st.session_state.messages içinde depolanan geçmiş mesajları birleştiriyoruz
    chat_history = "\n".join(
        [f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages]
    )

    # Modelden cevabı al
    response = model_file.give_response(chat_history, soru)

    # Cevabı ekrana yazdır
    with st.chat_message("assistant"):
        st.markdown(response)

    # Cevabı session_state'e kaydet
    st.session_state.messages.append({"role": "assistant", "content": response})