import streamlit as st


# 問題のリスト
questions = [
    {
        "description": "問題1: セルをコピーするショートカットキーは何ですか？",
        "solution": "ctrl+c"
    },
    {
        "description": "問題2: セルを貼り付けるショートカットキーは何ですか？",
        "solution": "ctrl+v"
    },
    {
        "description": "問題3: セル内で改行するショートカットキーは何ですか？",
        "solution": "alt+enter"
    },
    {
        "description": "問題4: セルの値を置換するショートカットキーは何ですか？",
        "solution": " ctrl+h"
    },
    {
        "description": "問題5: セルを絶対参照に切り替えるショートカットキーは何ですか？",
        "solution": "f4"
    },
    {
        "description": "問題6: セルのフィルタをオン/オフにするショートカットキーは何ですか？",
        "solution": "ctrl+shift+l"
    },
    {
        "description": "問題7: 現在の時間を表示するショートカットキーは何ですか？",
        "solution": "ctrl+shift+;"
    },
    {
        "description": "問題8: シートを新規作成するショートカットキーは何ですか？",
        "solution": "ctrl+n"
    },
    {
        "description": "問題9: セルの値をクリアするショートカットキーは何ですか？",
        "solution": "delete"
    },
    {
        "description": "問題10: シート間を移動するショートカットキーは何ですか？",
        "solution": "ctrl+pgUp/pgDn"
    },
    {
        "description": "問題11: シートを元に戻すショートカットキーは何ですか？",
        "solution": "ctrl+z"
    },
    {
        "description": "問題12: 現在のセルの左側に新しい列を挿入するショートカットキーは何ですか？",
        "solution": "ctrl+shift++"
    },
    {
        "description": "問題13: 現在のセルの上側に新しい行を挿入するショートカットキーは何ですか？",
        "solution": "ctrl+shift++"
    },
    {
        "description": "問題14: 選択したセルの行を削除するショートカットキーは何ですか？",
        "solution": "ctrl+-"
    },
    {
        "description": "問題15: 選択したセルの列を削除するショートカットキーは何ですか？",
        "solution": "ctrl+-"
    },
    {
        "description": "問題16: シート全体を選択するショートカットキーは何ですか？",
        "solution": "ctrl+a"
    },
    {
        "description": "問題17: シートの先頭に移動するショートカットキーは何ですか？",
        "solution": "ctrl+home"
    },
    {
        "description": "問題18: シートの最後に移動するショートカットキーは何ですか？",
        "solution": "ctrl+end"
    },
    {
        "description": "問題19: 複数のセルを選択したい時に使うショートカットキーは何ですか？",
        "solution": "shift+↑→↓←"
    },
    {
        "description": "問題20: 複数のセルを一気に選択したい時に使うショートカットキーは何ですか？",
        "solution": "ctrl+shift+↑→↓←"
    }
]

def get_next_question(index):
    return questions[index % len(questions)]

st.title("スプレッドシート問題 20本ノック 中級 for Windows")

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

selected_question = get_next_question(st.session_state.question_index)
st.text(selected_question["description"])
user_solution = st.text_input("解答式を入力してください:")

if "show_correct_answer" not in st.session_state:
    st.session_state.show_correct_answer = False

if st.button("解答"):
    if user_solution.strip().upper() == selected_question["solution"].strip().upper():
        st.success("正解です！")
        st.session_state.show_correct_answer = False
    else:
        st.error("不正解です。")
        st.session_state.show_correct_answer = True

if st.session_state.show_correct_answer:
    if st.button("正しい解答を見る"):
        st.success(f"正しい解答は {selected_question['solution']} です。")

if st.button("次へ"):
    st.session_state.question_index += 1
    st.session_state.show_correct_answer = False
    st.experimental_rerun()