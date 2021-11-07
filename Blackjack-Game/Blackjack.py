import random
import pygame

pygame.init()

screenWidth = 800
screenHeight = 650
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Blackjack')
font = pygame.font.SysFont('Constantia', 20)
margin = 70

# Game variables
winningScore = 21
playerTotal = 0
hitCardsList = []
onSwitch = 0  # DIRECTLY CONTROLS IF THE HIT BUTTON WILL DISPLAY THE NEW CARD
gameOver = False
xPos = 30

background = (3, 160, 98)
white = (255, 255, 255)

oneCards = {
    1: "card-images/ace_of_clubs.png", 2: "card-images/ace_of_diamonds.png", 3: "card-images/ace_of_hearts.png",
    4: "card-images/ace_of_spades.png"}
twoCards = {
    1: "card-images/2_of_clubs.png", 2: "card-images/2_of_diamonds.png", 3: "card-images/2_of_hearts.png",
    4: "card-images/2_of_spades.png"}
threeCards = {
    1: "card-images/3_of_clubs.png", 2: "card-images/3_of_diamonds.png", 3: "card-images/3_of_hearts.png",
    4: "card-images/3_of_spades.png"}
fourCards = {
    1: "card-images/4_of_clubs.png", 2: "card-images/4_of_diamonds.png", 3: "card-images/4_of_hearts.png",
    4: "card-images/4_of_spades.png"}
fiveCards = {
    1: "card-images/5_of_clubs.png", 2: "card-images/5_of_diamonds.png", 3: "card-images/5_of_hearts.png",
    4: "card-images/5_of_spades.png"}
sixCards = {
    1: "card-images/6_of_clubs.png", 2: "card-images/6_of_diamonds.png", 3: "card-images/6_of_hearts.png",
    4: "card-images/6_of_spades.png"}
sevenCards = {
    1: "card-images/7_of_clubs.png", 2: "card-images/7_of_diamonds.png", 3: "card-images/7_of_hearts.png",
    4: "card-images/7_of_spades.png"}
eightCards = {
    1: "card-images/8_of_clubs.png", 2: "card-images/8_of_diamonds.png", 3: "card-images/8_of_hearts.png",
    4: "card-images/8_of_spades.png"}
nineCards = {
    1: "card-images/9_of_clubs.png", 2: "card-images/9_of_diamonds.png", 3: "card-images/9_of_hearts.png",
    4: "card-images/9_of_spades.png"}
tenCards = {
    1: "card-images/10_of_clubs.png", 2: "card-images/10_of_diamonds.png", 3: "card-images/10_of_hearts.png",
    4: "card-images/10_of_spades.png"}
tenJackCards = {
    1: "card-images/jack_of_clubs2.png", 2: "card-images/jack_of_diamonds2.png", 3: "card-images/jack_of_hearts2.png",
    4: "card-images/jack_of_spades2.png"}
tenQueenCards = {
    1: "card-images/queen_of_clubs2.png", 2: "card-images/queen_of_diamonds2.png",
    3: "card-images/queen_of_hearts2.png",
    4: "card-images/queen_of_spades2.png"}
tenKingCards = {
    1: "card-images/king_of_clubs2.png", 2: "card-images/king_of_diamonds2.png", 3: "card-images/king_of_hearts2.png",
    4: "card-images/king_of_spades2.png"}
elevenCards = {
    1: "card-images/ace_of_clubs.png", 2: "card-images/ace_of_diamonds.png", 3: "card-images/ace_of_hearts.png",
    4: "card-images/ace_of_spades.png"}


class Card:
    def __init__(self, x, y, image, scale, value):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.value = value

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True

                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


def getRandomValue():  # Returns a random int used to pick a dictionary
    randomValue = random.randint(1, 14)  # because there are fourteen dictionaries (1,10 + face cards and 11/ace)
    return randomValue


def getCardDictionary(randomValue):
    if randomValue == 1:
        dictionaryName = oneCards
        return dictionaryName
    elif randomValue == 2:
        dictionaryName = twoCards
        return dictionaryName
    elif randomValue == 3:
        dictionaryName = threeCards
        return dictionaryName
    elif randomValue == 4:
        dictionaryName = fourCards
        return dictionaryName
    elif randomValue == 5:
        dictionaryName = fiveCards
        return dictionaryName
    elif randomValue == 6:
        dictionaryName = sixCards
        return dictionaryName
    elif randomValue == 7:
        dictionaryName = sevenCards
        return dictionaryName
    elif randomValue == 8:
        dictionaryName = eightCards
        return dictionaryName
    elif randomValue == 9:
        dictionaryName = nineCards
        return dictionaryName
    elif randomValue == 10:
        dictionaryName = tenCards
        return dictionaryName
    elif randomValue == 11:
        dictionaryName = tenJackCards
        return dictionaryName
    elif randomValue == 12:
        dictionaryName = tenQueenCards
        return dictionaryName
    elif randomValue == 13:
        dictionaryName = tenKingCards
        return dictionaryName
    elif randomValue == 14:
        dictionaryName = elevenCards
        return dictionaryName


def getCardValue(randomValue):
    if randomValue == 11:
        cardValue = 10
        return cardValue
    elif randomValue == 12:
        cardValue = 10
        return cardValue
    elif randomValue == 13:
        cardValue = 10
        return cardValue
    elif randomValue == 14:
        cardValue = 11
        return cardValue
    else:
        return randomValue


def getRandomCardSuite():  # returns a random number from one to four (picks a random card within the dictionary)
    cardSuite = random.randint(1, 4)
    return cardSuite


def getCardImage(cardDictionary, cardSuite):  # returns a card image
    cardImage = pygame.image.load(cardDictionary.get(cardSuite))
    return cardImage


def increaseXPos():
    global xPos
    xPos += 30
    print(f"New x: {xPos}")


def draw_board():
    screen.fill(background)
    pygame.draw.line(screen, white, (0, margin), (screenWidth, margin))


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def createCardX(xPos):
    cardXRandomValue = getRandomValue()  # Random integer to pick a random dictionary
    cardXDictionary = getCardDictionary(cardXRandomValue)
    cardXValue = getCardValue(cardXRandomValue)  # Gets real card value used to calculate player score
    cardXSuite = getRandomCardSuite()
    cardXImage = getCardImage(cardXDictionary, cardXSuite)
    increaseXPos()
    hitCardsList.append(Card(xPos, 400, cardXImage, 0.25, cardXValue))


def getPlayerTotal():
    total = 0
    for count in range(0, len(hitCardsList)):
        total += hitCardsList[count].value
    return total


# load images
hit_button_image = pygame.image.load('card-images/hit_btn.png')
stay_button_image = pygame.image.load('card-images/stay_btn.png')
reset_button_image = pygame.image.load('card-images/reset_btn.png')
quit_button_image = pygame.image.load('card-images/quit_btn.png')

hit_button = Button(300, 200, hit_button_image, 0.3)
stay_button = Button(400, 200, stay_button_image, 0.3)
reset_button = Button(300, 600, reset_button_image, 0.3)
quit_button = Button(400, 600, quit_button_image, 0.3)

createCardX(xPos)  # 1st card
createCardX(xPos)  # 2nd Card

# Main game loop
run = True

while run:

    pygame.display.flip()  # Updates display with any new drawings

    if gameOver is False:
        # Draw Background
        screen.fill(background)
        pygame.draw.line(screen, white, (0, margin), (screenWidth, margin))
        draw_text("Player total: " + str(playerTotal), font, white, 20, 15)


        for card in hitCardsList:
            card.draw()

        if hit_button.draw():
            createCardX(xPos)
            print("hi")
            playerTotal = getPlayerTotal()
            print(getPlayerTotal())

        if stay_button.draw():
            playerTotal = getPlayerTotal()
            if playerTotal != winningScore:
                draw_text("You lost :(", font, white, 22, 44)
            else:
                draw_text("You Won!", font, white, 22, 44)
            gameOver = True

        # Code for reset functionality
        if reset_button.draw():
            hitCardsList = []
            xPos = 30
            playerTotal = 0
            createCardX(xPos)
            createCardX(xPos)
            gameOver = False

        # Functionality for quitting game
        if quit_button.draw():
            pygame.quit()

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update Display window
    pygame.display.update()

pygame.quit()
