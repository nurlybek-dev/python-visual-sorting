import random

import pygame
import pygame_gui

from pygame_gui.elements import UIHorizontalSlider
from pygame_gui.elements import UIDropDownMenu
from pygame_gui.elements import UIButton
from pygame_gui.elements import UILabel

import sorting


class Options:
    def __init__(self):
        self.resolution = (800, 600)


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Text Game')
        self.options = Options()
        self.window_surface = pygame.display.set_mode(self.options.resolution)

        self.background_surface = None
        self.ui_manager = pygame_gui.UIManager(self.options.resolution)

        self.algorithm_label = None
        self.algorithm_drop_down_menu = None
        self.array_size_label = None
        self.array_size_drop_down_menu = None
        self.shuffle_button = None
        self.generate_button = None
        self.play_speed_label = None
        self.play_speed_slider = None
        self.play_button = None

        self.recreate_ui()

        self.clock = pygame.time.Clock()
        self.is_running = True
        self.is_play = False

        self.strategy = None
        self.array = [0] * 50
        self.bar_width = 0

    def recreate_ui(self):
        self.ui_manager.set_window_resolution(self.options.resolution)
        self.ui_manager.clear_and_reset()

        self.background_surface = pygame.Surface(self.options.resolution)
        self.background_surface.fill((33, 40, 45))

        self.algorithm_label = UILabel(pygame.Rect(525, 65, 100, 25),
                                       'Algorithm:',
                                       self.ui_manager)

        self.algorithm_drop_down_menu = UIDropDownMenu(['Bubble sort',
                                                        'Insertion sort',
                                                        'Merge sort',
                                                        'Selection sort',
                                                        'Quicksort'],
                                                       'Bubble sort',
                                                       pygame.Rect((620, 65), (150, 25)),
                                                       self.ui_manager)

        self.array_size_label = UILabel(pygame.Rect(525, 100, 100, 25),
                                        'Array size:',
                                        self.ui_manager)

        self.array_size_drop_down_menu = UIDropDownMenu(['10',
                                                         '50',
                                                         '100',
                                                         '200'],
                                                        '50',
                                                        pygame.Rect((620, 100), (150, 25)),
                                                        self.ui_manager)

        self.generate_button = UIButton(relative_rect=pygame.Rect((620, 135), (150, 25)),
                                        text='Generate',
                                        manager=self.ui_manager)

        self.shuffle_button = UIButton(relative_rect=pygame.Rect((620, 170), (150, 25)),
                                       text='Shuffle',
                                       manager=self.ui_manager)

        self.play_speed_label = UILabel(pygame.Rect(525, 240, 100, 25),
                                        'Play speed:',
                                        self.ui_manager)

        self.play_speed_slider = UIHorizontalSlider(pygame.Rect((620, 240), (150, 25)),
                                                    50.0,
                                                    (0.0, 100.0),
                                                    self.ui_manager)

        self.play_button = UIButton(relative_rect=pygame.Rect((620, 275), (150, 25)),
                                    text='Play',
                                    manager=self.ui_manager)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.generate_button:
                        self.generate()
                    if event.ui_element == self.shuffle_button:
                        self.shuffle()
                    if event.ui_element == self.play_button:
                        self.play()

            self.ui_manager.process_events(event)

    def generate(self):
        size = self.array_size_drop_down_menu.selected_option
        self.array.clear()
        for _ in range(int(size)):
            length = random.randint(50, 450)
            self.array.append(length)

    def shuffle(self):
        random.shuffle(self.array)

    def play(self):
        self.is_play = True
        self.change_strategy()
        self.strategy.sort(self.array)
        self.is_play = False

    def change_strategy(self):
        algorithm = self.algorithm_drop_down_menu.selected_option
        if algorithm == 'Bubble sort':
            self.strategy = sorting.BubbleSort(self)
        elif algorithm == 'Insertion sort':
            self.strategy = sorting.InsertionSort(self)
        elif algorithm == 'Merge sort':
            self.strategy = sorting.MergeSort(self)
        elif algorithm == 'Selection sort':
            self.strategy = sorting.SelectionSort(self)
        elif algorithm == 'Quicksort':
            self.strategy = sorting.QuickSort(self)

    def draw(self):
        element_width = (500 - len(self.array)) // len(self.array)
        boundary_array = 500 / len(self.array)

        for index, element in enumerate(self.array):
            pygame.draw.line(self.window_surface, (0, 204, 102),
                             (boundary_array * index + 20, 600),
                             (boundary_array * index + 20, 600 - element),
                             element_width)

    def loop(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.process_events()

        self.ui_manager.update(time_delta)

        self.window_surface.blit(self.background_surface, (0, 0))
        self.ui_manager.draw_ui(self.window_surface)

        self.draw()

        pygame.display.update()

        if self.is_play:
            play_speed = 100 - self.play_speed_slider.get_current_value()
            pygame.time.delay(int(play_speed))

    def run(self):
        while self.is_running:
            self.loop()


if __name__ == '__main__':
    app = App()
    app.run()
