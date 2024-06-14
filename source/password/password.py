import sys, pygame

STATUS_OK = 0
STATUS_CANCEL = 1
STATUS_TOO_MANY_ATTEMPTS = 2


class Password():
    def __init__(self, correct_pass, max_attempts, ok_callback, cancel_callback):
        pygame.init()

        self.max_attepts = max_attempts
        self.attempts_failed = 0

        self.ok_callback = ok_callback
        self.cancel_callback = cancel_callback
        self.result_status = 0
        self.correct_pass = correct_pass

        self.font = pygame.font.SysFont("Arial", 30, True)

        self.screen = pygame.display.get_surface()
        self.window_rect = pygame.Rect(0, 0, 400, 300)
        self.window_rect.center = self.screen.get_rect().center

        self.prompt_cache = None
        self.answer_cache = None

        self.answer = ""

        self.show_error = False
        self.error_text = ""
        self.error_timer_event_code = pygame.event.custom_type()
        self.error_timer_processor = None

    def draw(self):
        pygame.draw.rect(self.screen, [14, 61, 52], self.window_rect, 0, 20)
        self.prompt_cache = self._draw_text("Введите пароль", self.font, [255, 255, 255], self.screen,
                                            [self.window_rect.centerx, self.window_rect.y + self.window_rect.h * 0.3],
                                            self.prompt_cache)

        if self.show_error:
            self._draw_text(self.error_text, self.font, [114, 36, 33], self.screen,
                            [self.window_rect.centerx,
                             self.window_rect.y + self.window_rect.h * 0.6])
        else:
            self.answer_cache = self._draw_text(self.answer, self.font, [255, 255, 255], self.screen,
                                                [self.window_rect.centerx,
                                                 self.window_rect.y + self.window_rect.h * 0.6], self.answer_cache)

    def controller(self, events, process_close=False):
        for e in events:
            if e.type == pygame.QUIT and process_close:
                pygame.quit()
                sys.exit(0)

            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                self._cancel(STATUS_CANCEL)
                continue

            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN and not self.show_error:
                self.check_answer()
                continue

            if e.type == pygame.KEYDOWN and not self.show_error:
                if e.key == pygame.K_BACKSPACE:
                    self.answer = self.answer[:-1]
                    self.answer_cache = None
                else:
                    self.answer += e.unicode
                    self.answer_cache = None

            if e.type == self.error_timer_event_code:
                self.error_timer_processor()

    def _draw_text(self, text, font: pygame.font.Font, color, surface: pygame.Surface, center, cache=None):
        if type(cache) is pygame.Surface:
            textobj = cache
        else:
            textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.center = center
        surface.blit(textobj, textrect)
        return textobj

    def _cancel(self, status):
        self.result_status = status
        if callable(self.cancel_callback):
            self.cancel_callback(status)

    def _ok(self, status):
        self.result_status = status
        if callable(self.ok_callback):
            self.ok_callback()

    def check_answer(self):
        if self.answer != self.correct_pass:
            self.attempts_failed += 1
            self._show_error("НЕПРАВИЛЬНЫЙ ПАРОЛЬ", 2000, self._incorrect_warning_timer)
        else:
            self._ok(STATUS_OK)

    def _show_error(self, text, delay, timer_processor):
        self.show_error = True
        self.error_text = text
        self.error_timer_processor = timer_processor
        pygame.time.set_timer(self.error_timer_event_code, delay, 1)

    def _remove_error(self):
        self.show_error = False

    def _incorrect_warning_timer(self):
        if self.attempts_failed < self.max_attepts:
            self._remove_error()
            self.answer = ""
            self.answer_cache = None
        else:
            self._show_error("СЛИШКОМ МНОГО ПОПЫТОК", 3000, self._too_many_attempts_timer)

    def _too_many_attempts_timer(self):
        self._cancel(STATUS_TOO_MANY_ATTEMPTS)
