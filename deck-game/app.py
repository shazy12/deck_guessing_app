import os
import time
import pygame
import voice_recog
from fetch_data import fetch_unique_id, update_data

test_var = 0
print(test_var)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SCREEN_SHIFT_X = 200
SCREEN_SHIFT_Y = 100
deck_answers = []
FINAL_ANSWER = 0
uid = fetch_unique_id()  # always taking uid as 0 therefore not updating db therefore changed
status = ""
Group_Count = 4
j = 0  ### j is the row counter
k = 0  ### k is the row loop counter
deck1 = []  ### List of odd numbers upto 63
deck1.append([])

for i in range(1, 64):
    if i % 2 > 0:
        deck1[j].append(i)
        k += 1
        if k == Group_Count and i != 63:
            deck1.append([])
            k = 0
            j += 1

print(deck1)

j = 8  ### j is the row increment
deck2 = []  ### List of odd numbers upto 63
deck2.append([2, 3, 6, 7])
for i in range(0, 8):
    if i > 0:
        deck2.append([deck2[i - 1][0] + j, deck2[i - 1][1] + j, deck2[i - 1][2] + j, deck2[i - 1][3] + j])

print(deck2)

j = 8  ### j is the row increment
deck3 = []  ### List of odd numbers upto 63
deck3.append([4, 5, 6, 7])
for i in range(0, 8):
    if i > 0:
        deck3.append([deck3[i - 1][0] + j, deck3[i - 1][1] + j, deck3[i - 1][2] + j, deck3[i - 1][3] + j])

print(deck3)

j = 4  ### j is the row increment
k = 12  ### k is another row increment
deck4 = []  ### List of odd numbers upto 63
deck4.append([8, 9, 10, 11])
for i in range(0, 8):
    if i > 0:
        if not (i % 2 == 0):
            deck4.append([deck4[i - 1][0] + j, deck4[i - 1][1] + j, deck4[i - 1][2] + j, deck4[i - 1][3] + j])
        else:
            deck4.append([deck4[i - 1][0] + k, deck4[i - 1][1] + k, deck4[i - 1][2] + k, deck4[i - 1][3] + k])

print(deck4)

j = 4  ### j is the row increment
k = 20  ### k is another row increment
deck5 = []  ### List of odd numbers upto 63
deck5.append([16, 17, 18, 19])
for i in range(0, 8):
    if i > 0:
        if not (i % 4 == 0):
            deck5.append([deck5[i - 1][0] + j, deck5[i - 1][1] + j, deck5[i - 1][2] + j, deck5[i - 1][3] + j])
        else:
            deck5.append([deck5[i - 1][0] + k, deck5[i - 1][1] + k, deck5[i - 1][2] + k, deck5[i - 1][3] + k])

print(deck5)

j = 4  ### j is the row increment
deck6 = []  ### List of odd numbers upto 63
deck6.append([32, 33, 34, 35])
for i in range(0, 8):
    if i > 0:
        deck6.append([deck6[i - 1][0] + j, deck6[i - 1][1] + j, deck6[i - 1][2] + j, deck6[i - 1][3] + j])

print(deck6)

formula_list = [1, 2, 4, 8, 16, 32]


class Pane(object):

    def __init__(self, title_text, title_font, title_font_size):
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # You have to call this before pygame.init()
        pygame.init()
        info = pygame.display.Info()  # You have to call this before pygame.display.set_mode()
        screen_width, screen_height = info.current_w, info.current_h
        window_width, window_height = screen_width - 200, screen_height - 100
        self.font = pygame.font.SysFont(title_font, title_font_size)
        pygame.display.set_caption(title_text)
        self.screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
        self.screen.fill((0, 0, 0))

        pygame.display.update()

    def __dinit__(self):
        pygame.quit()

    def __del__(self):
        self.__dinit__()

    def addRect(self, rect_location):
        self.rect = pygame.draw.rect(self.screen, (255, 255, 255), rect_location)
        pygame.display.update()

    def addText(self, text, text_color, text_location):
        self.screen.blit(self.font.render(text, True, text_color), text_location)
        pygame.display.update()


def wait_for_answer():
    while True:
        voice_response = voice_recog.prompt_response()
        print('voice response in wait for answer : ', voice_response)
        if 'yes' in voice_response:
            return 'yes'
        elif 'no' in voice_response:
            return 'no'
        elif 'escape' in voice_response:
            return 'escape'
        elif 'thank you' in voice_response:
            return 'thank you'
        elif 'finish' in voice_response:
            return 'finish'
        elif 'rerun' in voice_response:
            return 'rerun'
        elif 'next guess' in voice_response:
            return 'next guess'
        else:
            return "Try, Once again saying"


def show_score_grid(pane):
    score_grid_margin = 5
    score_grid_width = 100
    score_grid_height = 50
    score_grid_text_horz_margin = 35
    score_grid_text_vert_margin = 10
    score_vertical_position = 620

    row2 = ['Response', '', '', '', '', '', '']
    for index_of_deck_answers in range(0, len(deck_answers)):
        row2[index_of_deck_answers + 1] = deck_answers[index_of_deck_answers]
    grid = [['Deck', 1, 2, 3, 4, 5, 6], row2]
    print(grid)
    for row in range(2):
        for column in range(7):
            if column == 0:
                pane.addRect([(score_grid_margin + score_grid_width) * column + score_grid_margin + SCREEN_SHIFT_X,
                              (score_grid_margin + score_grid_height) * row + score_vertical_position
                              + score_grid_margin + SCREEN_SHIFT_Y,
                              score_grid_width, score_grid_height])
                pane.addText(str(grid[row][column]), BLACK,
                             ((
                                      score_grid_margin + score_grid_width) * column + score_grid_text_horz_margin // 3 + SCREEN_SHIFT_X,
                              (score_grid_margin + score_grid_height) * row + score_vertical_position +
                              score_grid_text_vert_margin + SCREEN_SHIFT_Y))
            else:
                pane.addRect([(score_grid_margin + score_grid_width) * column + score_grid_margin + SCREEN_SHIFT_X,
                              (score_grid_margin + score_grid_height) * row + score_vertical_position +
                              score_grid_margin + SCREEN_SHIFT_Y,
                              score_grid_width, score_grid_height])
                pane.addText(str(grid[row][column]), BLACK,
                             ((
                                      score_grid_margin + score_grid_width) * column + score_grid_text_horz_margin + SCREEN_SHIFT_X,
                              (score_grid_margin + score_grid_height) * row + score_vertical_position +
                              score_grid_text_vert_margin + SCREEN_SHIFT_Y))


def deck_draw(grid, title, is_final_deck):
    # Define some colors
    global FINAL_ANSWER, uid, status

    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 200
    HEIGHT = 50
    WINDOW_SIZE = [850, 900]
    # This sets the margin between each cell
    MARGIN = 5
    TEXT_HORZ_MARGIN = 90
    TEXT_VERT_MARGIN = 15
    # Initialize pygame
    grid_text_vertical_position_start = 50
    pane1 = Pane(title, 'Arial', 25)

    # -------- Main Program Loop -----------
    done = False
    number_of_tries = 0
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        # Draw Header
        pane1.addText(title, RED, (2 + SCREEN_SHIFT_X, 10 + SCREEN_SHIFT_Y))
        # Draw Footer
        if not is_final_deck:
            question_text = "Please Say 'Yes' if Your Number is in the Deck Shown or Say 'No'"
            pane1.addText(question_text, GREEN, (2 + SCREEN_SHIFT_X, 470 +
                                                 grid_text_vertical_position_start + SCREEN_SHIFT_Y))
        if not is_final_deck:
            # Draw the grid
            for row in range(8):
                for column in range(4):
                    pane1.addRect([(MARGIN + WIDTH) * column + MARGIN + SCREEN_SHIFT_X,
                                   (
                                           MARGIN + HEIGHT) * row + grid_text_vertical_position_start + MARGIN + SCREEN_SHIFT_Y,
                                   WIDTH, HEIGHT])
                    pane1.addText(str(grid[row][column]), GREEN,
                                  ((MARGIN + WIDTH) * column + TEXT_HORZ_MARGIN + SCREEN_SHIFT_X,
                                   (
                                           MARGIN + HEIGHT) * row + grid_text_vertical_position_start + TEXT_VERT_MARGIN + SCREEN_SHIFT_Y))
        # pygame.draw.rect(screen,
        #                  color,
        #                  [(MARGIN + WIDTH) * column + MARGIN,
        #                   (MARGIN + HEIGHT) * row + MARGIN,
        #                   WIDTH,
        #                   HEIGHT])

        show_score_grid(pane1)

        if is_final_deck:
            for i in range(0, len(deck_answers)):
                FINAL_ANSWER = formula_list[i] * deck_answers[i] + FINAL_ANSWER

            # to call save final answer to db
            status = "Final Answer"
            update_data(uid, status, FINAL_ANSWER)
            last_answer = FINAL_ANSWER
            # display_answer(FINAL_ANSWER)
            pane2 = Pane(title, 'Verdana', 144 * 4)
            pane2.addRect([0, 0, 1000, 1000])
            pane2.addText(str(FINAL_ANSWER), RED, (100, 50))
            print("Final Answer\t", FINAL_ANSWER)
            time.sleep(10)

        answer = wait_for_answer()

        if is_final_deck:
            if 'thank you' in answer or 'finish in answer':
                return False
            elif 'rerun' in answer or 'next guess':
                return True
            else:
                return True

        if not is_final_deck:

            print('answer: ', answer)
            if 'yes' in answer:
                ans = 1
                done = True
            elif 'no' in answer:
                ans = 0
                done = True
            elif 'escape' in answer:
                pane1.__del__()
                return False
            else:
                ans = -1
                number_of_tries += 1
                question_text = 'Please try saying Yes or No again, Number of voice tries count :- ' + str(
                    number_of_tries)
                pane1.addText(question_text, GREEN,
                              (2 + SCREEN_SHIFT_X, 520 + grid_text_vertical_position_start + SCREEN_SHIFT_Y))
                question_text = "Please Say 'Yes' if Your Number is in the Deck Shown or Say 'No'"
                pane1.addText(question_text, GREEN,
                              (2 + SCREEN_SHIFT_X, 570 + grid_text_vertical_position_start + SCREEN_SHIFT_Y))

            if ans in [0, 1]:
                deck_answers.append(ans)
                show_score_grid(pane1)
                return True
        print("final", FINAL_ANSWER)
        return FINAL_ANSWER


def ask_init_question():
    pane_init = Pane('', 'Verdana', 25)
    pane_init.addRect((0, 0, 2000, 2000))
    pane_init.addText('IBM Think BOOTH IDEA# 2', (0, 0, 0), (0, 50))
    txt = []
    # uid=fetch_unique_id()
    txt.append("Your PIN number for ipad application is : " + str(uid))
    txt.append("Guess a number in your memory between 1 and 50,")
    txt.append("Once you have thought, say 'Start' ")

    def _ask_question(txt):
        Init_X = 200
        Init_Y = 100
        Increment_in_Y = 50

        for i in range(0, len(txt)):
            if (i + 1) % 2 == 0:
                pane_init.addText(txt[i], (0, 255, 0), (Init_X, i * Increment_in_Y + Init_Y))
            else:
                pane_init.addText(txt[i], (0, 255, 255), (Init_X, i * Increment_in_Y + Init_Y))

    _ask_question(txt=txt)
    number_of_tries = 0
    while True:
        voice_response = voice_recog.prompt_response()
        print(voice_response)

        if 'start' in voice_response:
            txt.clear
            txt.append("Showing Deck 1 ....")
            _ask_question(txt=txt)
            time.sleep(3)
            pane_init.__del__()
            return True
        elif 'escape' in voice_response or 'skip' in voice_response:
            txt.clear
            txt.append("Quiting The APP :) Have a nice day....")
            _ask_question(txt=txt)
            time.sleep(3)
            pane_init.__del__()
            return False
        elif 'rerun' in voice_response or 'next guess' in voice_response:
            txt.clear
            txt.append("Restarting The APP :) please wait....")
            _ask_question(txt=txt)
            time.sleep(3)
            pane_init.__del__()
            return True
        else:
            number_of_tries += 1
            txt.append("Try  Once again saying 'Start', Number of voice tries: " + str(number_of_tries))
            _ask_question(txt=txt)


if __name__ == '__main__':
    run_app = True
    while run_app:
        if ask_init_question():
            if deck_draw(deck1, 'IBM Think BOOTH IDEA# 2 - Deck 1', False):
                if deck_draw(deck2, 'IBM Think BOOTH IDEA# 2 - Deck 2', False):
                    if deck_draw(deck3, 'IBM Think BOOTH IDEA# 2 - Deck 3', False):
                        if deck_draw(deck4, 'IBM Think BOOTH IDEA# 2 - Deck 4', False):
                            if deck_draw(deck5, 'IBM Think BOOTH IDEA# 2 - Deck 5', False):
                                if deck_draw(deck6, 'IBM Think BOOTH IDEA# 2 - Deck 6', False):
                                    if not deck_draw(formula_list, 'IBM Think BOOTH IDEA# 2 - Result ', True):
                                        run_app = False
        else:
            run_app = False

    # update db and stop running and answer = 0
    # update_data(uid, status, FINAL_ANSWER)
    print(deck_answers)