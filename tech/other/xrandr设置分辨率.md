alias dispon='xrandr --output HDMI1 --auto --display '
alias dispoff='xrandr --output HDMI1 --off --display '

xrandr -s 1024x768

xrandr --output VGA --same-as LVDS --auto
xrandr --output VGA --same-as LVDS --mode 1024x768
xrandr --output VGA --right-of LVDS --auto
xrandr --output VGA --off
xrandr --output VGA --auto --output LVDS --off
xrandr --output VGA --off --output LVDS --auto


xrandr --output VGA-0 --right-of LVDS --auto
xrandr --output LVDS --right-of VGA-0 --mode 1366x768
xrandr --output LVDS --mode 1024x768
xrandr --output VGA-0 --auto
xrandr --output VGA-0 --off  -s 1024x768


xrandr --output VGA --same-as LVDS --auto
xrandr --output VGA --same-as LVDS --mode 1024x768
xrandr --output VGA --right-of LVDS --auto
xrandr --output VGA --off
xrandr --output VGA --auto --output LVDS --off
xrandr --output VGA --off --output LVDS --auto




xrandr --output VGA-0 --right-of LVDS --auto
xrandr --output LVDS --right-of VGA-0 --mode 1366x768
xrandr --output LVDS --mode 1024x768
xrandr --output VGA-0 --auto
xrandr --output VGA-0 --off 
