module main

import gg
import gx

struct App {
mut:
	gg &gg.Context = unsafe { nil }
	universe Universe = init_universe()
}

fn (mut app App) display() {
	print('display')
	for star in app.universe.stars {
		app.gg.draw_circle_filled(star.x - star.radius / 2, star.y + star.radius / 2, star.radius, star.color)
	}
}

fn frame(mut app App) {
	app.gg.begin()
	app.display()
	app.gg.end()
}

fn main() {
	mut app := App{
		gg: 0
	}
	app.gg = gg.new_context(
		bg_color: background_color
		frame_fn: frame
		user_data: &app
		width: screen_width
		height: screen_height
		create_window: true
		resizable: false
		window_title: 'Universe simulator'
	)

	app.gg.run()
}
