
//#define SSD1306_64X32
#define SSD1306_128X64
#include "ch32v003fun.h"
#include <stdio.h>
#include "ssd1306_i2c.h"
#include "ssd1306.h"
#include "qr.h"
#include <stdio.h>

void init_screen()
{
	if ( !ssd1306_i2c_init() )
	{
		// Get the length of the text string

		// Initialize the OLED display
		ssd1306_init();
	}
	else
	{
		// Print an error message if the screen initialization fails
		printf( "%s", "error in screen init." );
	}
}

int main()
{
	SystemInit();	// 48MHz internal clock
	Delay_Ms( 200 );
	init_screen();
	
    while(1) {
        ssd1306_drawImage( 20, 0, qr_code_one, 64, 64, 1 );
    ssd1306_refresh();
	Delay_Ms( 2000 );
    }
}