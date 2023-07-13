import streamlit as st
import pandas as pd 

# 常時ワイドモード
st.set_page_config(layout="wide")

# 問題のリスト
questions = [
    {
        "description": "問題1：Googleスプレッドシートでセルをコピーするショートカットキーは何ですか？",
        "choices": ["1. Ctrl + X", "2. Ctrl + V", "3. Ctrl + C"],
        "solution": "3. Ctrl + C",
        "explanation": " Ctrl + Cを押すことで、選択したセルをコピーできます。"
    },
    {
        "description": "問題2：Googleスプレッドシートでセルを貼り付けるショートカットキーは何ですか？",
        "choices": ["1. Ctrl + V", "2. Ctrl + C", "3. Ctrl + X"],
        "solution": "1. Ctrl + V",
        "explanation": " Ctrl + Vを押すことで、選択したセルにコピーした内容を貼り付けられます。"},
    {
        "description": "問題3：Googleスプレッドシートでセルを切り取るショートカットキーは何ですか？",
        "choices": ["1. Ctrl + X", "2. Ctrl + C", "3. Ctrl + V"],
        "solution": "1. Ctrl + X",
        "explanation": " Ctrl + Xを押すことで、選択したセルを切り取ることができます。"},
    {
        "description": "問題4：Googleスプレッドシートで元に戻すショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Y", "2. Ctrl + Z", "3. Ctrl + R"],
        "solution": "2. Ctrl + Z",
        "explanation": " Ctrl + Zを押すことで、直前の操作を元に戻すことができます。"},
    {
        "description": "問題5：Googleスプレッドシートでやり直しのショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Y", "2. Ctrl + Z", "3. Ctrl + R"],
        "solution": "1. Ctrl + Y",
        "explanation": " Ctrl + Yを押すことで、元に戻した操作をやり直すことができます。"},
    {
        "description": "問題6：Googleスプレッドシートで全てのセルを選択するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + D", "2. Ctrl + S", "3. Ctrl + A"],
        "solution": "3. Ctrl + A",
        "explanation": " Ctrl + Aを押すことで、シート内の全てのセルを選択できます。"},
    {
        "description": "問題7：Googleスプレッドシートで検索を開始するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + H", "2. Ctrl + G", "3. Ctrl + F"],
        "solution": "3. Ctrl + F",
        "explanation": " Ctrl + Fを押すことで、検索ウィンドウが開き、キーワードの検索ができます。"},
    {
        "description": "問題8：Googleスプレッドシートで選択したセルの書式をクリアするショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Shift + Y", "2. Ctrl + Shift + Z", "3. Ctrl + Shift + X"],
        "solution": "2. Ctrl + Shift + Z",
        "explanation": " Ctrl + Shift + Zを押すことで、選択したセルの書式をクリアできます。"},
    {
        "description": "問題9：Googleスプレッドシートで選択したセルを結合するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + M", "2. Ctrl + N", "3. Ctrl + O"],
        "solution": "1. Ctrl + M",
        "explanation": " Ctrl + Mを押すことで、選択したセルを結合できます。"},
    {
        "description": "問題10：Googleスプレッドシートで選択したセルの値をフィルタするショートカットキーは何ですか？",
        "choices": ["1. Ctrl + hSift + F", "2. Ctrl + Shift + L", "3. Ctrl + Shift + S"],
        "solution": "2. Ctrl + Shift + L",
        "explanation": " Ctrl + Shift + Lを押すことで、選択したセルの値に基づいてフィルタを適用できます。"},
    {
        "description": "問題11：Googleスプレッドシートで選択したセルの書式をコピーするショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Alt + C", "2. Ctrl + Shift + C", "3. Ctrl + Alt + V"],
        "solution": "2. Ctrl + Shift + C",
        "explanation": "Ctrl + Shift + Cを押すことで、選択したセルの書式をコピーできます。"},
    {
        "description": "問題12：Googleスプレッドシートで選択したセルに書式を貼り付けるショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Shift + V", "2. Ctrl + Alt + V", "3. Ctrl + Alt + C"],
        "solution": "1. Ctrl + Shift + V",
        "explanation": " Ctrl + Shift + Vを押すことで、選択したセルに書式を貼り付けられます。"},
    {
        "description": "問題13：Googleスプレッドシートで現在のシートの名前を変更するショートカットキーは何ですか？",
        "choices": ["1. Alt + Shift + N", "2. Alt + Shift + S", "3. Alt + Shift + R"],
        "solution": "3. Alt + Shift + R",
        "explanation": " Alt + Shift + Rを押すことで、現在のシートの名前を変更できます。"},
    {
        "description": "問題14：Googleスプレッドシートで新しいシートを追加するショートカットキーは何ですか？",
        "choices": ["1. Shift + F11", "2. Ctrl + Shift + N", "3. Alt + Shift + S"],
        "solution": "1. Shift + F11",
        "explanation": " Shift + F11を押すことで、新しいシートを追加できます。"},
    {
        "description": "問題15：Googleスプレッドシートで行を挿入するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Alt + I", "2. Ctrl + Alt + R", "3. Ctrl + Alt + L"],
        "solution": "2. Ctrl + Alt + R",
        "explanation": " Ctrl + Alt + Rを押すことで、選択したセルの上に新しい行を挿入できます。"},
    {
        "description": "問題16：Googleスプレッドシートで列を挿入するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Alt + I", "2. Ctrl + Alt + L", "3. Ctrl + Alt + C"],
        "solution": "3. Ctrl + Alt + C",
        "explanation": " Ctrl + Alt + Cを押すことで、選択したセルの左に新しい列を挿入できます。"},
    {
        "description": "問題17：Googleスプレッドシートで行を削除するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Alt + E", "2. Ctrl + Alt + R", "3. Ctrl + Alt + D"],
        "solution": "3. Ctrl + Alt + D",
        "explanation": " Ctrl + Alt + Dを押すことで、選択した行を削除できます。"},
    {
        "description": "問題18：Googleスプレッドシートで列を削除するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Alt + E", "2. Ctrl + Alt + D", "3. Ctrl + Alt + C"],
        "solution": "1. Ctrl + Alt + E",
        "explanation": " Ctrl + Alt + Eを押すことで、選択した列を削除できます。"},
    {
        "description": "問題19：Googleスプレッドシートで選択したセルを編集するショートカットキーは何ですか？",
        "choices": ["1. F4", "2. F3", "3. F2"],
        "solution": "3. F2",
        "explanation": " F2を押すことで、選択したセルを編集モードに変更できます。"},
    {
        "description": "問題20：Googleスプレッドシートで選択したセルの値を右のセルからコピーするショートカットキーは何ですか？",
        "choices": ["1. Ctrl + R", "2. Ctrl + L", "3. Ctrl + ;"],
        "solution": "1. Ctrl + R",
        "explanation": " Ctrl + Rを押すことで、選択したセルの値を右のセルからコピーできます。"},
    {
        "description": "問題21：Googleスプレッドシートで選択したセルの値を左のセルからコピーするショートカットキーは何ですか？",
        "choices": ["1. Ctrl + L", "2. Ctrl + '", "3. 3. Ctrl + R"],
        "solution": "2. Ctrl + '",
        "explanation": " Ctrl + ' を押すことで、選択したセルの値を左のセルからコピーできます。"},
    {
        "description": "問題22：Googleスプレッドシートで現在の日付を挿入するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + ;", "2. Ctrl + '", "3. Ctrl + ,"],
        "solution": "1. Ctrl + ;",
        "explanation": "Ctrl + ; を押すことで、選択したセルに現在の日付を挿入できます。"},
    {
        "description": "問題23：Googleスプレッドシートで現在の時刻を挿入するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Shift + ;", "2. Ctrl + Shift + '", "3. Ctrl + Shift + ,"],
        "solution": "1. Ctrl + Shift + ;",
        "explanation": "  Ctrl + Shift + ; を押すことで、選択したセルに現在の時刻を挿入できます。"},
    {
        "description": "問題24：Googleスプレッドシートで選択したセルを1つ上に移動するショートカットキーは何ですか？",
        "choices": ["1. Shift + 上矢印", "2. Alt + 上矢印", "3. Ctrl + 上矢印"],
        "solution": "3. Ctrl + 上矢印",
        "explanation": " Ctrl + 上矢印を押すことで、選択したセルを1つ上に移動できます。"},
    {
        "description": "問題25：Googleスプレッドシートで選択したセルを一気に上に移動するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Shift + 上矢印", "2. Alt + 上矢印", "3. Ctrl + 上矢印"],
        "solution": "1. Ctrl + Shift + 上矢印",
        "explanation": " Ctrl + Shift + 上矢印を押すことで、選択したセルを一気に上に移動できます。"},
    {
        "description": "問題26：Googleスプレッドシートで選択したセルにコメントを追加するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Alt + Shift + C", "2. Ctrl + Alt + Shift + M", "3. Ctrl + Alt + Shift + V"],
        "solution": "1. Ctrl + Alt + Shift + C",
        "explanation": " Ctrl + Alt + Shift + Mを押すことで、選択したセルにコメントを追加できます。"},
    {
        "description": "問題27： Googleスプレッドシートで選択したセルのコメントを表示するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Alt + C", "2. Ctrl + Alt + V", "3.  Ctrl + Alt + M"],
        "solution": "3.  Ctrl + Alt + M",
        "explanation": " Ctrl + Alt + Mを押すことで、選択したセルのコメントを表示できます。"},
    {
        "description": "問題28：Googleスプレッドシートで選択したセルの書式をパーセンテージ書式に変更するショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Shift + 1", "2. Ctrl + Shift + 2", "3. Ctrl + Shift + 5"],
        "solution": "3. Ctrl + Shift + 5",
        "explanation": " Ctrl + Shift + 5を押すことで、選択したセルの書式をパーセンテージ書式に変更できます。"},
    {
        "description": "問題29：Googleスプレッドシートで選択したセルのフォントサイズを大きくするショートカットキーは何ですか？",
        "choices": ["1. Ctrl + Shift + >", "2. Ctrl + Shift + +", "3. Ctrl + Shift + <"],
        "solution": "1. Ctrl + Shift + >",
        "explanation": " Ctrl + Shift + > を押すことで、選択したセルのフォントサイズを大きくできます。"},
    {
        "description": "問題30：Googleスプレッドシートで選択したセルのフォントサイズを小さくするショートカットキーは何ですか？",
        "choices": ["1.Ctrl + Shift + - + 上矢印", "2. Ctrl + Shift + <", "3. Ctrl + Shift + >"],
        "solution": "2. Ctrl + Shift + <",
        "explanation": " Ctrl + Shift + < を押すことで、選択したセルのフォントサイズを小さくできます。"}
]

def get_next_question(index):
    """「スプレッドシート 初級30本ノック Windows版」
    """
    return questions[index % len(questions)]

def initialize_session_state():
    """「初期化する」
    """
    if "started" not in st.session_state:
        st.session_state.started = False
        st.session_state.results = []
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

def get_rank_color(accuracy):
    """「HOME画面のランクカラー」
    """
    if 1 <= accuracy:
        return "maroon"
    if 0.8 <= accuracy < 0.99:
        return "indigo"
    elif 0.6 <= accuracy < 0.8:
        return "blue"
    elif 0.4 <= accuracy < 0.6:
        return "turquoise"
    elif 0.2 <= accuracy < 0.4:
        return "goldenrod"
    elif 0.1 <= accuracy < 0.2:
        return "silver"
    elif 0.01 <= accuracy < 0.1:
        return "peru"
    elif 0 <= accuracy < 0.01:
        return "saddlebrown"
    
def display_start_screen():
    """「HOME画面」
    """
    st.title("スプレッドシート 初級30本ノック Windows版")
    st.write("スプレッドシートで手を動かしながらやってみてね！")
    if st.button("Start", key="start_button"):
        st.session_state.started = True
        st.session_state.correct_answers = 0  # 正解数を追跡する変数を追加
        st.experimental_rerun()
        
    with st.expander("説明", expanded=False):
        st.write("形式：3択問題となっております")
        st.write("解答ボタン：選択した解答に対して正解か不正解かが表示されます")
        st.write("解説ボタン：問題に対しての解説となっています")
        st.write("次へボタン：次の問題へ移動します")
        st.write("結果画面：問題の結果をまとめた画面になります正解数によってランクがつけられます")
        st.write("ランク：問題の結果をまとめた画面になります  ※ランク詳細以下参照")
    
        # ランク表を作成
        st.write("解答率 | ランク")
        st.markdown(f"0% | <span style='color: {get_rank_color(0)}; font-weight: bold;'>ルーキー</span>", unsafe_allow_html=True)
        st.markdown(f"1〜9% | <span style='color: {get_rank_color(0.01)}; font-weight: bold;'>ブロンズ</span>", unsafe_allow_html=True)
        st.markdown(f"10〜19% | <span style='color: {get_rank_color(0.1)}; font-weight: bold;'>シルバー</span>", unsafe_allow_html=True)
        st.markdown(f"20〜39% | <span style='color: {get_rank_color(0.2)}; font-weight: bold;'>ゴールド</span>", unsafe_allow_html=True)
        st.markdown(f"40〜59% | <span style='color: {get_rank_color(0.4)}; font-weight: bold;'>プラチナ</span>", unsafe_allow_html=True)
        st.markdown(f"60〜79% | <span style='color: {get_rank_color(0.6)}; font-weight: bold;'>ダイア</span>", unsafe_allow_html=True)
        st.markdown(f"80〜99% | <span style='color: {get_rank_color(0.8)}; font-weight: bold;'>マスター</span>", unsafe_allow_html=True)
        st.markdown(f"100% | <span style='color: {get_rank_color(1)}; font-weight: bold;'>プレデター</span>", unsafe_allow_html=True)

def display_question_screen():
    """「問題画面」
    """
    progress = st.session_state.question_index / len(questions)
    st.progress(progress)
    st.write(f"問題 {st.session_state.question_index + 1} / {len(questions)}")
    selected_question = get_next_question(st.session_state.question_index)
    st.text(selected_question["description"])
    user_solution = st.radio("選択肢:", selected_question["choices"])
    # フォームを作成
    with st.form(key="question_form"):
        # 解答ボタン
        answer_button = st.form_submit_button("解答")
        # 解説ボタン
        explanation_button = st.form_submit_button("解説")
        # 次へボタン
        next_button = st.form_submit_button("次へ")
    # 解答ボタンが押されたら、正解か不正解かを表示する
    if answer_button:
        is_correct = user_solution == selected_question["solution"]
        if is_correct:
            st.success("正解！")
            st.session_state.correct_answers += 1
        else:
            st.error(f"不正解... 正解は {selected_question['solution']}")
        # 解答した問題を結果に追加
        st.session_state.results.append({
            "question": selected_question["description"],  # 修正: 'question' -> 'description'
            "is_correct": is_correct
        })
        # 解答数をカウント
        st.session_state.total_answers += 1
    # 解説ボタンが押されたら、解説を表示する
    if explanation_button:
        st.info(selected_question["explanation"])
    # 次へボタンが押されたら、次の問題に移動する
    if next_button:
        st.session_state.question_index += 1
        st.experimental_rerun()

def display_result_screen():
    """「結果画面」
    """
    st.header("結果画面")
    st.write(f"正解数: {st.session_state.correct_answers} / {len(questions)}")
    
    if st.session_state.total_answers < 20:
        st.markdown("**問題の解答数が足りてないのでランクをつけれません**")
        if st.button("初めから", key="restart_button"):
            st.session_state.question_index = 0
            st.session_state.correct_answers = 0
            st.session_state.total_answers = 0
            st.session_state.results = []
            st.session_state.started = False
            st.experimental_rerun()
    else:
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
            rank_color = "blue"
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
            rank_color = "peru"
        else:
            rank = "ルーキー"
            rank_color = "saddlebrown"
        st.markdown(f"あなたのランクは...**<span style='color: {rank_color}; font-weight: bold;'>{rank}</span>**", unsafe_allow_html=True)
    
        # 正解・不正解の一覧
        st.write("正解・不正解の一覧:")
        results_table = pd.DataFrame(st.session_state.results)
        results_table["結果"] = results_table["is_correct"].apply(lambda x: "<span style='color: blue;'>○</span>" if x else "<span style='color: red;'>×</span>")
        results_table = results_table.rename(columns={"question": "問題"})
        results_table = results_table[["問題", "結果"]]
        st.write("""
        <style>
        table {
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: lightgrey;
        }
        </style>
        """, unsafe_allow_html=True)
        st.write(results_table.to_html(index=False, escape=False, table_id="results_table"), unsafe_allow_html=True)

        # 「初めから」のボタンを追加
        if st.button("初めから", key="restart_2_button"):
            st.session_state.question_index = 0
            st.session_state.correct_answers = 0
            st.session_state.total_answers = 0
            st.session_state.results = []
            st.session_state.started = False
            st.experimental_rerun()

# 実行処理
if __name__ == "__main__":
    if "started" not in st.session_state:
        st.session_state.started = False
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
    if "total_answers" not in st.session_state:
        st.session_state.total_answers = 0
    if "correct_answers" not in st.session_state:
        st.session_state.correct_answers = 0
    if "results" not in st.session_state:
        st.session_state.results = []
    if not st.session_state.started:
        display_start_screen()
    elif st.session_state.question_index < len(questions):
        display_question_screen()
    else:
        display_result_screen()