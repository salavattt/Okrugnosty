import pygame
import sys
import os


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.pos = (pos_x, pos_y)


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


pygame.init()

size = WIDTH, HEIGHT = 550, 550
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Перемещение героя')
STEP = 50
FPS = 50
player = None

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mar.png', -1)

tile_width = tile_height = 50
clock = pygame.time.Clock()
start_screen()
urov = input('Введите название уровня ')

player, level_x, level_y = generate_level(load_level(urov))
level_map = load_level(urov)

# camera = Camera()
# camera.update(player)
# обновляем положение всех спрайтов
# with open('data/urov2.txt', 'r') as mapFile:
    #  = [line.strip() for line in mapFile]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if level_map[player.pos[0]][player.pos[1] + 1] == '.' or level_map[player.pos[0]][player.pos[1] + 1] == '@':
                player.rect.y += STEP
                player.pos = (player.pos[0], player.pos[1] + 1)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if level_map[player.pos[0]][player.pos[1] - 1] == '.' or level_map[player.pos[0]][player.pos[1] - 1] == '@':
                player.rect.y -= STEP
                player.pos = (player.pos[0], player.pos[1] - 1)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if level_map[player.pos[0] - 1][player.pos[1]] == '.' or level_map[player.pos[0] - 1][player.pos[1]] == '@':
                player.rect.x -= STEP
                player.pos = (player.pos[0] - 1, player.pos[1])
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if level_map[player.pos[0] + 1][player.pos[1]] == '.' or level_map[player.pos[0] + 1][player.pos[1]] == '@':
                player.rect.x += STEP
                player.pos = (player.pos[0] + 1, player.pos[1])

    # camera.update(player)
    # обновляем положение всех спрайтов
    # for sprite in all_sprites:
    #     camera.apply(sprite)

    screen.fill(pygame.Color("black"))
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()

pygame.quit()
