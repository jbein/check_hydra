# check_hydra
Monitor your Ai Hydra 26HD with Icinga2.

## Usage

./check_hydra.py -h HOST -m MODE

## Modes
leds: check the actual value of all LED's with performance-data.
```
./check_hydra.py -h HOST -m leds
OK - LED's: blue=54.7,response_code=0.0,uv=13.4,royal=60.0,deep_red=8.0,green=12.0,cool_white=66.7,violet=14.7|blue=54.7,response_code=0.0,uv=13.4,royal=60.0,deep_red=8.0,green=12.0,cool_white=66.7,violet=14.7
```
power: check the actual used power in watt's all LED's and aggregated, with performance-data.
```
./check_hydra.py -h HOST -m power
OK - 43.664 Watt's are in use. | watt=43.664,blue=10.885,uv=0.964,royal=14.28,deep_red=0.296,green=0.492,cool_white=15.674,violet=1.073
```
checkfirmware: check the version of the firmware.
```
./check_hydra.py -h HOST -m checkfirmware
OK - No update availavble. Current version: 2.0.0-16
```
