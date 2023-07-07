import streamlit as st
import random


# 問題のリスト
questions = [
    {
        "description": "問題1: Googleスプレッドシートでセルをコピーするショートカットキーは何ですか？",
        "choices": ["1. Ctrl + X", "2. Ctrl + V", "3. Ctrl + C"],
        "solution": "3. Ctrl + C",
        "explanation": " Ctrl + Cを押すことで、選択したセルをコピーできます。"
    },
    {
        "description": "問題2: Googleスプレッドシートでセルを貼り付けるショートカットキーは何ですか？",
        "choices": ["1. Ctrl + V", "2. Ctrl + C", "3. Ctrl + X"],
        "solution": "1. Ctrl + V",
        "explanation": " Ctrl + Vを押すことで、選択したセルにコピーした内容を貼り付けられます。"},
    {
        "description": "問題3: Googleスプレッドシートでセルを切り取るショートカットキーは何ですか？",
        "choices": ["1. Ctrl + X", "2. Ctrl + C", "3. Ctrl + V"],
        "solution": "1. Ctrl + X",
        "explanation": " Ctrl + Xを押すことで、選択したセルを切り取ることができます。"},
    {
        "description": "問題4: Googleスプレッドシートで元に戻すショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Y", "2. Ctrl + Z", "3. Ctrl + R"],
        "solution": "2. Ctrl + Z",
        "explanation": " Ctrl + Zを押すことで、直前の操作を元に戻すことができます。"},
    {
        "description": "問題5: Googleスプレッドシートでやり直しのショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Y", "2. Ctrl + Z", "3. Ctrl + R"],
        "solution": "1. Ctrl + Y",
        "explanation": " Ctrl + Yを押すことで、元に戻した操作をやり直すことができます。"},
    {
        "description": "問題6: Googleスプレッドシートで全てのセルを選択するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + D", "2. Ctrl + S", "3. Ctrl + A"],
        "solution": "3. Ctrl + A",
        "explanation": " Ctrl + Aを押すことで、シート内の全てのセルを選択できます。"},
    {
        "description": "問題7: Googleスプレッドシートで検索を開始するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + H", "2. Ctrl + G", "3. Ctrl + F"],
        "solution": "3. Ctrl + F",
        "explanation": " Ctrl + Fを押すことで、検索ウィンドウが開き、キーワードの検索ができます。"},
    {
        "description": "問題8: Googleスプレッドシートで選択したセルの書式をクリアするショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Shift + Y", "2. Ctrl + Shift + Z", "3. Ctrl + Shift + X"],
        "solution": "2. Ctrl + Shift + Z",
        "explanation": " Ctrl + Shift + Zを押すことで、選択したセルの書式をクリアできます。"},
    {
        "description": "問題9: Googleスプレッドシートで選択したセルを結合するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + M", "2. Ctrl + N", "3. Ctrl + O"],
        "solution": "1. Ctrl + M",
        "explanation": " Ctrl + Mを押すことで、選択したセルを結合できます。"},
    {
        "description": "問題10: Googleスプレッドシートで選択したセルの値をフィルタするショートカットキーは何ですか？",
        "choices": ["1. Ctrl + hSift + F", "2. Ctrl + Shift + L", "3. Ctrl + Shift + S"],
        "solution": "2. Ctrl + Shift + L",
        "explanation": " Ctrl + Shift + Lを押すことで、選択したセルの値に基づいてフィルタを適用できます。"},
    {
        "description": "問題11: Googleスプレッドシートで選択したセルの書式をコピーするショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Alt + C", "2. Ctrl + Shift + C", "3. Ctrl + Alt + V"],
        "solution": "2. Ctrl + Shift + C",
        "explanation": "Ctrl + Shift + Cを押すことで、選択したセルの書式をコピーできます。"},
    {
        "description": "問題12: Googleスプレッドシートで選択したセルに書式を貼り付けるショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Shift + V", "2. Ctrl + Alt + V", "3. Ctrl + Alt + C"],
        "solution": "1. Ctrl + Shift + V",
        "explanation": " Ctrl + Shift + Vを押すことで、選択したセルに書式を貼り付けられます。"},
    {
        "description": "問題13: Googleスプレッドシートで現在のシートの名前を変更するショートカットキーは何ですか？",
        "choices": ["1. Alt + Shift + N", "2. Alt + Shift + S", "3. Alt + Shift + R"],
        "solution": "3. Alt + Shift + R",
        "explanation": " Alt + Shift + Rを押すことで、現在のシートの名前を変更できます。"},
    {
        "description": "問題14: Googleスプレッドシートで新しいシートを追加するショートカットキーは何ですか？",
        "choices": ["1. Shift + F11", "2. Ctrl + Shift + N", "3. Alt + Shift + S"],
        "solution": "1. Shift + F11",
        "explanation": " Shift + F11を押すことで、新しいシートを追加できます。"},
    {
        "description": "問題15: Googleスプレッドシートで行を挿入するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Alt + I", "2. Ctrl + Alt + R", "3. Ctrl + Alt + L"],
        "solution": "2. Ctrl + Alt + R",
        "explanation": " Ctrl + Alt + Rを押すことで、選択したセルの上に新しい行を挿入できます。"},
    {
        "description": "問題16: Googleスプレッドシートで列を挿入するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Alt + I", "2. Ctrl + Alt + L", "3. Ctrl + Alt + C"],
        "solution": "3. Ctrl + Alt + C",
        "explanation": " Ctrl + Alt + Cを押すことで、選択したセルの左に新しい列を挿入できます。"},
    {
        "description": "問題17: Googleスプレッドシートで行を削除するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Alt + E", "2. Ctrl + Alt + R", "3. Ctrl + Alt + D"],
        "solution": "3. Ctrl + Alt + D",
        "explanation": " Ctrl + Alt + Dを押すことで、選択した行を削除できます。"},
    {
        "description": "問題18: Googleスプレッドシートで列を削除するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Alt + E", "2. Ctrl + Alt + D", "3. Ctrl + Alt + C"],
        "solution": "1. Ctrl + Alt + E",
        "explanation": " Ctrl + Alt + Eを押すことで、選択した列を削除できます。"},
    {
        "description": "問題19: Googleスプレッドシートで選択したセルを編集するショートカットキーは何ですか？",
        "choices": ["1. F4", "2. F3", "3. F2"],
        "solution": "3. F2",
        "explanation": " F2を押すことで、選択したセルを編集モードに変更できます。"},
    {
        "description": "問題20:  Googleスプレッドシートで選択したセルの値を右のセルからコピーするショートカットキーは何ですか？",
        "choices": ["1. Ctrl + R", "2. Ctrl + L", "3. Ctrl + ;"],
        "solution": "1. Ctrl + R",
        "explanation": " Ctrl + Rを押すことで、選択したセルの値を右のセルからコピーできます。"},
    {
        "description": "問題21:  Googleスプレッドシートで選択したセルの値を左のセルからコピーするショートカットキーは何ですか？",
        "choices": ["1. Ctrl + L", "2. Ctrl + '", "3. 3. Ctrl + R"],
        "solution": "2. Ctrl + '",
        "explanation": " Ctrl + ' を押すことで、選択したセルの値を左のセルからコピーできます。"},
    {
        "description": "問題22:  Googleスプレッドシートで現在の日付を挿入するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + ;", "2. Ctrl + '", "3. Ctrl + ,"],
        "solution": "1. Ctrl + ;",
        "explanation": "Ctrl + ; を押すことで、選択したセルに現在の日付を挿入できます。"},
    {
        "description": "問題23:  Googleスプレッドシートで現在の時刻を挿入するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Shift + ;", "2. Ctrl + Shift + '", "3. Ctrl + Shift + ,"],
        "solution": "1. Ctrl + Shift + ;",
        "explanation": "  Ctrl + Shift + ; を押すことで、選択したセルに現在の時刻を挿入できます。"},
    {
        "description": "問題24:  Googleスプレッドシートで選択したセルを1つ上に移動するショートカットキーは何ですか？",
        "choices": ["1. Shift + 上矢印", "2. Alt + 上矢印", "3. Ctrl + 上矢印"],
        "solution": "3. Ctrl + 上矢印",
        "explanation": " Ctrl + 上矢印を押すことで、選択したセルを1つ上に移動できます。"},
    {
        "description": "問題25:  Googleスプレッドシートで選択したセルを一気に上に移動するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Shift + 上矢印", "2. Alt + 上矢印", "3. Ctrl + 上矢印"],
        "solution": "1. Ctrl + Shift + 上矢印",
        "explanation": " Ctrl + Shift + 上矢印を押すことで、選択したセルを一気に上に移動できます。"},
    {
        "description": "問題26:  Googleスプレッドシートで選択したセルにコメントを追加するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Alt + Shift + C", "2. Ctrl + Alt + Shift + M", "3. Ctrl + Alt + Shift + V"],
        "solution": "1. Ctrl + Alt + Shift + C",
        "explanation": " Ctrl + Alt + Shift + Mを押すことで、選択したセルにコメントを追加できます。"},
    {
        "description": "問題27:   Googleスプレッドシートで選択したセルのコメントを表示するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Alt + C", "2. Ctrl + Alt + V", "3.  Ctrl + Alt + M"],
        "solution": "3.  Ctrl + Alt + M",
        "explanation": " Ctrl + Alt + Mを押すことで、選択したセルのコメントを表示できます。"},
    {
        "description": "問題28:  Googleスプレッドシートで選択したセルの書式をパーセンテージ書式に変更するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Shift + 1", "2. Ctrl + Shift + 2", "3. Ctrl + Shift + 5"],
        "solution": "3. Ctrl + Shift + 5",
        "explanation": " Ctrl + Shift + 5を押すことで、選択したセルの書式をパーセンテージ書式に変更できます。"},
    {
        "description": "問題29:  Googleスプレッドシートで選択したセルのフォントサイズを大きくするショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Shift + >", "2. Ctrl + Shift + +", "3. Ctrl + Shift + <"],
        "solution": "1. Ctrl + Shift + >",
        "explanation": " Ctrl + Shift + > を押すことで、選択したセルのフォントサイズを大きくできます。"},
    {
        "description": "問題30:  Googleスプレッドシートで選択したセルのフォントサイズを小さくするショートカットキーは何ですか？",
        "choices": ["1.Ctrl + Shift + - + 上矢印", "2. Ctrl + Shift + <", "3. Ctrl + Shift + >"],
        "solution": "2. Ctrl + Shift + <",
        "explanation": " Ctrl + Shift + < を押すことで、選択したセルのフォントサイズを小さくできます。"}
]

def get_next_question(index):
    return questions[index % len(questions)]
if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.results = []
if not st.session_state.started:
    st.title("スプレッドシート 初級30本ノック Windows版")
    if st.button("Start"):
        st.session_state.started = True
        st.experimental_rerun()
    st.write("スプレッドシートで手を動かしながらやってみてね！")
else:
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
    if "correct_answers" not in st.session_state:
        st.session_state.correct_answers = 0
    if "total_answers" not in st.session_state:
        st.session_state.total_answers = 0
    if "answered" not in st.session_state:
        st.session_state.answered = False
    if "show_correct_answer" not in st.session_state:
        st.session_state.show_correct_answer = False
    if st.session_state.question_index >= len(questions):
        st.header("結果画面")

        # ランク表示
        accuracy = st.session_state.correct_answers / len(questions)
        rank = ""
        if accuracy == 1:
            rank = "プレデター"
            rank_color = "maroon"
        elif 0.8 <= accuracy < 1:
            rank = "マスター"
            rank_color = "indigo"
        elif 0.6 <= accuracy < 0.8:
            rank = "ダイア"
            rank_color = "navy"
        elif 0.4 <= accuracy < 0.6:
            rank = "プラチナ"
            rank_color = "turquoise"
        elif 0.2 <= accuracy < 0.4:
            rank = "ゴールド"
            rank_color = "goldenrod"
        elif 0.1 <= accuracy < 0.2:
            rank = "シルバー"
            rank_color = "silver"
        elif 0.01 <= accuracy < 0.1:
            rank = "ブロンズ"
            rank_color = "brown"
        else:
            rank = "ルーキー"
            rank_color = "saddlebrown"
        st.markdown(f"あなたのランクは...<span style='color: {rank_color}; font-weight: bold;'>{rank}</span>", unsafe_allow_html=True)
 
        # 正解・不正解の一覧
        st.write("正解・不正解の一覧:")
        col1, col2 = st.columns(2)
        col1.write("問題")
        col2.write("結果")
        for result in st.session_state.results:
            col1.write(result["question"])
            if result["is_correct"]:
                col2.markdown("<span style='color: blue;'>&#x25CB;</span>", unsafe_allow_html=True)
            else:
                col2.markdown("<span style='color: red;'>&#x2715;</span>", unsafe_allow_html=True)
    else:
        progress = st.session_state.question_index / len(questions)
        st.progress(progress)
        st.write(f"問題 {st.session_state.question_index + 1} / {len(questions)}")
        selected_question = get_next_question(st.session_state.question_index)
        st.text(selected_question["description"])
        user_solution = st.radio("選択肢:", selected_question["choices"])
        correct_choice_index = selected_question["choices"].index(selected_question["solution"])

        if not st.session_state.answered:
            if st.button("解答"):
                st.session_state.total_answers += 1
                if user_solution == selected_question["choices"][correct_choice_index]:
                    st.success("正解です！")
                    st.session_state.correct_answers += 1
                    st.session_state.show_correct_answer = False
                else:
                    st.error("不正解です。")
                    st.session_state.show_correct_answer = True
                st.session_state.answered = True
                result = {
                    "question": selected_question["description"],
                    "user_solution": user_solution,
                    "correct_solution": selected_question["choices"][correct_choice_index],
                    "is_correct": user_solution == selected_question["choices"][correct_choice_index],
                    "explanation": selected_question["explanation"]
                }
                st.session_state.results.append(result)
        if st.session_state.show_correct_answer:
            st.write("正解: " + selected_question["choices"][correct_choice_index])
            st.write("解説: " + selected_question["explanation"])
        if st.session_state.answered:
            if st.button("次へ"):
                st.session_state.question_index += 1
                st.session_state.show_correct_answer = False
                st.session_state.answered = False
                st.experimental_rerun()