import streamlit as st
import time
from game import TicTacToe


    
st.set_page_config(page_title="TicTacToe Game", layout="centered")
st.title("🎮Tic Tac Toe - You vs AI")
difficulty = st.selectbox(label="Choose A Level :" , options=["Hard" , "Medium" , "Easy"] , index=2)

if "game" not in st.session_state :
    st.session_state.game = TicTacToe(difficulty=difficulty)
    st.session_state.gameover = False
    st.session_state.winner = None
    st.session_state.ai_turn = False
    
if "score" not in st.session_state :
    st.session_state.score = {"Human" : 0 , "AI" : 0 ,"Draw" :0}

game = st.session_state.game

st.write(f"🏆 Score -> You : {st.session_state.score["Human"]} , AI : {st.session_state.score["AI"]} , Draw : {st.session_state.score["Draw"]}")


if st.session_state.ai_turn and not st.session_state.gameover :
    with st.spinner("🤖 AI is thinking") :
        time.sleep(0.5)
    move = game.ai_move()
    game.fix_spot(move , game.ai)
    if game.has_player_won(game.ai):
        st.session_state.score["AI"] += 1
        st.session_state.winner = "AI"
        st.session_state.gameover = True
    elif game.is_board_filled() :
        st.session_state.score["Draw"] += 1
        st.session_state.winner = "Draw"
        st.session_state.gameover = True

    st.session_state.ai_turn = False
    st.rerun()
    
if st.session_state.gameover :
    if st.session_state.winner == "Human" :
        st.success("🎉 You Won!")
    elif st.session_state.winner == "AI" :
        st.error("🫠 AI Won!")
    elif st.session_state.winner == "Draw" :
        st.info("😊 It's a Draw")

for row in range(3) :
    cols = st.columns(3)
    for col in range(3) :
        index = row * 3 + col + 1
        cell_value = game.board[index]
        button_label = cell_value if cell_value != " " else "⬜"
        is_disabled = (cell_value != " ") or st.session_state.gameover or st.session_state.ai_turn
        if cols[col].button(label=button_label , key=f"cell_{index}" , disabled = is_disabled) :
            game.fix_spot(index , game.human)
            if game.has_player_won(game.human):
              st.session_state.score["Human"] += 1
              st.session_state.winner = "Human"
              st.session_state.gameover = True
              st.rerun()
            elif game.is_board_filled() :
               st.session_state.score["Draw"] += 1
               st.session_state.winner = "Draw"
               st.session_state.gameover = True
               st.rerun()

            else :
              st.session_state.ai_turn = True
              st.rerun()

        
if st.button("🔄 Restart Game"):
    st.session_state.game = TicTacToe(difficulty=difficulty)  
    st.session_state.gameover = False
    st.session_state.winner = None
    st.session_state.ai_turn = False
    st.rerun()