from cmu_graphics import *
import math
import random

def onAppStart(app):
    reset(app)

def reset(app):
    app.width = 1000
    app.height = 800
    app.headX = app.width / 2
    app.headY = app.height / 2
    app.snake = [(app.headX, app.headY)]
    app.snakeLength = 50
    app.defaultSpeed = 4
    app.boostedSpeed = 6
    app.speed = app.defaultSpeed
    app.segmentSpacing = 10
    app.gamePaused = False
    app.gameOver = False
    app.cursor = None
    app.snakeFatness = 10
    app.accelerating = False
    app.cameraOffsetX = 0
    app.cameraOffsetY = 0
    app.circlePositions = []
    app.collectedCircles = []
    app.blueCircleRadius = 8
    generateMap(app)

def generateMap(app):
    # app.map = [
    #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #     [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    #     [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    #     [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #     [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    #     [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    #     [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    #     [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    #     [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    #     [1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    #     [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
    #     [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    #     [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # ]
    
    app.map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    
    app.rows = len(app.map)
    app.cols = len(app.map[0])  
 
def redrawAll(app):
    # drawMap(app)
    drawOval(app.width/2, app.height/2, app.width * 2, app.height * 2, fill = "black",
             border = "red")
    # Draw the snake
    for segment in app.snake:
        x, y = segment
        drawOval(x - app.cameraOffsetX, y - app.cameraOffsetY,
                app.snakeFatness, app.snakeFatness, fill = "red",
                border = "black")
    for x, y in app.circlePositions:
        drawCircle(x - app.cameraOffsetX, y - app.cameraOffsetY,
                   app.snakeFatness // 2, fill = "blue", border = "black")

def drawMap(app):
    # Calculate cell size
    cellWidth = app.width / app.cols
    cellHeight = app.height / app.rows

    # Draw each cell based on the map (1 = wall, 0 = space)
    for row in range(app.rows):
        for col in range(app.cols):
            color = "purple" if app.map[row][col] == 1 else "pink"
            drawRect(col * cellWidth - app.cameraOffsetX,
                    row * cellHeight - app.cameraOffsetY, cellWidth,
                    cellHeight, fill=color, border=color)

def checkCollision(app):
    newCirclePositions = []
    for circleX, circleY in app.circlePositions:
        headX, headY = app.snake[0]
        distance = ((headX - circleX)**2 + (headY - circleY)**2)**0.5
        if distance <= app.snakeFatness / 2:
            app.snakeLength += 0.1
            app.snakeFatness += 0.1
            app.collectedCircles.append((circleX, circleY))
        else:
            newCirclePositions.append((circleX, circleY))
    app.circlePositions = newCirclePositions

def checkCollisionWithLand(app):
    headX, headY = app.snake[0]
    # Check if the snake's head is outside the large oval
    if not (app.width / 2 - (app.width - 100) / 2 < headX < app.width / 2 + (app.width - 100) / 2 and
            app.height / 2 - (app.height - 100) / 2 < headY < app.height / 2 + (app.height - 100) / 2):
        app.gameOver = True

def onStep(app):
    if not (app.gamePaused or app.gameOver):
        if app.cursor is not None:
            headX, headY = app.snake[0]
            mouseX, mouseY = app.cursor
            dx = mouseX - headX
            dy = mouseY - headY
            magnitude = (dx ** 2 + dy ** 2) ** 0.5

            if magnitude != 0:
                directionX = dx / magnitude
                directionY = dy / magnitude
            else:
                directionX, directionY = 0, 0

            newHeadX = headX + directionX * app.speed
            newHeadY = headY + directionY * app.speed

            # Update snake and move the head
            app.snake.insert(0, (newHeadX, newHeadY))
            if len(app.snake) > app.snakeLength:
                app.snake.pop()

            app.cameraOffsetX = newHeadX - app.width / 2
            app.cameraOffsetY = newHeadY - app.height / 2

            checkCollision(app)
            checkCollisionWithLand(app)

def onMouseMove(app, mouseX, mouseY):
    app.cursor = (mouseX, mouseY)

def onMousePress(app, mouseX, mouseY):
    app.speed = app.boostedSpeed
    app.accelerating = True
    onStep(app)

def onMouseRelease(app, mouseX, mouseY):
    app.speed = app.defaultSpeed
    app.accelerating = False
    onStep(app)

def onKeyPress(app, key):
    if key == 'r':
        reset(app)
    elif key == 'p':
        app.gamePaused = not app.gamePaused
    if key == "space":
        app.snakeLength += 2
        if app.snakeLength % 8 == 0:    
            app.snakeFatness += 2
    if key == 'd':
        for x, y in app.snake:
            offsetX = random.uniform(-app.snakeFatness, app.snakeFatness)
            offsetY = random.uniform(-app.snakeFatness, app.snakeFatness)
            app.circlePositions.append((x + offsetX, y + offsetY))

runApp(width = 600, height = 600)