# Tic Tac Toe extins
## Descriere generala
Proiectul acesta este un joc de Tic Tac Toe (sau X si 0) singleplayer care este jucat impotriva unui AI realizat pe baza unui algoritm minimax. Regulile jocului sunt simple, jucatrul uman si AI-ul aleg pe rand pozitii pe un grid de dimensiuni variabile, patrat, de forma N x N. Scopul pentru a castiga este inlantuirea a N elemente consecutive pe rand, coloana sau diagonala. Prmul care indeplineste cel putin una dintre conditii castiga. Limitarea este faptul ca tot timpul jucatorul uman o sa inceapa, si prin deducere. Interfata jocului este grafica realizata cu modulul tkinter si consta intr-o matrice de butoane care odata apasate iau simbolul jucatorului curent. 
## Explicatie algoritmi
Principalul algoritm utilizat este minimax, responsabil de mutarile AI-ului. Pe langa acesta sunt utilizate o combinatie de clase si metode pentru a realiza jocul. In 'game_logic.py'