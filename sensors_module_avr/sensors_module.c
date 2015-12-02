/* Sensors Monitoring API */

/* Copyright (C) 2015  Augusto Lopez Dantas aldantas@protonmail.com */

/* This program is free software; you can redistribute it and/or modify */
/* it under the terms of the GNU General Public License as published by */
/* the Free Software Foundation; either version 2 of the License, or */
/* (at your option) any later version. */

/* This program is distributed in the hope that it will be useful, */
/* but WITHOUT ANY WARRANTY; without even the implied warranty of */
/* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the */
/* GNU General Public License for more details. */

/* You should have received a copy of the GNU General Public License along */
/* with this program; if not, write to the Free Software Foundation, Inc., */
/* 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA. */

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include <avrutil/usart.h>
#include "dht11.h"

#define LIGHT 'l'
#define TEMPERATURE 't'
#define HUMIDTY 'h'

uint8_t volatile sensor;
uint8_t volatile dht11_value;
int8_t volatile ret;

ISR(USART_RX_vect)
{
	sensor = USART_receive_byte();
	switch (sensor) {
	case LIGHT:
		ADCSRA |= (1 << ADSC);
		break;
	case TEMPERATURE:
		do {
			ret = DHT11_get_temperature();
		} while(ret == -1);
		dht11_value = ret;
		USART_print_byte(dht11_value);
		USART_print_string("*");
		break;
	case HUMIDTY:
		do {
			ret = DHT11_get_humidity();
		} while(ret == -1);
		dht11_value = ret;
		USART_print_byte(dht11_value);
		USART_print_string("*");
		break;
	}
}

ISR(ADC_vect)
{
	uint8_t high, low;
	low = ADCL;
	high = ADCH;
	uint16_t value = high;
	value = (value << 8) | low;
	USART_print_word(value);
	USART_print_string("*");
}

int main(void)
{
	ADMUX = (1 << REFS0) | (1 << MUX2) | (1 << MUX0);
	// ADC Prescaler divisor: 64
	ADCSRA |= (1 << ADPS2) | (1 << ADPS1) | (1 << ADEN) | (1 << ADIE);

	USART_init();
	USART_enable_rx_interrupt;
	sei();

	while(1);

	return 0;
}
