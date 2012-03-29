
now()
{
	date +%s
}

poll_every=1800 #check the weather every 30 min, otherwise, return cached weather
$(weather.py > ~/.weather)
weather()
{
	last_run=$(stat -c %Y ~/.weather)
	if [ $(( $last_run + $poll_every )) -lt $(now) ]; then
		$(weather.py > ~/.weather)
	fi
	cat ~/.weather
}


PS1='$(weather) \u@\h\$ '
