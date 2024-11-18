from cmu_graphics import *
import math
import random

def onAppStart(app):
    resetGlow(app)

# GIT TEST

def resetGlow(app):
    app.width = 1000
    app.height = 800
    app.blobX = app.width / 2
    app.blobY = app.height / 2
    app.glowFactor = 0.5
    app.glowSpeed = 0.025
    app.colorStart = randomColor()
    app.colorEnd = randomColor()
    app.stepsPerSecond = 60
    app.time = 0
    app.glowRadiusBase = 115
    app.glowRadiusAmplitude = 4
    app.glowSpeedMultiplier = 0.05
    app.glowRadius = app.glowRadiusBase

def randomColor():
    return rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def colorSwitcher(color1, color2, factor):
    return rgb(
        int(color1.red + (color2.red - color1.red) * factor),
        int(color1.green + (color2.green - color1.green) * factor),
        int(color1.blue + (color2.blue - color1.blue) * factor)
    )

def onStep(app):
    app.glowFactor += app.glowSpeed
    if app.glowFactor >= 1.5 or app.glowFactor <= 0.5:
        app.glowSpeed *= -1
    
    app.time += app.glowSpeedMultiplier
    app.glowRadius = app.glowRadiusBase + app.glowRadiusAmplitude * math.sin(app.time)

def redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill="black")
    currentColor = colorSwitcher(app.colorStart, app.colorEnd, (app.glowFactor - 0.5))
    gradientStartColor = rgb(255, 255, 255)
    gradientCenterColor = rgb(0, 0, 0)
    drawCircle(app.blobX, app.blobY, app.glowRadius, fill=gradient(gradientStartColor, gradientCenterColor, start='center'))
    drawCircle(app.blobX, app.blobY, 70, fill=currentColor)

runApp(width=1000, height=800)