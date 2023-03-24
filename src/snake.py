from direction import Direction
from part import Part


class Snake:

    def __init__(self, height, width):
        # When start game snake spawn moving to right
        self.direction = Direction.RIGHT.value
        self.speed = 20
        # Cabeça da cobra
        self.head = Part(240, 200)
        # Partes do corpo da cobra
        self.parts = [self.head, Part(220, 200), Part(200, 200)]
        # Ultima posição da cobra
        self.last = self.head
        # Tamanho da tela
        self.height = height
        self.width = width

    def move(self, direction):
        # Verifica se a cobra não está indo na direção oposta
        if (direction == Direction.RIGHT.value and self.direction != Direction.LEFT.value or
                direction == Direction.LEFT.value and self.direction != Direction.RIGHT.value or
                direction == Direction.UP.value and self.direction != Direction.DOWN.value or
                direction == Direction.DOWN.value and self.direction != Direction.UP.value):
            self.direction = direction

    def add(self, part):
        self.parts.append(part)

    def remove(self, part):
        if part in self.parts:
            self.parts.remove(part)

    def update(self):
        # Salva a posição atual da cabeça da cobra
        last_pos = (self.head.x, self.head.y)
        # Move a cabeça da cobra na direção atual
        if self.direction == Direction.RIGHT.value:
            self.head.x += self.speed
        if self.direction == Direction.LEFT.value:
            self.head.x -= self.speed
        if self.direction == Direction.UP.value:
            self.head.y -= self.speed
        if self.direction == Direction.DOWN.value:
            self.head.y += self.speed

        # Verifica se a cobra passou da borda e faz ela aparecer do outro lado
        if self.head.x < 0:
            self.head.x = self.width - self.speed
        if self.head.x >= self.width:
            self.head.x = 0
        if self.head.y < 0:
            self.head.y = self.height - self.speed
        if self.head.y >= self.height:
            self.head.y = 0

        self.parts[0] = self.head

        # Move o resto do corpo da cobra para a posição anterior
        for index in range(1, len(self.parts)):
            part = self.parts[index]
            # Salva a posição atual da parte do corpo
            part_pos = (part.x, part.y)
            # Atualiza a posição da parte do corpo com base na posição anterior
            part.x, part.y = last_pos
            # Atualiza a posição anterior com a posição atual da parte do corpo
            last_pos = part_pos
            self.parts[index] = part

    def show(self, screen, pygame):
        # Desenha a cobra na tela
        for part in self.parts:
            pygame.draw.rect(screen, (0, 128, 0), (part.x, part.y, 20, 20))

    def is_collision(self):
        # Verifica se a cabeça da cobra colidiu com alguma parte do corpo
        for part in self.parts[1:]:
            if self.head.x == part.x and self.head.y == part.y:
                return True
        return False
