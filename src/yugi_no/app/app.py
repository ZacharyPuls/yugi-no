import pygame


class App:
    running: bool = False
    screen: pygame.Surface
    clock: pygame.Clock
    resolution: tuple[int, int]

    def __init__(self, resolution: tuple[int, int] = (1280, 720)) -> None:
        self.resolution = resolution

    def start(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.running = True
        self.event_loop()
        pygame.quit()

    def event_loop(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("green")
            pygame.display.flip()
            self.clock.tick(60)
