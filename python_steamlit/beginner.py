import streamlit as st


# 問題のリスト
questions = [
    {
        "description": "問題1: キーボードにあるctrlキーの名称は？ ※カタカナでお答えください",
        "solution": "コントロールキー",
        "explanation": "ctrlキーは、他のキーと組み合わせて使用されることが多いです。\n\n例1: ctrl+c:コピー\n\n例2: ctrl+v:貼り付け(ペースト)"
    },
    {
        "description": "問題2: キーボードにあるshiftキーの名称は？ ※カタカナでお答えください",
        "solution": "シフトキー",
        "explanation": "shiftキーは、他のキーと組み合わせて使用されることが多いです。\n\n例1: shift+矢印:複数選択 \n\n例2: shift+ctrl+v:値貼り付け(書式を変えずに貼り付け)"
    },
    {
        "description": "問題3: キーボードにあるaltキーの名称は？ ※カタカナでお答えください",
        "solution": "オルトキー",
        "explanation": "altキーは、他のキーと組み合わせて使用されることが多いです。\n\n例: alt+tab:開いてるアプリ切り替え"
    },
    {
        "description": "問題4: キーボードにある一番長いキーの名称は？ ※カタカナでお答えください",
        "solution": "スペースキー",
        "explanation": "spaceキーは、空白を入れる際に使用します"
    },
    {
        "description": "問題5: キーボードにあるF1〜F12キーの名称は？ ※カタカナでお答えください",
        "solution": "ファンクションキー",
        "explanation": "fnキーは、特殊なキーが設置されてるので（F1:ヘルプキー）使用方法は自分で調べてみてね"
    },
    {
        "description": "問題6: キーボードにある決定や改行などを行うキーの名称は？ ※カタカナでお答えください",
        "solution": "エンターキー",
        "explanation": "enterキーは、決定や改行をする際に使用します"
    },
    {
        "description": "問題7: キーボードにあるtobキーの名称は？ ※カタカナでお答えください",
        "solution": "タブキー",
        "explanation": "tabキーは、他のキーと組み合わせて使用されることが多いです。\n\n例1: alt+shift+tab:ウィンドウ移動(左) \n\n例2: alt+tab:ウィンドウ移動(右)"
    },
    {
        "description": "問題8: キーボードにあるescキーの名称は？ ※カタカナでお答えください",
        "solution": "エスケープキー",
        "explanation": "escキーは、処理を中止したり取り消したりする機能を持っている"
    },
    {
        "description": "問題9: マウスを2回クリックすることを何と言いますか？ ※カタカナでお答えください",
        "solution": "ダブルクリック",
        "explanation": "ブラウザでWEBに入る時やスプレッドシート内でも多用するので必ず覚えておきましょう"
    },
    {
        "description": "問題10: キーを複数押して便利な機能が使えるキーのことを何と言うでしょうか？ ※カタカナでお答えください",
        "solution": "ショートカットキー",
        "explanation": "上記の解説で紹介した例がショートカットキーです。"
    },
    {
        "description": "問題11: Googleから提供されてる表計算ソフトの名称は？ ※カタカナでお答えください",
        "solution": "スプレッドシート",
        "explanation": "文字の生成&数字の計算など使用頻度とても高いので覚えておいてね"
    },
    {
        "description": "問題12: Microsoftから提供されてる表計算ソフトの名称は？ ※カタカナでお答えください",
        "solution": "エクセル",
        "explanation": "文字の生成&数字の計算など使用頻度とても高いので覚えておいてね"
    },
    {
        "description": "問題13: スプレッドシートとエクセルの違いはインターネットを通してるかどうかです。文字をリアルタイムで他の人に共有できるのはどっち？ ※カタカナでお答えください",
        "solution": "スプレッドシート",
        "explanation": "スプシは便利だけど、デメリットは複数人が一つのシートを使用したりするので作業が被ったりする危険性がある！"
    },
    {
        "description": "問題14: Goggleにおいて保存したいブラウザを保管する方法を何と言う（右上の⭐マーク）？ ※カタカナでお答えください",
        "solution": "ブックマーク",
        "explanation": "ブックマークフォルダなども作成できるので、学習用や勤務系やメイン業務などフォルダ分けがおすすめです"
    },
    {
        "description": "問題15: Goggleにおいて『https〜』から始まる文字のことを何という？ ※アルファベットでお答えください",
        "solution": "URL",
        "explanation": "URLをコピーして貼り付けする作業も多いので覚えておきましょう"
    },
    {
        "description": "問題16: Goggleにおいて共有したい写真や動画やシートを保管するサービスを何といいますか？ ※アルファベットでお答えください",
        "solution": "Goggle drive",
        "explanation": "チーム内で触ってるシートなどはドライブに基本あるのでシートを見失ったらドライブ！"
    },
    {
        "description": "問題17: スプレッドシートとエクセルにある文字を記入できる部分のことをなんと言う？ ※カタカナでお答えください",
        "solution": "セル",
        "explanation": "セルはスプシとエクセルの共通用語なので覚えておきましょう"
    },
    {
        "description": "問題18: １と1の文字の違いは何でしょうか？ ※漢字でお答えください",
        "solution": "全角半角",
        "explanation": "日付など記入する際、全角半角で判定が変わってエラーになる場合もあります"
    },
    {
        "description": "問題19: スプレッドシートにて、シートが複数ある場合に下部に出現するものを何といいますか？ ※カタカナでお答えください",
        "solution": "シートタブ",
        "explanation": "ブラウザタブとシートタブがあるので気をつけましょう"
    },
    {
        "description": "問題20: マウスを上下左右に動かすとPC上の矢印も動くと思います。その挙動を何と言いますか？ ※カタカナでお答えください",
        "solution": "スクロール",
        "explanation": "業務説明でこの単語をよく聞くと思いますので覚えておいてね"
    }
]

def get_next_question(index):
    return questions[index % len(questions)]

st.title("PC問題 初級 20 本ノック for Windows")

if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    if st.button("Start"):
        st.session_state.started = True

else:
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
    if "correct_answers" not in st.session_state:
        st.session_state.correct_answers = 0
    if "total_answers" not in st.session_state:
        st.session_state.total_answers = 0
    selected_question = get_next_question(st.session_state.question_index)
    st.text(selected_question["description"])
    user_solution = st.text_input("解答式を入力してください:")
    if "show_correct_answer" not in st.session_state:
        st.session_state.show_correct_answer = False
    if st.button("解答"):
        st.session_state.total_answers += 1
        if user_solution.strip().upper() == selected_question["solution"].strip().upper():
            st.success("正解です！")
            st.session_state.correct_answers += 1
            st.session_state.show_correct_answer = False
        else:
            st.error("不正解です。")
            st.session_state.show_correct_answer = True
    # 問題の進捗表示
    st.write(f"問題の進捗: {st.session_state.question_index + 1} / {len(questions)}")
    question_progress = (st.session_state.question_index + 1) / len(questions)
    st.progress(question_progress)
    # 正解率の表示
    st.write(f"解答数: {st.session_state.total_answers}")
    st.write(f"正解数: {st.session_state.correct_answers}")
    if st.session_state.total_answers > 0:
        accuracy = st.session_state.correct_answers / st.session_state.total_answers
        st.write(f"正解率: {accuracy * 100:.2f}%")
        st.progress(accuracy)
        if st.session_state.question_index + 1 == len(questions):
            st.write("全ての問題が終わりました！")
            rank = ""
            if accuracy == 1:
                rank = "プレデター"
                rank_color = "red"
            elif 0.8 <= accuracy < 1:
                rank = "マスター"
                rank_color = "purple"
            elif 0.6 <= accuracy < 0.8:
                rank = "ダイア"
                rank_color = "gold"
            elif 0.4 <= accuracy < 0.6:
                rank = "プラチナ"
                rank_color = "silver"
            elif 0.2 <= accuracy < 0.4:
                rank = "ゴールド"
                rank_color = "yellow"
            elif 0.1 <= accuracy < 0.2:
                rank = "シルバー"
                rank_color = "gray"
            elif 0.01 <= accuracy < 0.1:
                rank = "ブロンズ"
                rank_color = "brown"
            else:
                rank = "ルーキー"
                rank_color = "saddlebrown"
            st.markdown(f"あなたのランクは...<span style='color: {rank_color}; font-weight: bold;'>{rank}</span>", unsafe_allow_html=True)

    if st.session_state.question_index + 1 < len(questions):
        if st.button("次へ"):
            st.session_state.question_index += 1
            st.session_state.show_correct_answer = False
            st.experimental_rerun()