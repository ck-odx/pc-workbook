import streamlit as st


# 問題のリスト
questions = [
    {
        "description": "問題1: キーボードにあるctrlキーの名称は？",
        "solution": "コントロールキー",
        "explanation": "ctrlキーは、他のキーと組み合わせて使用されることが多いです。\n\n例1:ctrl+c:コピー\n\n例2:ctrl+v:貼り付け(ペースト)"
    },
    {
        "description": "問題2: キーボードにあるshiftキーの名称は？",
        "solution": "シフトキー",
        "explanation": "shiftキーは、他のキーと組み合わせて使用されることが多いです。\n\n例1:shift+矢印:複数選択 \n\n例2:shift+ctrl+v:値貼り付け(書式を変えずに貼り付け)"
    },
    {
        "description": "問題3: キーボードにあるaltキーの名称は？",
        "solution": "オルトキー",
        "explanation": "altキーは、他のキーと組み合わせて使用されることが多いです。\n\n例:alt+tab:開いてるアプリ切り替え"
    },
    {
        "description": "問題4: キーボードにある一番長いキーの名称は？",
        "solution": "スペースキー",
        "explanation": "spaceキーは、空白を入れる際に使用します"
    },
    {
        "description": "問題5: キーボードにあるF1〜F12キーの名称は？",
        "solution": "ファンクションキー",
        "explanation": "fnキーは、特殊なキーが設置されてるので（F1:ヘルプキー）使用方法は自分で調べてみてね"
    },
    {
        "description": "問題6: キーボードにある決定や改行などを行うキーの名称は？",
        "solution": "エンターキー",
        "explanation": "enterキーは、決定や改行をする際に使用します"
    },
    {
        "description": "問題7: キーボードにあるtobキーの名称は？",
        "solution": "タブキー",
        "explanation": "tabキーは、他のキーと組み合わせて使用されることが多いです。\n\n例1:alt+shift+tab:ウィンドウ移動(左) \n\n例2:alt+tab:ウィンドウ移動(右)"
    },
    {
        "description": "問題8: キーボードにあるescキーの名称は？",
        "solution": "エスケープキー",
        "explanation": "escキーは、処理を中止したり取り消したりする機能を持っている"
    },
    {
        "description": "問題9: マウスを2回クリックすることを何と言いますか？",
        "solution": "ダブルクリック",
        "explanation": "ブラウザでWEBに入る時やスプレッドシート内でも多用するので必ず覚えておきましょう"
    },
    {
        "description": "問題10: キーを複数押して便利な機能が使えるキーのことを何と言うでしょうか？",
        "solution": "ショートカットキー",
        "explanation": "上記の解説で紹介した例がショートカットキーです。"
    },
    {
        "description": "問題11: Googleから提供されてる表計算ソフトの名称は？",
        "solution": "スプレッドシート",
        "explanation": "文字の生成&数字の計算など使用頻度とても高いので覚えておいてね"
    },
    {
        "description": "問題12: Microsoftから提供されてる表計算ソフトの名称は？",
        "solution": "エクセル",
        "explanation": "文字の生成&数字の計算など使用頻度とても高いので覚えておいてね"
    },
    {
        "description": "問題13: スプレッドシートとエクセルの違いはインターネットを通してるかどうかです。文字をリアルタイムで他の人に共有できるのはどっち？",
        "solution": "スプレッドシート",
        "explanation": "スプシは便利だけど、デメリットは複数人が一つのシートを使用したりするので作業が被ったりする危険性がある！"
    },
    {
        "description": "問題14: Goggleにおいて保存したいブラウザを保管する方法を何と言う（右上の⭐マーク）？",
        "solution": "ブックマーク",
        "explanation": "ブックマークフォルダなども作成できるので、学習用や勤務系やメイン業務などフォルダ分けがおすすめです"
    },
    {
        "description": "問題15: Goggleにおいて『https〜』から始まる文字のことを何という？",
        "solution": "URL",
        "explanation": "URLをコピーして貼り付けする作業も多いので覚えておきましょう"
    },
    {
        "description": "問題16: Goggleにおいて共有したい写真や動画やシートを保管するサービスを何といいますか？",
        "solution": "Goggle drive",
        "explanation": "チーム内で触ってるシートなどはドライブに基本あるのでシートを見失ったらドライブ！"
    },
    {
        "description": "問題17: スプレッドシートとエクセルにある文字を記入できる部分のことをなんと言う？",
        "solution": "セル",
        "explanation": "セルはスプシとエクセルの共通用語なので覚えておきましょう"
    },
    {
        "description": "問題18: １と1の文字の違いは何でしょうか？",
        "solution": "全角半角",
        "explanation": "日付など記入する際、全角半角で判定が変わってエラーになる場合もあります"
    },
    {
        "description": "問題19: スプレッドシートにて、シートが複数ある場合に下部に出現するものを何といいますか？",
        "solution": "シートタブ",
        "explanation": "ブラウザタブとシートタブがあるので気をつけましょう"
    },
    {
        "description": "問題20: マウスを上下左右に動かすとPC上の矢印も動くと思います。その挙動を何と言いますか？",
        "solution": "スクロール",
        "explanation": "業務説明でこの単語をよく聞くと思いますので覚えておいてね"
    }
]

def get_next_question(index):
    return questions[index % len(questions)]

st.title("PC問題 初級 20 本ノック for Windows")

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
        st.info(f"解説: {selected_question['explanation']}")

if st.button("次へ"):
    st.session_state.question_index += 1
    st.session_state.show_correct_answer = False
    st.experimental_rerun()