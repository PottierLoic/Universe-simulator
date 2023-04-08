module main

import gx

struct Star {
mut:
	x      f32
	y      f32
	mass   f32
	radius f32
	color  gx.Color
}

fn init_star(x f32, y f32, mass f32, radius f32, color gx.Color) Star {
	return Star{
		x: x
		y: y
		mass: mass
		radius: radius
		color: color
	}
}
