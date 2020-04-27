
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
        p.surrender()
        return 0
                    
