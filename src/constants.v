module main

import gx
import math

const (
	background_color = gx.black
	screen_height    = 800
	screen_width     = 800

	// physics
	g                = 6.67408 * math.pow(10, -11)
	delay            = 50

	// stars attributes
	star_amount      = 100
	radius_min = 1
	radius_max = 40
	mass_min   = 5000
	mass_max   = 50000
)
