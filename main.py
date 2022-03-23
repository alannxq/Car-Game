import turtle
import random
import time


PLAYER_SPEED = 20
SPAWN_RATE = 500 ## higher = less frequent
ENEMY_CAR_SPEED = 1

score = 0




wn = turtle.Screen()
wn.setup(1000, 800)
wn.tracer(0, 0)

car_picture = "car.gif"
road_bg = "road.gif"
enemy = "enemy.gif"

wn.register_shape(car_picture)
wn.register_shape(road_bg)
wn.register_shape(enemy)



## ROAD
road = turtle.Turtle()
road.penup()
road.speed(0)
road.shape(road_bg)


## PLAYER CAR
player_car = turtle.Turtle()
player_car.penup()
player_car.shape(car_picture)
player_car.speed(0)
player_car.goto(player_car.xcor(), player_car.ycor() - 250)


## SCORE

sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("black")
sketch.penup()
sketch.hideturtle()
sketch.goto(-350, 350)
sketch.write(f"Score: {score}",
             align="center", font=("Iosevka Medium", 24, "normal"))


enemy_cars = []

def makeEnemyCar(starting_x):
	enemy_car = turtle.Turtle()
	enemy_car.penup()
	enemy_car.goto(starting_x, 400)
	enemy_car.speed(0)
	enemy_car.shape(enemy)

	enemy_cars.append(enemy_car)

def goLeft():
	player_car.setx(player_car.xcor() - PLAYER_SPEED)

def goRight():
	player_car.setx(player_car.xcor() + PLAYER_SPEED)

def goUp():
	player_car.sety(player_car.ycor() + PLAYER_SPEED)

def goDown():
	player_car.sety(player_car.ycor() - PLAYER_SPEED)

## KEY BINDING
wn.listen()
wn.onkeypress(goLeft, "a")
wn.onkeypress(goRight, "d")
wn.onkeypress(goUp, "w")
wn.onkeypress(goDown, "s")

count_to_place_another_car = 0 ## instead of waiting to place, its completely based on how fast your computer is lol

while True:
	wn.update()

	for index, car in enumerate(enemy_cars):
		car.sety(car.ycor() - ENEMY_CAR_SPEED)

		if car.ycor() < -420:
			car.goto(1000,1000)
			#car.reset()
			enemy_cars.pop(index)

			score += 1
			if random.randint(1,2) == 1: SPAWN_RATE -= 50 
			else: SPAWN_RATE += 35

			ENEMY_CAR_SPEED += 0.05

			sketch.clear()
			sketch.write(f"Score: {score}", align="center", font=("Iosevka Medium", 24, "normal"))

		if car.xcor() < player_car.xcor() + 50 and car.xcor() > player_car.xcor() - 50 and car.ycor() < player_car.ycor() + 150 and car.ycor() > player_car.ycor() - 150:
			print(f"score: {score}")
			quit()

	if count_to_place_another_car % SPAWN_RATE == 0:
		makeEnemyCar(random.randint(-170, 170))

	if player_car.xcor() > 175 or player_car.xcor() < -175:
		print(f"score: {score}")
		quit()
	
	count_to_place_another_car += 1
