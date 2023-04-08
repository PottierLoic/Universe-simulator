module main

import rand
import gx

struct Universe {
mut:
	stars []Star
}

fn (mut u Universe) update() {
	mut new_stars := []Star{}
	for star in u.stars {
		for star2 in u.stars {
			if star != star2 {
				// aplly forces
			}
		}
	}
}


fn init_universe() Universe {
	mut u := Universe{}
	for i := 0; i < star_amount; i++ {
		x, y := rand.f32_in_range(0, screen_width) or { 0 }, rand.f32_in_range(0, screen_height) or { 0 }
		mass := rand.f32_in_range(mass_min, mass_max) or { 0 }
		radius := rand.f32_in_range(radius_min, radius_max) or { 0 }
		color := gx.yellow
		u.stars << init_star(x, y, mass, radius, color)
	}
	return u
}
