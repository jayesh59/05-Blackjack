
import cv2

def function_sequence(obj):
    if k == 27:
        break

    elif k == ord('1'):
        break

    elif k == ord('2'):
        if obj == p:
            gameplay_layout(p_turn = 1)
        else:
            gameplay_layout(p2_turn = 1)

    elif k == ord('3'):
        if obj.dd == 0:
            print('You cannot opt for this yet')
            function_sequence(obj)

        if obj == p:
            gameplay_layout(p_dd = 1)
        
        elif obj == p2:
            gameplay_layout(p2_dd = 1)

    elif k == ord('4'):
        print('Please Just Do Not')
        function_sequence(obj)

    elif k == ord('5'):
        obj.surrender()
        return 0
                    
def winning_condition():
    global game_round

    if p.win == 0 and p2.win == 0:
        return 1

    if p.surrender == 1 or p2.surrender == 1:
        return 1
    
    if p.win == 1 or p2.win == 1:
        return 1

    if bj_p == 1 and bj_p2 == 1 and bj_d == 1:
        game_round += 1
        print('It was a Tie, Begin again...')
        start(p)
        displaying_gameplay_window()

